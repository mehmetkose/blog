---
author: "Mehmet Köse"
date: 2019-04-04
title: "Sayfa Assetlerinizi Html İçine Toparlayın : Node Inline"
featuredImg: ""
tags: 
  - node
  - web
  - performans
  - base64
  - gulp
---


# Neden?

Öncelikle amacımız ne ona bakalım, kütüphanenin amacı sayfa asset'lerini html içine gömerek tek dosyaya indirgimeye çalışmak.

Peki bizim amacımız ne olabilir? 

Performans olabilir mesela. Lighthouse'da test yapıyorsunuz ve gereksiz asset'lerin arayüzün çizilmesini engellediği yönünde hatalar alıyorsunuz. Muhtemelen statikleri inline gömmek sorununuzu çözecektir. Veya interneti crawl edip sayfaları yedekliyor olabilirsiniz. Assetler ile birleştirmek mantıklı bir fikir olabilirdi. Ya da, web sitenizi Electron ile desktop uygulaması olarak derlemek istiyor, ama assetleri taşıyarak, path'ler ile uğraşarak vakit kaybetmek istemiyorsunuz. Web sayfasının "dist" klasöründen alıp, inline derleyip Electron'a vermek mantıklı olabilirdi. 

Her ne amaçla olursa olsun, bunu kolayca yapabileceğiniz birkaç seçenek var. En kolayı [node-inline](https://github.com/fb55/node-inline) adlı bu node modülünü kullanmak. 
Diğer bir yol da [Gulp](https://gulpjs.com) gibi bir araç ile kendi task'lerinizi yazıp assetleri html içine gömmek. Tabi gulp kullanırsanız dünya kadar modül olduğu için çeşitli senaryolarla işi ilerletebilirsiniz. Örneğin fontları ve resimleri base64 olarak CSS içine, CSS'i ve JS'i de minify edip html içine gömebilirsiniz. Ve taskleri bir kere yazdıktan sonra arkaplanda çalışıp değişiklik oldukça sürekli aynı işi yapan bir robot sahibi olabilirsiniz.

Neyse biz şimdilik node-inline ile devam edelim.


```
mkdir site && cd site
```

Proje klasörünü yarttık ve içine girdik.

```
yarn init -y 
```

Projeyi initialize edelim

```
yarn add inline
```

Paketimizi ekleyelim.


```
yarn add inline
```

```
var Inline = require("inline"),
    minreq = require("minreq");

minreq.get("https://mehmetkose.com.tr/").pipe(
  new Inline("https://mehmetkose.com.tr/", {
    //default options:
    images: true, //inline images
    scripts: true, //inline scripts
    stylesheets: true //inline stylesheets
  }, function(err, data){
    if(err) throw err;
    require("fs").writeFileSync("index.html", data);
  }
));
```

Gördüğünüz gibi panpamız external url'leri indirerek çalışabiliyor. Harika! Isterseniz lokaldeki projeyi, isterseniz uzaktaki sayfayı indirin böylece.