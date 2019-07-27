---
author: "Mehmet Köse"
date: 2019-04-11
title: React Projelerinde Otomatik Dökümantasyon Üretmek
featuredImg: ""
tags: 
  - react
  - doc
---

Gelin size bu aralar uğraştığım bir şeyden bahsedeyim. Dökümantasyon. Evet, aslında biraz sıkıcı bir konu olabilir, ama gerçekten yazdığınız componentlar tricky şeyler içeriyorsa, bir zaman sonra geri gelip anlamaya çalıştığınızda zorluklarla karşılaşacağınız neredeyse kesin. 

Neyse döküman önemli, ama nasıl tutsak. Business tarafı sizden döküman istiyor ve bunu 3. parti bir uygulamada tutmak istiyorsa? Kod sürekli değişiyor muhterem. Sürekli gidip bir yerdeki dökümanı güncelliyor olmak zor. 

Velhasılı aynı durum için ben dökümanı reponun içine koymaya karar verdim. Format markdown, çünkü basit. 

Birkaç sorgudan sonra şu kütüphaneye ulaşıyorsunuz: [react-doc-generator](https://github.com/marborkowski/react-doc-generator).
Componentların tepesine, belli formatta yorum satırları ekleyip nasıl çalıştığını açıklıyorsunuz. Prop'ları açıklıyor, default parametrelerini belirliyorsunuz. Derlemek için package.json içine de npm script'i yazdınız mı, mis. Mis gibi bir dökümantasyonunuz oldu. 

Tabi ben bununla yetinmedim. Componentları açıklayan markdown dosyasının yanına kendim proje hakkında başka markdown dosyaları da ekledim. Pandoc kullanarak hepsini tek bir PDF, Epub dosyası haline getirdiğim bir sürece başladım. 

Artık yeni versiyon çıkarken terminalden

```
yarn docs
```
yazmam ile dağıtıma hazır bir döküman elde etmiş oluyorum. 
