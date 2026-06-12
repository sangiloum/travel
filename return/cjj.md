---
title: Cheongju Airport (CJJ)
parent: Return to the airport
nav_order: 2
permalink: /return/cjj/
---
{% assign s = site.data.schedules["yuseong-cjj"] %}

# Return to Cheongju Airport (CJJ)

[Cheongju Airport](https://www.airport.co.kr/cheongjueng/index.do) is the closest airport to Daejeon, about 51 km away from IBS. You can reach it by the airport bus from Yuseong, by a local train from Daejeon Station, or directly by taxi.

{% capture allcontent %}

<h2 id="method1"><span class="btn">Method 1</span> Airport bus from Yuseong Complex Terminal</h2>

<h3 id="method1-1">Step 1 @ IBS — Get to Yuseong Complex Terminal</h3>

The Yuseong Complex Terminal (유성복합터미널) is about 5 km from IBS.

{% include taxi_phrase.html
   english="Yuseong Complex Terminal"
   korean="유성복합터미널로 가 주세요."
   time="15 min" %}

<h3 id="method1-2">Step 2 @ Yuseong Complex Terminal — Bus to the Cheongju Airport</h3>

Take the bus from Yuseong Complex Terminal to Cheongju Airport (청주공항). The price is 6,500 KRW and the ride takes about 50 minutes. The first bus departs at {{ s.first_bus }} and the last bus departs at {{ s.last_bus }}.

> Current schedule (as of {{ s.updated }})
>
> {{ s.times | join: ", " }}
{: .note-title }

Times can change, so confirm at the Yuseong ticket office or kiosk on the day you depart.

<h2 id="method2"><span class="btn">Method 2</span> Local train from Daejeon Station</h2>

There is a train stop at the Cheongju Airport. You can take a local train from Daejeon Station to Cheongju Airport. It takes about 1 hour. The airport train stop is a short walking distance to the airport terminal.

<h3 id="method2-1">Step 1 @ IBS — Get to Daejeon Station</h3>

{% include taxi_phrase.html
   english="Daejeon Station"
   korean="대전역으로 가 주세요."
   time="25 min" %}

<h3 id="method2-2">Step 2 @ Daejeon Station — Train to the Cheongju Airport</h3>

#### Direct train timetable (Daejeon → Cheongju Airport)
- Mugunghwa trains — fare KRW 3,900 (standard seat).
- ITX trains - fare KRW 5,900.
- *Source: Korail mobile booking screen, March 2026.*

| Train | Departure (Daejeon) | Arrival (Cheongju Airport) | Travel time |
| --- | --- | --- | --- |
| 1701 | 06:06 | 07:01 | 55 min |
| 1703 | 06:50 | 07:47 | 57 min |
| 4301 | 07:54 | 08:52 | 58 min |
| 1705 | 08:46 | 09:39 | 53 min |
| 1701 ITX | 10:05 | 10:55 | 50 min |
| 1757 | 12:22 | 13:19 | 53 min |
| 1759 | 14:43 | 15:34 | 54 min |
| 1761 | 17:43 | 18:37 | 54 min |
| 1763 | 18:45 | 19:40 | 55 min |
| 4303 | 20:11 | 21:10 | 59 min |
| 1765 | 21:11 | 22:05 | 54 min |

Times may change, so confirm on the day of departure through Korail or the station kiosk.

Tickets for trains can be purchased by tellers at ticketing counters, by machine, or online at
- [Korail Website (English)](https://www.letskorail.com/english)
- [Mobile Korail Website (English)](https://m.letskorail.com/english)

As of 2023, it is possible to buy tickets online at above website by using foreign credit cards.
For visitors from China, it is also possible to buy the train ticket on [WeChat](https://www.minipaycn.com/minipay/wechat.do) or [AliPay](https://www.minipaycn.com/minipay/alipay.do).

<h2 id="method3"><span class="btn">Method 3</span> Taxi directly to the airport</h2>

<h3 id="method3-1">Step 1 @ IBS — Taxi to the Cheongju Airport</h3>

If you have heavy luggage or an early flight, a taxi straight to the airport is the simplest option. The ride takes about 50 minutes.

{% include taxi_phrase.html
   english="Cheongju International Airport"
   korean="청주국제공항으로 가 주세요."
   time="50 min" %}

You can also call a taxi with the Kakao T or k.ride apps — see the [Local Information](/localinfo/) page.

{% endcapture %}
{% include toc.html html=allcontent h_max=3 %}

<div id="map"></div>
<script language="javascript">
var greenIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});
var redIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});
var map = L.map('map').setView([36.376419, 127.385482], 9);
L.tileLayer('https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
L.control.scale().addTo(map);
var ibs = [36.376419, 127.385482];
var yuseong = [36.35609, 127.3311];
var daejeonstn = [36.33209, 127.4340];
var cjj = [36.72261, 127.4965];
L.marker(ibs).addTo(map).bindPopup('<b><a href="https://kko.to/5AYThThWnr" target="maps">IBS Discrete Mathematics Group (IBS 이산수학그룹)</a></b>');
L.marker(yuseong, {icon: greenIcon}).addTo(map).bindPopup('<b>Yuseong Complex Terminal (유성복합터미널)</b>');
L.marker(daejeonstn, {icon: greenIcon}).addTo(map).bindPopup('<b><a href="https://kko.kakao.com/q2xzI4nqiG" target="maps">Daejeon Station (대전역)</a></b>');
L.marker(cjj, {icon: redIcon}).addTo(map).bindPopup('<b>Cheongju International Airport (청주공항)</b>');
L.polyline([ibs, yuseong, cjj], {color: 'red'}).addTo(map);
L.polyline([ibs, daejeonstn, cjj], {color: 'blue'}).addTo(map);
L.polyline([ibs, cjj], {color: 'green'}).addTo(map);
var bounds = new L.latLngBounds([ibs, yuseong, daejeonstn, cjj]);
map.fitBounds(bounds);
</script>

{{ allcontent }}

<a href="/localinfo/" class="btn btn-green">Local Information</a>
