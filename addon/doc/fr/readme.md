# Manuel de zPod

zPod est une extension pour avoir un aperçu d'un fichier multimédia de façon rapide.

Ils m'ont proposé l'idée de créer une extension facile afin d'explorer rapidement un dossier avec de nombreux fichiers multimédia sans avoir à entrer dans un lecteur.

Ceci est utile pour les personnes qui ont besoin de voir rapidement le contenu d'un fichier multimédia et d'agir sur lui, si ce n'est pas le fichier que nous recherchons nous passons rapidement au suivant afin d'avoir un aperçu de celui-ci.

Cette extension peut lire jusqu'à 139 extensions multimédia.

Il est valable pour les extensions audio et vidéo, mais je me permets de préciser que s'il s'agissait d'une vidéo, seul l'audio sera entendu, cette extension ne dispose pas d'une interface et est tout géré par les combinaisons de touches attribuées par l'utilisateur.

Notez également que cela est valable au cas où nous avons un NVDA portable et sur un ordinateur qui n'est pas le notre et nous voulons lire quelque chose.

Cette extension n'a pas besoin d'installer quelque chose sur l'ordinateur ni dépend d'une bibliothèque externe à l'extension afin qu'il soit valide pour prévisualiser un fichier multimédia à un moment donné que nous n'avons pas de lecteur commun.

## Note importante de l'auteur

Cette extension n'est pas destinée à être un lecteur multimédia, elle peut être utilisée pour écouter un fichier multimédia en soi, mais elle ne deviendra jamais un lecteur commun ni les nouvelles options ne seront ajoutées à l'extension pour devenir telle.

Il s'agit de couvrir le besoin de voir rapidement le contenu d'un fichier multimédia et rien de plus.

## Utilisation de l'extension

Cette extension dans sa première exécution n'a pas de touche attribuée pour cela nous devrons donc aller dans le menu NVDA / Préférences / Gestes de commandes dans la catégorie zPod puis configurer les touches que nous considérons que nous allons avoir besoin.

Une fois que l'on a attribuée le plus important des gestes de commandes est d'exécuter Zpod avec laquel nous allons exécuter l'extension.

Lorsque le focus est mis sur un fichier multimédia et nous appuyons sur cette combinaison il commencera la lecture, pouvant agir sur le fichier avec le reste des combinaisons de touches.

Si le fichier multimédia n'était pas compatible, nous serons informés des messages correspondants.

Vous ne pouvez pas choisir plus d'un fichier à lire, si nous le faisons, nous serons informés avec un message.

Par conséquent, je donne un exemple si nous sommes dans un répertoire avec de nombreux fichiers multimédia et que nous ne savons pas ce que nous voulons, nous pouvons explorer le répertoire et aller en appuyant sur Exécuter zPod jusqu'à trouver celui que nous voulons.

Lorsque ce fichier est en cours de lecture et que nous choisissons un autre, automatiquement celui qui est en cours de lecture s'arrêtera et il commencera celui que nous Choisissons.

## Gestes de commandes

Elle apporte 8 combinaisons qui sont les suivantes:

* Exécuter zPod: Avec cette combinaison une fois configurée, nous commencerons la lecture du fichier multimédia qui a le focus.

* Mettre en pause la lecture: Avec cela, nous mettrons en pause le fichier multimédia qui est en cours de lecture.

* Arrêter zPod: Avec cela, nous arrêterons la lecture du fichier multimédia qui est en cours de lecture.

* Obtenir la durrée de temps écoulé / total de lecture: Avec cette combinaison, nous serons informés de la durée du temps écoulée de lecture du fichier multimédia et la durée du temps totale de lecture du fichier multimédia.

* Baisser le volume et Augmenter le volume: Avec cela, nous allons baisser et augmenter le volume de lecture, lorsque nous appuyons sur lui, nous serons informés dans quel pourcentage est celui-ci. Chaque modification du son sera sauvegardé dans le fichier NVDA.ini et il sera établi pour la prochaine fois. Par défaut, la première fois le son est de 50%.

