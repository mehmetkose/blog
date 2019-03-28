---
author: "Mehmet Köse"
date: 2019-03-27
title: Jest create-react-app default setup dosyası
featuredImg: ""
tags: 
  - react
  - jest
  - test
---
Kullandığım bazı componentlar için test yazarken Jest ağlamaya başlayınca düştüm yollara çözüm aramaya başladım. 

Hatta hatayı da yazayım da google'da dolaşan panpalar da gelsin;

```
matchMedia not present, legacy browsers require a polyfill
```

tamam sorunun çözümü ile alakalı konulara internetten ulaşabilirsiniz ama ola ki yönlendirdikleri üzere Jest'i configure etmek üzere setupFile yaratmaya ve package.json'a eklemeye çalışırsanız bu sefer de react-scripts'in ağladığını göreceksiniz. 


```
"devDependencies": {
    ...
},
"jest": {
    "setupFiles": [
      "setupTests.js"
    ]
},
"browserslist": [
    ...
]
```

Neyse sözün özü, "src" içine setupTests.js dosyası yaratırsanız bu test başlamadan önce otomatik olarak bakılıp çalıştırılacak olan dosya. Sorunun çözümü ile alakalı kısımları oraya yazıyoruz. 

```
window.matchMedia =
  window.matchMedia ||
  function() {
    return {
      matches: false,
      addListener: function() {},
      removeListener: function() {}
    };
  };
```