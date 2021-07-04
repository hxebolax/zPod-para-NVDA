# -*- coding: utf-8 -*-
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.

# import the necessary modules (NVDA)
import globalPluginHandler
import addonHandler
import keyboardHandler
import globalVars
import gui
import ui
import config
from scriptHandler import script
from gui.settingsDialogs import NVDASettingsDialog, SettingsPanel
from gui import guiHelper, nvdaControls
import wx
import time
from datetime import timedelta
import ctypes
import os, sys
from .lib import mpv
from .win32 import win32clipboard as cb
from .pubsub import pub

addonHandler.initTranslation()

# Extensiones
dvd_blu = ["ac3", "a52", "eac3", "mlp", "dts", "dts-hd", "dtshd", "true-hd", "thd", "truehd", "thd+ac3", "tta"]
Uncompressed = ["pcm", "wav", "aiff", "aif", "aifc", "amr", "awb", "au", "snd", "lpcm", "yuv", "y4m"]
free_lossless = ["ape", "wv", "shn", ]
mpeg = ["m2ts", "m2t", "mts", "mtv", "ts", "tsv", "tsa", "tts", "trp", "adts", "adt", "mpa", "m1a", "m2a", "mp1", "mp2", "mp3", "mpeg", "mpg", "mpe", "mpeg2", "m1v", "m2v", "mp2v", "mpv", "mpv2", "mod", "tod", "vob", "vro", "evob", "evo", "mpeg4", "m4v", "mp4", "mp4v", "mpg4", "m4a", "aac", "h264", "avc", "x264", "264", "hevc", "h265", "x265", "265", ]
xiph = ["flac", "oga", "ogg", "opus", "spx", "ogv", "ogm", "ogx"]
matroska = ["mkv", "mk3d", "mka", "webm", "weba"]
misc = ["avi", "vfw", "divx", "3iv", "xvid", "nut", "flic", "fli", "flc", "nsv", "gxf", "mxf", ]
windows = ["wma", "wm", "wmv", "asf", "dvr-ms", "dvr", "wtv"]
dv = ["dv", "hdv", ]
flash = ["flv", "f4v", "f4a"]
quicktime = ["qt", "mov", "hdmov"]
real = ["rm", "rmvb", "ra", "ram"]
tres_gpp = ["3ga", "3ga2", "3gpp", "3gp", "3gp2", "3g2"]
video_game = ["ay", "gbs", "gym", "hes", "kss", "nsf", "nsfe", "sap", "spc", "vgm", "vgz"]
playlist = ["m3u", "m3u8", "pls", "cue"]

listaExtensiones = dvd_blu + Uncompressed + free_lossless + mpeg + xiph + matroska + misc + windows + dv + flash + quicktime + real + tres_gpp + video_game + playlist

dictTiempos = {
	0:1,
	1:5,
	2:15,
	3:30,
	4:60,
	5:300,
	6:600,
	7:900,
}
tiempoDescripcion = [
	_("1 segundo"),
	_("5 segundos"),
	_("15 segundos"),
	_("30 segundos"),
	_("1 minuto"),
	_("5 minutos"),
	_("10 minutos"),
	_("15 minutos"),
]

def initConfiguration():
	confspec = {
		"atras": "integer(default=1, min=0, max=7)",
		"adelante": "integer(default=2, min=0, max=7)",
		"volumen": "integer(default=50, min=0, max=100)",
	}
	config.conf.spec['zPod'] = confspec

def getConfig(key):
	value = config.conf["zPod"][key]
	return value

def setConfig(key, value):
	try:
		config.conf.profiles[0]["zPod"][key] = value
	except:
		config.conf["zPod"][key] = value

initConfiguration()
tempAtras = getConfig("atras")
tempAdelante = getConfig("adelante")
volumenGeneral = getConfig("volumen")

player = mpv.MPV(ytdl=True, video=False)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)

		if globalVars.appArgs.secure: return

		NVDASettingsDialog.categoryClasses.append(zPodPanel)