* Reculer la lecture et Avancer la lecture: Avec ces combinaisons, nous allons reculer ou avancer la durée  de temps dans le fichier multimédia en cours de lecture. Par défaut, la première fois est sur reculer 5 secondes et avancer 15 secondes.

Ceci peut être configuré dans Préférences / Paramètres / zPod, dans le dialogue Paramètres de NVDA , nous pouvons choisir la durée de temps que nous souhaitons pour chaque action de 1 seconde à 15 minutes.

Ces réglages seront également sauvegardées dans le fichier NVDA.ini et seront établies pour la prochaine fois.

## Recommandation très importante pour pouvoir configurer le premier geste de commande Exécuter zPod

Juste au cas où, je vous dis que dans aucun cas, vous devez faire Contrôle + c pour démarrer l'extension, cela est fait par l'extension en interne, il vous suffit d'utiliser la combinaison que nous allons assignée au geste de commande appelé "Exécuter zPod".

N'utilisez pas dans la combinaison de touches pour démarrer l'extension ni la touche control ni les symboles, car ils donneront des erreurs car le geste physique est mélangé avec le virtuel que nous envoyons, c'est-à-dire que si nous avons par exemple un control + alt +i pour vraiment démarrer ensuite, ceci est convertit en deux contrôle car il est étroitement lié à celui que l'extension de manière interne fait, c'est-à-dire lorsque nous sommes sur un fichier multimédia ce qu'il fait est qu'il simule une combinaison de touche du fichier exactement Ctrl +C, exacte ceci copie le fichier dans le presse-papiers et on obtient le chemin du fichier à être exécuté par zPod.

Dans les autres combinaisons de touches, cela n'a pas d'importance, mais dans le démarrage de l'extension non.

N'oubliez pas que cette extension est déjà faite et qu'il n'aura donc pas plus de développement que nécessaire à sa maintenance et qui fonctionne avec les futures versions de NVDA.

## Extensions supportées

ac3, a52, eac3, mlp, dts, dts-hd, dtshd, true-hd, thd, truehd, thd+ac3, tta, pcm, wav, aiff, aif, aifc, amr, awb, au, snd, lpcm, yuv, y4m, ape, wv, shn, m2ts, m2t, mts, mtv, ts, tsv, tsa, tts, trp, adts, adt, mpa, m1a, m2a, mp1, mp2, mp3, mpeg, mpg, mpe, mpeg2, m1v, m2v, mp2v, mpv, mpv2, mod, tod, vob, vro, evob, evo, mpeg4, m4v, mp4, mp4v, mpg4, m4a, aac, h264, avc, x264, 264, hevc, h265, x265, 265, flac, oga, ogg, opus, spx, ogv, ogm, ogx, mkv, mk3d, mka, webm, weba, avi, vfw, divx, 3iv, xvid, nut, flic, fli, flc, nsv, gxf, mxf, wma, wm, wmv, asf, dvr-ms, dvr, wtv, dv, hdv, flv, f4v, f4a, qt, mov, hdmov, rm, rmvb, ra, ram, 3ga, 3ga2, 3gpp, 3gp, 3gp2, 3g2, ay, gbs, gym, hes, kss, nsf, nsfe, sap, spc, vgm, vgz, m3u, m3u8, pls, cue

## Remerciements et traducteurs

* Reinier Ginnari: Pour me commenter sont besoin et me donner l'idée. Aussi pour me donner le nom de l'extension et par ses tests de l'extension et de ses commentaires pour devenir ce que l'extension est.
* Français: Rémy Ruiz
* Portugais: Ângelo Miguel Abrantes
* Turc: umut korkmaz
* Italien: Alessio Lenzi
* Arabe: Wafiq Taher

# Journal des changements.
## Version 0.2.

* Ajout de la compatibilité avec NVDA 2022.1.

* Ajout de la langue arabe.

## Version 0.1.5. 

* Ajout de la traduction française et Portugaise (Portugal / Brésil).

## Version 0.1.

* Version initiale.