# Manuale di zPod

zPod è un componente aggiuntivo per ottenere rapidamente l'anteprima d'ascolto di un file multimediale.

Mi è stata proposta l'idea di creare un componente aggiuntivo con il quale  si potesse, in maniera semplice, sfogliare rapidamente una cartella contenente molti file multimediali, senza dover aprire un riproduttore.

Questo può tornare molto utile a quelle persone che vogliono conoscere velocemente il contenuto di un file multimediale per lavorare su di esso. In caso non fosse quello desiderato, poter passare rapidamente a quello successivo ed essere in grado di visualizzarlo in anteprima.

Con questo componente si possono riprodurre fino a 139 estensioni di file multimediali.

zPod funziona sia con estensioni di file audio che video ma si tenga presente che in caso di video, si sentirà solo l'audio. Questo componente non ha un'interfaccia ma tutto viene gestito tramite combinazioni di tasti assegnate dall'utente.

é molto utile anche se si possiede una versione portatile di NVDA e vogliamo riprodurre i file multimediali su un computer che non è nostro.

Questo componente non necessita di aver installato niente sul computer né dipende da alcuna libreria esterna. In questo modo tornerà molto utile per riprodurre in anteprima un file multimediale in caso non avessimo un lettore predefinito che lo possa gestire.

## Nota importante dell'autore

Questo componente non è concepito per essere un vero e proprio lettore multimediale, può essere utilizzato per ascoltare un file di questo tipo ma non diventerà mai un lettore o verranno aggiunte nuove opzioni che porteranno il componente ad esserlo in futuro.

Serve a coprire la necessità di riprodurre rapidamente un file multimediale e nulla più.

## Uso del componente

La prima volta che si esegue, il componente non ha tasti assegnati. Dovremo andare in Preferenze / Gesti e tasti d'immissione / zPod e configurare le combinazioni di tasti che riterremo più opportune.

La combinazione di tasti più importante da assegnare è avviare zPod, che serve proprio per iniziare l'ascolto di un file.

Quando il focus si trova su un file multimediale e si preme questa combinazione, inizierà la riproduzione e si potrà agire sul file con il resto delle combinazioni di tasti assegnabili.

Nel caso il file multimediale non fosse compatibile, saremo avvisati attraverso appositi messaggi.

Non è possibile selezionare più di un file da riprodurre, in caso verremo avvisati attraverso un apposito messaggio.

Per fare un esempio, se ci troviamo in una cartella che contiene molti file multimediali e non sappiamo quale riprodurre, possiamo selezionarli uno ad uno, premere la combinazione di tasti per la riproduzione fino a che non troviamo quello che desideriamo ascoltare.

Quando un file è in riproduzione e ne selezioniamo un'altro, quello in riproduzione si fermerà automaticamente e quello che selezioneremo subito dopo verrà riprodotto immediatamente.

## Gesti d'immissione

Si possono assegnare le seguenti 8 combinazioni di tasti:

* Avviare zPod: Una volta configurata questa combinazione, avvieremo la riproduzione del file multimediale che si troverà nel focus.

* Mettere in pausa la riproduzione: Con questa combinazione metteremo in pausa il file che stiamo ascoltando.

* Fermare zPod: Con questa combinazione fermeremo la riproduzione del file che stiamo ascoltando.

* Ottenere il tempo riprodotto/totale: Con questa combinazione potremo conoscere il tempo di riproduzione trascorso e quello complessivo del file in riproduzione.

* Abbassare e alzare il volume: Con queste combinazioni abbasseremo e alzeremo il volume della riproduzione. Ad ogni pressione verrà letta la percentuale raggiunta. La modifica verrà salvata nel file NVDA.ini e verrà mantenuta per le esecuzioni successive. Al primo avvio, la percentuale sarà impostata per default al 50% del suono.

* Riavvolgimento e avanzamento della riproduzione: Con queste combinazioni potremo avanzare o retrocedere nella riproduzione del file per il tempo impostato. Per default, il tempo è retrocedere di 5 secondi ed avanzare di 15 secondi.

Questa impostazione potraà essere configurata in Preferenze / Opzioni / zPod. Nella finestra delle opzioni potremo scegliere il tempo desiderato per ogni azione da 1 secondo a 15 minuti.

Queste impostazioni verranno salvate anche nel file NVDA.ini e verranno mantenute per le volte successive.

## Raccomandazione importante per poter configurare il primo gesto di immissione avviare zPod

Si raccomanda di non utilizzare mai Control + c per avviare il componente, dovremo utilizzare soltanto la combinazione che assegneremo nel gesto di immissione chiamato "Avviare zPod".

Si prega di non utilizzare ne il tasto control ne i simboli per impostare il gesto di avvio del componente, poichè si rischierebbe di mescolarli con gesti virtuali che il componente dovrà eseguire per realizzare la riproduzione di un file. Di fatto, zPod copia virtualmente il file in memoria per riprodurlo e se utilizzassimo control o tasti simili, la copia non avverrebbe perchè il componente li premerebbe 2 volte.

Per gli altri gesti non ci sarà nessun problema nell'utilizzare particolari combinazioni di tasti ma per l'avvio è fondamentale tenere conto di quanto detto sopra.

Si noti che questo componente è già completo e non saranno effettuati ulteriori aggiornamenti. Verrà effettuata solo normale attività di manutenzione in quanto continuerà a funzionare anche nelle future versioni di NVDA.

## Estensioni supportate

ac3, a52, eac3, mlp, dts, dts-hd, dtshd, true-hd, thd, truehd, thd+ac3, tta, pcm, wav, aiff, aif, aifc, amr, awb, au, snd, lpcm, yuv, y4m, ape, wv, shn, m2ts, m2t, mts, mtv, ts, tsv, tsa, tts, trp, adts, adt, mpa, m1a, m2a, mp1, mp2, mp3, mpeg, mpg, mpe, mpeg2, m1v, m2v, mp2v, mpv, mpv2, mod, tod, vob, vro, evob, evo, mpeg4, m4v, mp4, mp4v, mpg4, m4a, aac, h264, avc, x264, 264, hevc, h265, x265, 265, flac, oga, ogg, opus, spx, ogv, ogm, ogx, mkv, mk3d, mka, webm, weba, avi, vfw, divx, 3iv, xvid, nut, flic, fli, flc, nsv, gxf, mxf, wma, wm, wmv, asf, dvr-ms, dvr, wtv, dv, hdv, flv, f4v, f4a, qt, mov, hdmov, rm, rmvb, ra, ram, 3ga, 3ga2, 3gpp, 3gp, 3gp2, 3g2, ay, gbs, gym, hes, kss, nsf, nsfe, sap, spc, vgm, vgz, m3u, m3u8, pls, cue

## Ringraziamenti e traduttori

* Reinier Ginnari: Per avermi parlato della sua esigenza e avermi dato l'idea. Anche per avermi suggerito il nome del componente e per i suoi test e il suo feedback per renderlo il componente che è adesso.
* Francese: Rémy Ruiz
* Portoghese: Ángelo Abrantes
* Turco: umut korkmaz
* Italiano: Alessio Lenzi

# Registro delle modifiche.
## Versione 0.1.5.

* Aggiunte le lingue francese e portoghese (Portogallo / Brasile).

## Versione 0.1.

* Versione iniziale.