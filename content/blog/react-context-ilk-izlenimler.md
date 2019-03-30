---
author: "Mehmet Köse"
date: 2019-03-29
title: React Context ilk izlenimlerim
featuredImg: ""
tags: 
  - hex
  - frontend
---

Son birkaç senede kendimce geliştirdiğim React ve Preact uygulamalar ve Freelance olarak yaptığım appler  büyük boyutlara ulaşmadığı için state management konusunda external bir çözüm kullanma ihtiyacı hissetmemiş, [prop-drilling](https://kentcdodds.com/blog/prop-drilling/)'den şaşmamıştım. Şöyle bir bakayım diye okumaya başladığım Redux, Flux konularına da o an ihtiyacım olmadığı için devam etmedim. Velhasılı, araya askerlik de girdi, döndüğümde ortaya [Context](https://reactjs.org/docs/context.html) çıkmıştı. Yeni başladığım işte de madem böyle bir şey var deneyelim diyerek state management ihtiyacını *Context* ile çözmeye giriştim.

Aslında ilk yaptığım şey klasör yapısını şöyle düzenlemek oldu; ["components", "context", "pages"]

Kullanımı konusunda da [şu](https://github.com/joseferrer1090/example-context-api) [iki](https://github.com/academind/react-redux-vs-context) örneği inceleyip benimseyerek basit bir yapı oturttum. 

Context klasörü içinde iki dosya var; birinde React.createContext initialize ediyorum. Diğerinde de standart bir class based component oluşturup, tüm datayı yöneteceğim bu componenti *Context.Provider* ile sarıp export ediyorum. Geriye ihtiyacım olduğu yerde import edip *Context.Consumer* vasıtasıyla erişmek kalıyor. 

Şimdi bu yöntem çok mu doğrudur emin değilim. Zaman gösterecek. Redux'a benzer yapılar kurup bu şekilde kullananlar da gördüm. Bahsettiğim gibi, karmaşık bir state management kütüphanesi hiç kullanmadığım için makul bir kıyaslama da yapamıyorum. 

Bu haliyle bizim işimizi gayet çözüyor. Yalnız Context'i genel olarak Component Lifecycle methodları içinde değil de JSX tarafında kullanmak zorunda olduğum için aslında data ile alakalı methodları data componenti içinde yazdığımı farkettim. Şu an için minnoş bir geliştirme ortamı sunan bu çözüm ilerleyen zamanlarda zapt etmesi zor bir canavara dönüşür mü göreceğiz. 

Ha bu arada hooks'u inceledim ama o tarafın daha oturmadığını düşünüyorum. Onu biraz bekleyeceğim. Onun hakkında da başka bir yazıda bahsederiz. 