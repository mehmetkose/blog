---
author: "Mehmet Köse"
date: 2019-03-26
title: Git ile commitlenmemiş değişiklikleri farklı branch'e almak
featuredImg: ""
tags: 
  - git
  - branch
---



Gaza geldiniz, yazdınız, yazdınız, yazdınız...

Hassiktir o da ne? Deneme maksadıyla girdiğiniz kodda başarılı bir şey yaptınız veya yeni bir şeye evrildi. Ayrı bir branch açıp bu konuyu orada devam ettirmek istiyorsunuz. Ama kodlar değişti bir kere. Bir yandan sürmesi gereken bir development var belki de, şu an bu yeni kodları tamamlamak için vakit ayıramayacağız. Zamanı geriye alıp yeni bir branch açamayacağımıza göre?

**git stash** 
diyorsunuz önce. Bu, değişiklikleri ayrı bir yere alıp, master'ı en son commit'e götürecek.

**git branch yeni\_bir\_sey** 
diyerek yeni branch'i açıyoruz.

**git checkout yeni\_bir\_sey** 
açtığımız branch'e geçiyoruz, master'da olduğumuzu var sayıyorum.

**git stash pop** 
git reyiz'e değişiklikleri yeni branch'e yapıştırmasını söylüyoruz.

**git commit -a -m "Ya işte şöyle oldu böyle oldu"**
commit'imizi de yaptık.

**git checkout master** 
master'a geçtik.

Şimdi burada temiz master branch'de yeni bişeyler yapmak istiyorsak devam ediyoruz. Farklı branch açabiliriz, bugfix yapabiliriz vs.

Ara ara bizim branch'de çalışmaya devam ettik günlerce. Vakti geldiğinde yapacağımız şey şu;

**git merge yeni\_bir\_sey** 
hoop, değişiklikler master'a geldi. Akıllı adamsın conflict yapmamışsındır herhalde. Yaptıysan da çözersin zeki adamsın sen. Hadi koçum.