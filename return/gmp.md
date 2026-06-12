---
title: Gimpo Airport (GMP)
parent: Return to the airport
nav_order: 3
permalink: /return/gmp/
---

# Return to Gimpo Airport (GMP)

[Gimpo International Airport (GMP)](https://www.airport.co.kr/gimpoeng/index.do) is located in the west of Seoul. It serves domestic flights (notably to Jeju) and short-haul international flights such as Tokyo Haneda, Osaka, Shanghai Hongqiao, Beijing, and Taipei Songshan. From Daejeon, the standard way is to take the KTX train to Seoul Station first.

{% capture allcontent %}

<h2 id="method1"><span class="btn">Method 1</span> KTX to Seoul Station + AREX all-stop train</h2>

<h3 id="method1-1">Step 1 @ IBS — Get to Daejeon Station</h3>

{% include taxi_phrase.html
   english="Daejeon Station"
   korean="대전역으로 가 주세요."
   fare="KRW 12,000–15,000"
   time="25 min" %}

<h3 id="method1-2">Step 2 @ Daejeon Station — KTX to Seoul Station</h3>

Take the KTX train from Daejeon Station to Seoul Station. It takes about 1 hour and trains run frequently. Tickets can be purchased at ticketing counters, at machines, or online at
- [Korail Website (English)](https://www.letskorail.com/english)
- [Mobile Korail Website (English)](https://m.letskorail.com/english)

<h3 id="method1-3">Step 3 @ Seoul Station — AREX all-stop train to the Gimpo Airport</h3>

At Seoul Station, transfer to the all-stop [AREX (Airport Railroad)](https://www.arex.or.kr/main.do) train toward the Incheon Airport and get off at the Gimpo Airport station. It takes about 22 minutes, costs KRW 1,600, and trains leave roughly every 7 minutes. Since the platform is deep underground, allow an extra 10 minutes at both Seoul Station and the Gimpo Airport station.

{: .warning}
The AREX **Express** train does NOT stop at the Gimpo Airport — take the **all-stop** train.

{: .note}
We do not recommend taking a taxi from Seoul Station to the Gimpo Airport — it is far more expensive than the AREX and can be slower in traffic.

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
var map = L.map('map').setView([36.376419, 127.385482], 7);
L.tileLayer('https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
L.control.scale().addTo(map);
var ibs = [36.376419, 127.385482];
var daejeonstn = [36.33209, 127.4340];
var seoulstn = [37.55413, 126.9714];
var gmp = [37.56535, 126.8011];
L.marker(ibs).addTo(map).bindPopup('<b><a href="https://kko.to/5AYThThWnr" target="maps">IBS Discrete Mathematics Group (IBS 이산수학그룹)</a></b>');
L.marker(daejeonstn, {icon: greenIcon}).addTo(map).bindPopup('<b><a href="https://kko.kakao.com/q2xzI4nqiG" target="maps">Daejeon Station (대전역)</a></b>');
L.marker(seoulstn, {icon: greenIcon}).addTo(map).bindPopup('<b>Seoul Station (서울역)</b>');
L.marker(gmp, {icon: redIcon}).addTo(map).bindPopup('<b>Gimpo International Airport (김포공항)</b>');
L.polyline([ibs, daejeonstn, seoulstn, gmp], {color: 'red'}).addTo(map);
var bounds = new L.latLngBounds([ibs, daejeonstn, seoulstn, gmp]);
map.fitBounds(bounds);
</script>

{{ allcontent }}

<a href="/localinfo/" class="btn btn-green">Local Information</a>
