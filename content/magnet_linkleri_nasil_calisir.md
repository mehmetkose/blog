---
author: "Mehmet Köse"
date: 2019-03-25
title: Magnet Linkleri Nasıl Çalışır?
featuredImg: ""
tags: 
  - magnet
  - bittorrent
---


Ulan hadi ben bu öğrendiklerimi unutmayayım diye yazıyorum bu yazıyı..

Sen niye o kadar kaynak varken gelip bunu okuyorsun?

Ha doğru ya, dallamanın biri köyünden çıkıp gelip kaynak siteyi engellemiştir belki de.

Ya şimdi bu **magnet** linkleri sihir gibi bişey.

Torrent dosyasını yine bittorrent'le indirmeni sağlıyor. Oha tabi yaa! nasıl düşünemedik..

Şimdi şu link'e bak ama ahengine kapılma ->

_magnet:?xt=urn:btih:dc2e7bf4a273dc4b25ae96e833fd50be2b00e953&dn=The+Humble+Indie+Bundle+6+for+Windows+%2B+Soundtracks&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80_

**magnet: —** Şimdi bu magnet reyizin URI şeması. Yani akıllı olan tarayıcı şunu anlar, bu link bir magnet linkidir. Ona göre bir torrent programı ile açsam iyi olur.

**xt=urn:btih:dc2e7bf4a273dc4b25ae96e833fd50be2b00e953 —** En önemli kısım bu. bu arkadaş torrent dosyasının infohash hali. biricik adı. Aslında dosyanın adını bir çok kriptografik yöntemle hashleyip yaymak mümkün, ama infohash en çok kullanılanı.

**dn=The+Humble+Indie+Bundle+6+for+Windows+%2B+Soundtracks —** bu da dosya hakkında birazcık bilgi. peerlar görsün, hakkında bilgi sahibi olsun diye. Akıllı adam buradan ekmek çıkarır.

**tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80 —** bu da tracker url'inin encoded hali. peer'ları sorup soruşturmak için bu reyizlere danışıyoruz. UDP protokolü kullanıldığını görebiliyorsunuz mesela bakınca. WS biliyorum da UDP hiç bilmiyorum. Bir ara baksam iyi olur.

Görüldüğü gibi aslında mantık çok basit, elinde dosyanın biricik adı var. Etrafa soruşturuyorsunuz ya dosyayı verin ya da distributed hash table verin diye.