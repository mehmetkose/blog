---
author: "Mehmet Köse"
date: 2019-04-12
title: "Web'de Img Etiketini Efektif Kullanmak"
featuredImg: ""
tags: 
  - web
  - resim
  - responsive
  - lazy
---

Yıllardır kullandığımız *img* etiketi süreç içinde oldukça *duyarlı* hale geldi. Logo gibi imaj dosyalarını responsive yapmak [yıllardır uygulanan](http://responsivelogos.co.uk/) bir şeydi. Kod seviyesinde düşünürsek standartların da günceli yakaladığını söyleyebiliriz.

Bu yazıda değinilen iki konu var aslında; resim performansı ve resim deneyimi.

Aşağıdaki koda bakacak olursanız, srcset attribute'ü ile cihaz genişliğine göre resim versiyonu girilebildiğini görebilirsiniz. Resimler pek dikkat etmediğimiz ama bizi büyük performans kaybına uğratan şeyler. Birkaç versiyonunu tutmak ve bu şekilde sunmakta fayda var. Ayrıca asıl *src* kısmına da küçük olan resmin girildiğini de görüyorsunuz. Sayfa yüklenme sürelerini arttıran bir unsur.

Diğer bir konu da *loading=lazy* attribute'ü. Bu tarayıcılara yeni yeni gelen bir konu. Önceside native olarak yapmanın imkanı yoktu.

Checklistlere ekleyin, performans, SEO, adına ne derseniz deyin.. Bakılacak kısımlardan biri de img etiketleri artık.


```
<img src="small.jpg"
     srcset="large.jpg 1024w, medium.jpg 640w, small.jpg 320w"
     sizes="(min-width: 36em) 33.3vw, 100vw"
     alt="A rad wolf" loading="lazy">
```
