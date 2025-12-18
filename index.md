---
nav_order: 1
title: Travel Instructions to IBS
---
# Travel Instructions to the IBS, Daejeon, Korea

## Notice: [K-ETA (Korea Electronic Travel Authorization) Temporary Exemption](https://www.k-eta.go.kr/portal/board/viewboarddetail.do?bbsSn=258312)
Normally, citizens of some countries do not need to get a visa to visit Korea, but they need to get the K-ETA (Korea Electronic Travel Authorization) online before flying to Korea. However, the Ministry of Justice of Korea has decided to temporarily exempt the K-ETA for citizens of 52 countries (including the US, Canada, Australia, and most European countries) until December 31, <b>2026</b>. Please check the [K-ETA website](https://www.k-eta.go.kr/portal/board/viewboarddetail.do?bbsSn=258312) for more information.
This extension of exemption was announced on December 11, 2024. 

According to an email from the government official, the K-ETA Temporary Exemption will be extended until the end of December 31, 2026.

Visitors without K-ETA are required to fill out the [e-Arrival card](https://www.e-arrivalcard.go.kr) on the website [www.e-arrivalcard.go.kr](https://www.e-arrivalcard.go.kr). This requires no fees and you can complete and submit it within 3 days before arrival in Korea.


## Where are you traveling from?

### Airports

#### Seoul/Incheon

[Incheon International Airport (ICN), Terminal 1](/icn/){: .btn .btn-blue .v-align-middle} or [Terminal 2](/icn2/){: .btn .btn-blue .v-align-middle}\
A major international airport of Korea. 200 km to Daejeon.

[Gimpo International Airport (김포공항)](/gmp/){: .btn .btn-blue .v-align-middle}\
Closer to the downtown Seoul. 178 km to IBS.

#### Cheongju (청주)

[Cheongju International Airport (청주공항)](/cjj/){: .btn .btn-blue .v-align-middle} \
Closest to Daejeon. 51 km to IBS.

#### Daegu

[Daegu International Airport (TAE) (대구공항)](/tae/){: .btn .btn-blue .v-align-middle} \
158 km to IBS.

### Cities

#### Seoul (서울)

[Seoul Station (서울역)](/seoul/){: .btn .btn-blue .v-align-middle} [Suseo Station (수서역)](/suseo/){: .btn .btn-blue .v-align-middle} 

#### Gyeonggi Province (경기도)

[Gwangmyeong Station (광명역)](/gwangmyeong/){: .btn .btn-blue .v-align-middle}
  
#### Daegu (대구)

[Dongdaegu Station (동대구역)](/dongdaegu/){: .btn .btn-blue .v-align-middle}

#### Busan (부산)

[Busan Station (부산역)](/busan/){: .btn .btn-blue .v-align-middle}

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
    var map = L.map('map').setView([36.376419,127.385482], 7);
    L.tileLayer('https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    L.control.scale().addTo(map);
    {% for dest in site.destinations %}
    {% if dest.lat and dest.long %}
        {% if dest.slug== "dimag" %}
        L.marker([{{ dest.lat }}, {{ dest.long }}],{icon:redIcon}).addTo(map)
        .bindPopup('<b>{{ dest.title }}</b>')
        .openPopup();
        {%else%}
        L.marker([{{ dest.lat }}, {{ dest.long }}]).addTo(map)
        .bindPopup('<b>{{ dest.title }}</b>');
        {%endif%}
    {% endif %}
    {% endfor %}
    {% for dest in site.origins %}
    {% if dest.lat and dest.long %}
    L.marker([{{ dest.lat }}, {{ dest.long }}],{icon:greenIcon}).addTo(map)
        .bindPopup('<b><a href="/{{dest.slug}}/">{{ dest.title }}</a></b>');
    {% endif %}
    {% endfor %}
</script>