# Variables
		pub.subscribe(self.onActualizaTiempo, "tiempo")
		pub.subscribe(self.nulo, "terminado")

		self.reproductor = MPVClass()
		self.tiempoTotal = None
		self.tiempo = _("Sin tiempo")

	def terminate(self):
		NVDASettingsDialog.categoryClasses.remove(zPodPanel)

	def nulo(self, event):
		self.tiempo = _("Sin tiempo")

	def onActualizaTiempo(self, event):
		self.tiempo = "{} / {}".format(str(event), self.tiempoTotal)

	def runPlay(self):
		time.sleep(0.7)
		keyboardHandler.KeyboardInputGesture.fromName("Control+c").send()
		try:
			cb.OpenClipboard()
		except pywintypes.error:
			cb.CloseClipboard()
			cb.OpenClipboard()

		if cb.IsClipboardFormatAvailable(cb.CF_HDROP):
			clipboard_file_path = cb.GetClipboardData(cb.CF_HDROP)
			cb.CloseClipboard()
			numList = len(clipboard_file_path)
			if numList == 0:
				ui.message(_("No hay nada compatible en el foco"))
				return False
			else:
				if numList == 1:
					if os.path.splitext(clipboard_file_path[0])[-1].lower().replace(".", "") in listaExtensiones:
						return clipboard_file_path[0]
					else:
						ui.message(_("El formato del archivo no es compatible"))
						return False
				else:
					ui.message(_("Ha seleccionado %s ficheros. Seleccione solo un fichero.") % numList)
					return False
		else:
			ui.message(_("No hay nada compatible en el foco"))
			return False

	@script(gesture=None, description= _("Ejecutar zPod"), category= _("zPod"))
	def script_zPodRun(self, event):
		p = self.runPlay()
		if ctypes.windll.user32.OpenClipboard(None):
			ctypes.windll.user32.EmptyClipboard()
			ctypes.windll.user32.CloseClipboard()
		if p == False:
			return
		else:
			self.reproductor.volumen(volumenGeneral)
			self.reproductor.play(p)
			self.duracion = self.reproductor.duracion()
			tiempo1 = int(self.duracion)
			self.tiempoTotal = str(timedelta(seconds=tiempo1))

	@script(gesture=None, description= _("Bajar volumen"), category= _("zPod"))
	def script_bajarVol(self, event):
		global volumenGeneral
		if volumenGeneral == 0:
			ui.message(_("No se puede bajar más el volumen ya se encuentra al 0%"))
		else:
			vol1 = volumenGeneral - 1
			volumenGeneral = vol1
			self.reproductor.volumen(volumenGeneral)
			ui.message(_("{}%").format(volumenGeneral))
			setConfig("volumen", volumenGeneral)

	@script(gesture=None, description= _("Subir volumen"), category= _("zPod"))
	def script_subirVol(self, event):
		global volumenGeneral
		if volumenGeneral == 100:
			ui.message(_("No se puede subir más el volumen ya se encuentra al 100%"))
		else:
			vol1 = volumenGeneral + 1
			volumenGeneral = vol1
			self.reproductor.volumen(volumenGeneral)
			ui.message(_("{}%").format(volumenGeneral))
			setConfig("volumen", volumenGeneral)

	@script(gesture=None, description= _("Poner en pausa la reproducción"), category= _("zPod"))
	def script_pausePlay(self, event):
		self.reproductor.pause()

	@script(gesture=None, description= _("Retroceder la reproducción "), category= _("zPod"))
	def script_atrasar(self, event):
		self.reproductor.atrasar(tempAtras)

	@script(gesture=None, description= _("Adelantar la reproducción "), category= _("zPod"))
	def script_adelantar(self, event):
		self.reproductor.adelantar(tempAdelante)

	@script(gesture=None, description= _("Obtener tiempo reproducido / total"), category= _("zPod"))
	def script_tiempo(self, event):
		ui.message(self.tiempo)

	@script(gesture=None, description= _("Detener zPod"), category= _("zPod"))
	def script_terminar(self, event):
		self.reproductor.stop()
		self.tiempo = _("Sin tiempo")

class zPodPanel(SettingsPanel):

	title=_("zPod")

	def makeSettings(self, sizer):
		helper=guiHelper.BoxSizerHelper(self, sizer=sizer)

		self.choiceAtrasar = helper.addLabeledControl(_("Seleccione el tiempo para retroceder la reproducción:"), wx.Choice, choices=tiempoDescripcion)
		self.choiceAtrasar.Bind(wx.EVT_CHOICE, self.onChoiceAtrasar)

		self.choiceAdelantar = helper.addLabeledControl(_("Seleccione el tiempo para adelantar la reproducción:"), wx.Choice, choices=tiempoDescripcion)
		self.choiceAdelantar.Bind(wx.EVT_CHOICE, self.onChoiceAdelantar)

		indexAtras = tempAtras
		self.choiceAtrasar.Selection = indexAtras
		indexAdelante = tempAdelante
		self.choiceAdelantar.Selection = indexAdelante

		self.onChoiceAtrasar(None)
		self.onChoiceAdelantar(None)

	def onSave(self):
		setConfig("atras", self.choiceAtrasar.Selection)
		setConfig("adelante", self.choiceAdelantar.Selection)

	def onChoiceAtrasar(self, event):
		global tempAtras
		tempAtras = self.choiceAtrasar.Selection

	def onChoiceAdelantar(self, event):
		global tempAdelante
		tempAdelante = self.choiceAdelantar.Selection

class MPVClass():
	def __init__(self):

		self.pausa = False
		self.player = player

	def atrasar(self, valor):
		try:
			temp = dictTiempos.get(valor)
			self.player.seek(- temp)
		except:
			pass

	def adelantar(self, valor):
		try:
			self.player.seek(dictTiempos.get(valor))
		except:
			pass

	def volumen(self, valor):
		self.player.volume = valor

	def pause(self):
		if self.pausa:
			self.pausa = False
			self.player.pause = self.pausa
		else:
			self.pausa = True
			self.player.pause = self.pausa

	def stop(self):
		self.player.command('stop')
		self.pausa = False

	def play(self, archivo):
		self.pausa = False
		self.player.play(archivo)

	def duracion(self):
		time.sleep(0.2)
		return self.player.duration

	@player.property_observer('time-pos') #'time-pos'
	def observe_time_pos(_name, value):
		if value == None:
			pass
		else:
			f = (lambda x, y: (int(x), int(x*y) % y/y))(float(value), 1e0)
			x=timedelta(seconds=f[0])
			wx.CallAfter(pub.sendMessage, "tiempo", event=x)

	@player.event_callback('end_file')
	def end_file_event(event):
		try:
			wx.CallAfter(pub.sendMessage, "terminado", event=None)
		except:
			pass
