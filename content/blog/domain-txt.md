---
author: "Mehmet Köse"
date: 2019-04-01
title: "Domain TXT Kaydı Sorgulamak"
featuredImg: ""
tags: 
  - domain
  - dns
  - txt
---

Tr domainlere amazon dahil bir çok cloud platformundan doğru düzgün dns server desteği bulamadığım, Cloudns'in de destek vermediği, bunun gibi bir çoğunu denediğim durumlarda hayli kullandığım ufak bir tool oldu *dig*.

NS server değiştirip durduğum günlerde Google'ın istediği TXT kaydını sürekli kontrol etmek için şöyle yapıyordum;

```
dig mehmetkose.com.tr TXT
```

bu arada firebase ve cli ile blog deploy etmek harika!