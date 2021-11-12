# zPod için Kılavuz:

zPod, medya dosyaları için hızlı bir önizleme eklentisidir.  

Bana, bir oynatıcıya girmek zorunda kalmadan birçok multimedya dosyasının bulunduğu bir klasörü kolayca keşfetmenizi sağlayacak bir eklenti oluşturma fikrini önerdiler.  

Bu, bir multimedya dosyasının içeriğini hızlı bir şekilde görmesi ve üzerinde hareket etmesi gerekenler için yararlıdır, eğer istediğiniz bu değilse, bir sonrakine hızlı bir şekilde gitmek ve onu önizlemek mümkün.  

Bu eklenti 139 adet multimedya uzantısını oynatabilir.  

Hem ses hem de video uzantıları için geçerlidir, Ancak video dosyalarında sadece ses duyulacağını, bu tamamlayıcının bir arabirime sahip olmadığını ve her şeyin kullanıcı tarafından atanan tuşlar aracılığıyla yönetildiğini bilmek gerekir.  

Taşınabilir NVDA sürümünde de geçerlidir.  

Bu eklentinin bilgisayarda yüklü olması gerekmez ve eklentinin dışındaki herhangi bir kitaplığa da bağımlı değildir, bu nedenle ortak bir oynatıcımız olmadığında bir multimedya dosyasını önizlemek için geçerlidir.  

## Yazardan önemli not:  

Bu eklentinin bir medya oynatıcı olması amaçlanmamıştır, bir medya dosyasını dinlemek için kullanılabilir, ancak asla ortak bir oynatıcı olmayacak veya eklentinin bir olmasına yol açan yeni seçenekler eklemeyecektir.  

Bir media dosyasının içeriğini hızlı bir şekilde görebilmeyi sağlar.  

## Eklentiyi kullanma:  

Bu eklentinin ilk kurulduğunda herhangi bir atanmış hareketi yoktur, bu nedenle Tercihler / Girdi hareketleri / zPod'a gitmemiz ve ihtiyaç duyacağımızı düşündüğümüz hareketleri beğenimize göre yapılandırmamız gerekmektedir.  

En önemlisi, zPod'u çalıştır hareketidir.  

Odak bir multimedya dosyasındayken ve bu kombinasyona bastığımızda, dosya üzerinde diğer tuş kombinasyonlarıyla hareket edebilecek şekilde çalmaya başlayacaktır.  

Multimedya dosyasının uyumlu olmaması durumunda ilgili mesajlarla bilgilendirileceğiz.  

Oynatmak için birden fazla dosya seçemeyiz, seçersek mesajla bilgilendiriliriz.  

Bu nedenle örnek vermek gerekirse, çok sayıda multimedya dosyasının bulunduğu bir dizindeysek ve hangisini istediğimizi bilmiyorsak, dizini araştırıp istediğimizi bulana kadar zPod'u çalıştır hareketine basabiliriz.  

Bir dosya oynatılırken başka bir dosya seçtiğimizde, çalmakta olan otomatik olarak duracak ve seçtiğimiz dosya başlayacaktır.  

## Girdi hareketleri:  

Aşağıda 8 girdi hareketi bulunur:  

* zPod'u çalıştır: Bu kombinasyonla, bir kez yapılandırıldıktan sonra, odağın bulunduğu multimedya dosyasını oynatmaya başlayacağız.  
* Duraklat: Bununla, oynatılan multimedya dosyasını duraklatacağız.  
* Durdur: Bununla, oynatılmakta olan multimedya dosyasının oynatılmasını durduracağız.  
* Geçen /Toplam süre:Bu kombinasyonla, multimedya dosyasının geçen süresi ve multimedya dosyasının toplam süresi hakkında bilgilendirileceğiz.  
* Sesi Azalt ve Sesi Arttır: Bununla dosyanın sesini azaltıp yükselteceğiz, bastığımızda yüzde kaç olduğu konusunda bilgi sahibi olacağız. Her ses değişikliği NVDA.ini dosyasına kaydedilecek ve bir sonraki sefer için ayarlanacaktır. Varsayılan olarak, ses %50'dir.  
* Geri sar ve İleri sar Bu kombinasyonlarla, oynatılan multimedya dosyasındaki süreyi azaltacak veya artıracağız. Varsayılan olarak ilk kez 5 saniye geri gidip 15 saniye ilerlemektir.  

