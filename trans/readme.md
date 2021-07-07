# Manual de zPod

zPod es un complemento para previsualizar multimedia de manera rápida.

Me ofrecieron la idea de crear un complemento que de manera fácil uno pudiese explorar rápidamente una carpeta con muchos archivos multimedia sin necesidad de entrar en un reproductor.

Esto es útil para aquellas personas que necesiten ver rápidamente el contenido de un archivo multimedia y actuar sobre él, si no es el que se busca pasar rápidamente al siguiente y poderlo previsualizar.

Este complemento puede reproducir hasta 139 extensiones multimedia.

Es valido para extensiones tanto de audio como de video pero dejando claro que si fuese un video solo se escuchara el audio, este complemento no tiene interface y se maneja todo a través de teclas asignadas por el usuario.

Decir que también es valido por si llevamos un NVDA portable y en un equipo que no es nuestro deseamos reproducir algo.

Este complemento no necesita tener nada instalado en el ordenador ni depende de ninguna librería externa al complemento por lo que es valido para previsualizar un archivo multimedia en un momento dado que no tengamos un reproductor común.

## Nota importante del autor

Este complemento no pretende ser un reproductor multimedia, se puede usar para escuchar un archivo multimedia en sí, pero nunca se convertirá en un reproductor común ni se le agregarán nuevas opciones que encaminen al complemento en convertirse en tal.

Viene a cubrir una necesidad de poder ver rápidamente el contenido de un archivo multimedia y nada más.

## Uso del complemento

Este complemento en su primera ejecución no tiene ninguna tecla asignada por lo que tendremos que ir a Preferencias / Gestos de entrada / zPod y configurar a nuestro gusto las teclas que consideremos que vamos a necesitar.

Una vez asignadas la más importante es Ejecutar zPod con la cual ejecutaremos el complemento.

Cuando el foco este encima de un archivo multimedia y presionemos esta combinación empezara a reproducirse, pudiendo actuar sobre el archivo con el resto de combinaciones de teclas.

En caso que el archivo multimedia no fuese compatible se nos informara con los correspondientes mensajes.

No se puede elegir más de un archivo para ser reproducido, si lo hiciéramos se nos informara con un mensaje.

Por lo tanto para poner un ejemplo si estamos en un directorio con muchos archivos multimedia y no sabemos cual es el que deseamos podemos ir explorando el directorio e ir pulsando el iniciar el complemento hasta encontrar el que deseamos. 

Cuando este sonando un archivo y elijamos otro automáticamente el que suena se parara y empezara el que elijamos.

## Gestos de entrada

Trae 8 combinaciones que son las siguientes:

* Ejecutar zPod: Con esta combinación una vez configurada iniciaremos la reproducción del archivo multimedia que tenga el foco.

* Poner en pausa la reproducción: Con esto pondremos en pausa el archivo multimedia que este sonando.

* Detener zPod: Con esto pararemos la reproducción del archivo multimedia que este sonando.

* Obtener tiempo reproducido / total: Con esta combinación se nos informara del tiempo transcurrido de reproducción del archivo multimedia y el tiempo total del archivo multimedia.

* Bajar volumen y Subir volumen: Con esto bajaremos y subiremos el volumen de la reproducción, cuando lo pulsemos se nos informara en que porcentaje esta. Cada modificación del sonido se guardara en el archivo NVDA.ini y quedara establecido para la siguiente vez. Por defecto la primera vez es del 50% del sonido.

* Retroceder la reproducción y Adelantar la reproducción: Con estas combinaciones disminuiremos o aumentaremos el tiempo en el archivo multimedia que este sonando. Por defecto la primera vez es de retroceder 5 segundos y adelantar 15 segundos.

Esto se puede configurar en Preferencias / Opciones / zPod, en el panel de opciones de NVDA podremos elegir el tiempo que deseamos para cada acción desde 1 segundo hasta 15 minutos.

Estas opciones se guardarán igualmente en el archivo NVDA.ini y quedaran establecidas para la siguiente vez.

## Extensiones soportadas

ac3, a52, eac3, mlp, dts, dts-hd, dtshd, true-hd, thd, truehd, thd+ac3, tta, pcm, wav, aiff, aif, aifc, amr, awb, au, snd, lpcm, yuv, y4m, ape, wv, shn, m2ts, m2t, mts, mtv, ts, tsv, tsa, tts, trp, adts, adt, mpa, m1a, m2a, mp1, mp2, mp3, mpeg, mpg, mpe, mpeg2, m1v, m2v, mp2v, mpv, mpv2, mod, tod, vob, vro, evob, evo, mpeg4, m4v, mp4, mp4v, mpg4, m4a, aac, h264, avc, x264, 264, hevc, h265, x265, 265, flac, oga, ogg, opus, spx, ogv, ogm, ogx, mkv, mk3d, mka, webm, weba, avi, vfw, divx, 3iv, xvid, nut, flic, fli, flc, nsv, gxf, mxf, wma, wm, wmv, asf, dvr-ms, dvr, wtv, dv, hdv, flv, f4v, f4a, qt, mov, hdmov, rm, rmvb, ra, ram, 3ga, 3ga2, 3gpp, 3gp, 3gp2, 3g2, ay, gbs, gym, hes, kss, nsf, nsfe, sap, spc, vgm, vgz, m3u, m3u8, pls, cue

## Agradecimientos

Reinier Ginnari: Por comentarme su necesidad y darme la idea. También por darme el nombre del complemento y por sus pruebas del complemento y su retroalimentación para llegar a ser lo que es el complemento.
# Registro de cambios.
## Versión 0.1.

* Versión inicial.