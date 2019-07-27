---
author: "Mehmet Köse"
date: 2019-04-02
title: "Declarative ve Imperative Programlama Farkı"
featuredImg: ""
tags: 
  - paradigma
  - declerative
  - imperative
  - programlama
---

Programlama paradigmaları temel bir kodlama stilidir. Çok kullanılan 4 tane programlama paradigması var; object-oriented, imperative, declarative, fonksiyonel (declarative programlamanın bir alt kümesi olarak görülebilir).

## Declarative programlama

Ne yapılacağını içeren, nasıl yapılacağınının mantığını pek de içermeyen paradigmadır. CSS veya HTML'i düşünün. Bir şeyin blur olacağını ifade edersiniz browser blur yapar. O şeyin nasıl blurlaştırılacağı hakkındaki fizik mantığını kurgulamaya çalışmazsınız. Veya border atadığınızda, onun aslında bir piksellik bir çizgi olduğunu, çizginin aslında noktalardan meydana geldiğini filan açıklamaya çalışmazsınız. Ne yapılacağını söylersiniz, yapılır. Nays!

```
function createWidget(type, txt) {
  return new Element(type, txt);
}
```
Mesela burada fonksiyon bir widget yaratıp geri döndürmüş. Widget'ın nasıl yaratıldığı hakkında çok fazla bilgimiz yok. Belki gerek de yok. Widget istedik widget'ı aldık. Önemli olan bu değil mi? (I dunno).

## Imperative programlama

Bu da Declarative reyizin tam tersi, neyin nasıl olacağını, flow'u detaylıca yazdığınız programlama stili. Aynı örnekten gidelim;

```
function createWidget(options) {
  const element = document.createElement('div');
  element.style.backgroundColor = options.bgColor;
  element.style.width = options.width;
  element.style.height = options.height;
  element.textContent = options.txt;
  return element;
}
```

Gördüğünüz gibi kral burada, fonksiyonun adına yaraşır şekilde *widget*'ı *yaratmış* ve geri döndürmüş.

### Javascript Örneği

#### Declarative 

```
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((n) => {
  return n * 2;
});
console.log(doubled); // => [2,4,6,8,10]
```

#### Imperative 

```
const numbers = [1, 2, 3, 4, 5];
const doubled = [];
 
for (let i = 0; i < numbers.length; i += 1) {
  const newNumber = numbers[i] * 2;
  doubled.push(newNumber);
}
console.log(doubled); // => [2,4,6,8,10]
```


Bu vesileyle, ES6+ yeni gelen Javascript özelliklerinin Declarative ve Functional olduğunu söyleyebiliriz.

[Declarative_programming](https://en.wikipedia.org/wiki/Declarative_programming)