Bu, Tercihler / Ayarlar / zPod'da yapılandırılabilir, NVDA seçenekler panelinde her eylem için istediğimiz süreyi 1 saniye ile 15 dakika arasında seçebiliriz.  

Bu seçenekler ayrıca NVDA.ini dosyasına kaydedilecek ve bir sonraki sefer için ayarlanacaktır.  

## zPod eklentisini ilk çalıştırmaya yönelik  belirtilen girdi hareketi için önemlli not:

Her ihtimale karşı, eklentiyi başlatmak için hiçbir zaman Control + c yapmanız gerekmediğini söylüyorum, bu eklenti tarafından dahili olarak yapılır, "ZPod'u Çalıştır" adlı giriş hareketinde atadığımız kombinasyonu kullanmanız yeterlidir.  

Eklentiyi başlatmak için kontrol tuşunu veya tuşların kombinasyonundaki sembolleri kullanmayın, çünkü fiziksel hareket gönderdiğimiz sanal olanla karıştırıldığından hata verecektir, örneğin bir kontrol + alt + Aslında başlamak için, eklentinin dahili olarak yaptığı ile iç içe geçtiği için iki kontrole dönüştürülür, yani, bir multimedya dosyasının üstündeyken, yaptığı şey, dosyanın bir anahtar kombinasyonunu simüle etmesidir. tam olarak Ctrl + C, bu, dosyayı panoya kopyalar ve oradan daha sonra zPot tarafından yürütülmek üzere dosya yolu elde edilir.  

Diğer tuş kombinasyonlarında önemli değil, ancak eklentiyi başlatmak için önemlidir.  

Bu eklentinin zaten yapıldığını ve bu nedenle bakımı için gerekenden daha fazla geliştirmeye sahip olmayacağını ve NVDA'nın gelecekteki sürümleriyle çalıştığını unutmayın.  

## Desteklenen uzantılar:  

ac3, a52, eac3, mlp, dts, dts-hd, dtshd, true-hd, thd, truehd, thd+ac3, tta, pcm, wav, aiff, aif, aifc, amr, awb, au, snd, lpcm, yuv, y4m, ape, wv, shn, m2ts, m2t, mts, mtv, ts, tsv, tsa, tts, trp, adts, adt, mpa, m1a, m2a, mp1, mp2, mp3, mpeg, mpg, mpe, mpeg2, m1v, m2v, mp2v, mpv, mpv2, mod, tod, vob, vro, evob, evo, mpeg4, m4v, mp4, mp4v, mpg4, m4a, aac, h264, avc, x264, 264, hevc, h265, x265, 265, flac, oga, ogg, opus, spx, ogv, ogm, ogx, mkv, mk3d, mka, webm, weba, avi, vfw, divx, 3iv, xvid, nut, flic, fli, flc, nsv, gxf, mxf, wma, wm, wmv, asf, dvr-ms, dvr, wtv, dv, hdv, flv, f4v, f4a, qt, mov, hdmov, rm, rmvb, ra, ram, 3ga, 3ga2, 3gpp, 3gp, 3gp2, 3g2, ay, gbs, gym, hes, kss, nsf, nsfe, sap, spc, vgm, vgz, m3u, m3u8, pls, cue  

## Teşekkür ve çevirmenler

* Reinier Ginnari: Bana ihtiyacınızdan bahsettiğiniz ve bana fikir verdiğiniz için. Ayrıca bana eklentinin adını verdiğiniz, eklenti testiniz ve eklentinin ne olduğu konusunda geri bildiriminiz için.  
* Fransızca: Rémy Ruiz  
* Portekizce: Angelo Abrantes  
* Türkçe: Umut KORKMAZ  

# Sürüm Geçmişi:  

## Sürüm 0.1.5.  

* Fransızca ve Portekizce dili eklendi (Portekiz / Brezilya).  

## Sürüm 0.1.  

* İlk sürüm.