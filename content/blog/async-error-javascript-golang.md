---
author: "Mehmet Köse"
date: 2019-04-13
title: "Javascript'te Asenkron Hata Ayıklamak, Golang Tarzı!"
featuredImg: ""
tags: 
  - async
  - javascript
  - error
  - golang
---

Promise based şeyler yazarken then/catch kullanıyoruz evet ama ya async/await kullanırken hata oluşursa ne yapacağız? try/catch dışında (ki çok çirkin, asenkron programlama yaparken bazı dillerde kullanılmaması önerilir) var mı bir çözüm diye sorarsanız, şu kütüphaneye bakmak isteyebilirsiniz, [await-to-js](https://github.com/scopsy/await-to-js).

işleminizi bu arkadaşla kapsarsanız, sonucu size golang tarzında bildiriyor. yani *await* işleminizden iki sonuç dönüyor. Birisi, işlem başarılıysa istediğimiz sonuç, ikincisi ise işlemin sonucuna göre kontrol ettiğimiz *error* değişkeni. 

```
async function asyncFunctionWithThrow() {
  const [err, user] = await to(UserModel.findById(1));
  if (!user) throw new Error('User not found'); 
}
``` 

Biraz *Go* aşinalığı olanlar için güzel bir çözüm.
