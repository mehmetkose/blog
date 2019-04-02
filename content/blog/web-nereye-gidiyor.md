---
author: "Mehmet Köse"
date: 2019-03-30
title: Web Nereye Gidiyor?
featuredImg: ""
tags: 
  - web
  - mobile
  - desktop
  - electron
  - deskgap
  - electrino
  - quark
---

Antalya'daki meetuplarımızda panpalarla laflarken son 5-6 senedir platformlar arası kıyaslamalar yaptığımız durumlarda yatırımı web'e yapmak gerektiği yönünde tartışmalara girdiğimi hatırlıyorum. 

Nitekim geldiğimiz nokta şu; henüz yolun başında olsa da [WebAssembly](https://webassembly.org/) denen şeyle büyük ve zorlu hesaplamaları derleyip tarayıcı içinde binary dosya çalıştırmak mümkün hale geldi. 

[PWA](https://developers.google.com/web/progressive-web-apps/) yaygınlaştı. Windows 10'a kurulabilir hale geldi. Eğer manifest dosyası düzgün yapılandırılmışsa PWA'yı doğrudan mobil cihazların menülerine bir uygulamaymışcasına eklemek mümkün.

Bu sene başında, PWA'ların doğrudan Play Store'da yayınlanabilir olacağı yönünde söylentiler arttı, doğrulandı, [şöyle bir yazı var](https://medium.com/@firt/google-play-store-now-open-for-progressive-web-apps-ec6f3c6ff3cc).

Electron ile web uygulamalarını paketleyip desktop app yapmak popüler oldu ama pek hoş bir deneyim olduğunu söyleyemem. 3-4 Electron temelli app çalıştırdığımızda bilgisayarlarımız alev üflemeye başlıyor. Ama yapılabiliyor olduğunu bilmek keyifli. 

Bu kısmın ne zaman olduğu yönünde bilgim yok, ama Desktop OS'lar da WebView destekliyor hale gelmiş. Yani araya bir chrome tarayıcı koymadan doğrudan işletim sistemininin desteğini kullanarak uygulamalar yapmak mümkün oluyor. Şu an bu kısım ile alakalı projelerin linklerini ekleyeyim, daha teknik bir spesifikasyona doğru kelimeleri bulamadığım için ulaşamıyorum nedense. [Deskgap](https://deskgap.com/), [Electrino](https://github.com/pojala/electrino), [Quark](https://github.com/jscherer92/Quark), [Webview Go](https://github.com/zserge/webview). Bunlardan *Deskgap* takip etmeye değer bir proje. Bundle içerisine node.js de gömdüğü için web uygulamanız file i/o işleri de yapabilir hale geliyor. Ve ortalama paket boyutu da 8-10 mb civarı oluyor. Performans da cabası. 

Şimdi düşününce, nereye gittiğimizi görüyorsunuz galiba değil mi? Başka platformlar ve çözümler sürekli teknoloji evrimi içinde ilerliyor olacak tabiki ama gelecek web'in etrafında şekillenecek gibi geliyor bana bu şekilde bakınca. Belki PC'ler ortadan kalkar, hepimiz gözlüğe ve saate döneriz ama hep web üzerinden bir şeyler gerçekleşecek gibi geliyor bana.

Google'ın vizyonu tam olarak bu yönde. Ve açıkcası çok iyi iş çıkarıyorlar. Chromebook'a ve opensource ettikleri veya geliştirdikleri ticari işlere bakınca vizyonu anlamak çok basit. 

İzlemesi, öğrenmesi uygulaması keyifli bir dönemdeyiz. 