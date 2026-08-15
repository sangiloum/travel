---
title: Incheon Airport (ICN)
parent: Return to the airport
nav_order: 1
permalink: /return/icn/
---
{% assign s1 = site.data.schedules["doryong-icn"] %}
{% assign s2 = site.data.schedules["govcomplex-icn"] %}

# Return to Incheon Airport (ICN)

The **most recommended way to reach the Incheon Airport from Daejeon is to take the airport bus**.
There are frequent buses from around 3 a.m. so that you can catch an early morning flight.
It is strongly recommended to buy the ticket early.
It takes up to 3 hours to reach Terminal 1
and up to 3 hours 18 minutes to reach Terminal 2.
**Book the bus in advance. The tickets may be sold out.**

{: .warning}
Make sure to board the correct bus. Not only the airport buses but also buses to Seoul and other cities stop at the same bus stops.

{% capture allcontent %}

<h2 id="method1"><span class="btn">Method 1</span> Airport bus from the Doryong Inter-City Bus Stop</h2>

The Doryong Inter-City Bus Stop (도룡시외버스정류장) is the closest airport bus stop to IBS — about 1.5 km, so it is walkable, and it is easy to find the right boarding point. This is the stop we recommend. Note that it is unmanned and has only automated ticket machines; if you prefer a staffed ticket office, use the Government Complex stop (Method 2).

<h3 id="method1-1">Step 1 @ IBS — Get to the Doryong Inter-City Bus Stop</h3>

The stop is about a 20-minute walk from IBS, or a few minutes by taxi. Here is the [exact location of the bus stop on Kakao Map](https://kko.kakao.com/m17R13IvP0)
or [Google Map](https://maps.app.goo.gl/emej8ELmnfrsHMQw8?g_st=aw).

On Uber, you can search "Inter-city bus" and pick the result whose address is "634, 대덕대로 유성구 대전광역시" — that is this stop. The ride from the Expo Park area takes only a few minutes and costs about KRW 5,000–6,500.

|![Searching for "Inter-city bus" on Uber](/assets/images/uber-search.png)|![Uber fare estimate to the Doryong Inter-City Bus Stop](/assets/images/uber-ride.png)|
|:--:|:--:|
|*Search "Inter-city bus" and choose the one at 634, 대덕대로*|*From Lotte City Hotel to Inter-city Bus Stop*|

{% include taxi_phrase.html
   english="Doryong Inter-City Bus Stop (for the Incheon Airport bus)"
   korean="인천공항 가는 공항버스를 타려고 합니다. 도룡시외버스정류장으로 가 주세요."
   time="5 min"
   note="The first sentence tells the driver that you are catching the airport bus to the Incheon Airport. The stop is known as the Doryong Inter-City Bus Stop." %}

<h3 id="method1-2">Step 2 @ Doryong Inter-City Bus Stop — Buy the ticket and board</h3>


The easiest method is to ask people in Korea: they can buy your bus ticket on the app "TMoney Go" and pay by a Korean credit card. Then there will be a ticket with a QR code. You should get the screenshot of your ticket having the QR code. When you board the bus, you show the QR code on your phone to the scanner on the bus.

There is no ticket office here; buy your ticket at the machine. <del>Previously it was possible to reserve it [online at https://txbuse.t-money.co.kr](https://txbuse.t-money.co.kr)
and print it at the machine before you leave. However, it is reported that this is no longer possible with international credit cards. You will likely want the following:</del>
- <del>Departure: Daejeondoryong</del>
- <del>Destination: IncheonAirportT1 or IncheonAirportT2.</del>


<del>If you want to use foreign credit cards, you should choose "GLOBAL CARD" in the list of credit cards. For "Card Password", it only needs the first 2 digits of your credit card password, but probably you can type anything, because it doesn't matter much.</del>

<del>For "Resident Registration Number (front 6 digits)", you simply need to type your birthday in YYMMDD format. For the Cellular Phone number, if you don't have the Korean mobile phone number, put any number, for instance the phone number of your host at IBS. That is for the identification.</del>

<del>After booking the ticket, you'll need to pick up the ticket at the bus stop by using the machine. It'll ask you to identify yourself by using the credit card number that was used to pay for your bus ticket or the phone number.</del>

|![Doryong Bus Stop](/assets/images/doryong.jpg)|![Ticket Machines at the Doryong Inter-City Bus Stop](/assets/images/doryong-ticket.jpg)|
|:--:|:--:|
|*Doryong Inter-City Bus Stop*|*Ticket Machines at the Doryong Inter-City Bus Stop*|

The first bus departs at {{ s1.first_bus }} and the last bus departs at {{ s1.last_bus }}.
The same departures serve both Terminal 1 and Terminal 2; Terminal 2 is the next airport stop after Terminal 1.

#### Bus Schedule to Incheon Airport (Terminals 1 and 2, as of {{ s1.updated }})

| Departure | Class | Fare for an Adult (KRW) |
| :--: | :--: | :--: |
{% for row in s1.rows %}| {{ row.time }} | {{ row.class }} | {{ row.fare }} |
{% endfor %}

<h2 id="method2"><span class="btn">Method 2</span> Airport bus from the Government Complex Bus Stop</h2>

The Government Complex (정부청사) stop is the one with a staffed ticket office. If you prefer to buy or pick up your ticket from a person rather than a machine, use this stop.

<h3 id="method2-1">Step 1 @ IBS — Get to the Government Complex Bus Stop</h3>

The bus stop is 2.3 km away from IBS — about 10 minutes by taxi, or a 30-minute walk. Here is the [exact location of the bus stop on Kakao Map](https://kko.kakao.com/y4Eea2yrof).

{: .warning}
There are many bus stops around the Government Complex — city bus stops and several intercity bus stops — and first-time visitors often end up at the wrong one. The airport bus leaves from the intercity bus stop with the ticket office, on the street on the west side of the Government Complex. Check the [exact location on Kakao Map](https://kko.kakao.com/y4Eea2yrof) before you go. When you take a taxi, tell the driver that you are going there to catch the airport bus to the Incheon Airport — the phrase below includes it.

{% include taxi_phrase.html
   english="Government Complex Bus Stop (for the Incheon Airport bus)"
   korean="인천공항 가는 공항버스를 타려고 합니다. 정부청사 시외버스 정류장으로 가 주세요."
   time="10 min"
   note="The first sentence tells the driver that you are catching the airport bus to the Incheon Airport, so they can drop you at the correct stop among the several stops around the Government Complex." %}

<h3 id="method2-2">Step 2 @ Government Complex Bus Stop — Buy the ticket and board</h3>


The easiest method is to ask people in Korea: they can buy your bus ticket on the app "TMoney Go" and pay by a Korean credit card. Then there will be a ticket with a QR code. You should get the screenshot of your ticket having the QR code. When you board the bus, you show the QR code on your phone to the scanner on the bus.

You can buy the ticket in person at the ticket office (open 6:00–21:15). 
<del>(Previously it was possible to reserve it [online at https://txbuse.t-money.co.kr](https://txbuse.t-money.co.kr) (choose **Daejeon Gov Complex(airport route)** as the departure) and print it at the machine, as described in Method 1. However it has been reported that it no longer accepts international credit cards.)</del>

|![Government Complex Bus Stop](/assets/images/dunsan.jpg)|
|:--:|
|*Government Complex Bus Stop*|

|![Ticket Machine at the Government Complex Bus Stop](/assets/images/dunsan-ticket.jpg)|![Ticket Office at the Government Complex Bus Stop](/assets/images/dunsan-ticket-office.jpg)|
|:--:|:--:|
|*Ticket Machine for the Incheon Airport*|*Ticket Office (6am–9:15pm)*|

The first bus departs at {{ s2.first_bus }} and the last bus departs at {{ s2.last_bus }}.
The same departures serve both Terminal 1 and Terminal 2; Terminal 2 is the next airport stop after Terminal 1.

#### Bus Schedule to Incheon Airport (Terminals 1 and 2, as of {{ s2.updated }})

| Departure | Class | Fare for an Adult (KRW) |
| :--: | :--: | :--: |
{% for row in s2.rows %}| {{ row.time }} | {{ row.class }} | {{ row.fare }} |
{% endfor %}

<h2 id="method3"><span class="btn">Method 3</span> KTX train via Seoul Station + AREX</h2>

If the bus schedule does not fit your flight, you can take the KTX train to Seoul Station and transfer to the AREX airport railroad.

<h3 id="method3-1">Step 1 @ IBS — Get to Daejeon Station</h3>

{% include taxi_phrase.html
   english="Daejeon Station"
   korean="대전역으로 가 주세요."
   time="25 min" %}

<h3 id="method3-2">Step 2 @ Daejeon Station — KTX to Seoul Station</h3>

Take the KTX train from Daejeon Station to Seoul Station. It takes about 1 hour and trains run frequently. Tickets can be purchased at ticketing counters, at machines, or online at
- [Korail Website (English)](https://www.letskorail.com/english)
- [Mobile Korail Website (English)](https://m.letskorail.com/english)

<h3 id="method3-3">Step 3 @ Seoul Station — AREX to the Incheon Airport</h3>

At Seoul Station, transfer to the [AREX (Airport Railroad Express)](https://www.arex.or.kr/main.do). The Express train takes about 43 minutes to Terminal 1 (about 51 minutes to Terminal 2); the all-stop train takes about 59 minutes to Terminal 1. Since the AREX platform is deep underground, allow an extra 10 minutes for the transfer.

<h2 id="method4"><span class="btn">Method 4</span> KTX train via Gwangmyeong Station + bus</h2>

This can be faster than going through Seoul Station, because Gwangmyeong Station is closer to the Incheon Airport.

<h3 id="method4-1">Step 1 @ IBS — Get to Daejeon Station</h3>

Take a taxi to Daejeon Station as in Method 3.

<h3 id="method4-2">Step 2 @ Daejeon Station — KTX to Gwangmyeong Station</h3>

Take the KTX train from Daejeon Station to Gwangmyeong Station. It takes about 35 minutes.

<h3 id="method4-3">Step 3 @ Gwangmyeong Station — Bus to the Incheon Airport</h3>

From Gwangmyeong Station, take the airport bus **6770** or **6014** (KRW 16,000 for an adult) to the Incheon Airport.

- **Bus 6770** goes directly to the airport without intermediate stops and runs every 20–30 minutes from about 05:00 to 20:30. The ride takes about 50–75 minutes. See the [KTX–airport bus guide on Korail](https://www.korail.com/ticket/train/stationGuide/terminal/ktxbus).
- **Bus 6014** stops at Gimpo Airport on the way and runs less frequently (roughly every 40–80 minutes from about 04:25 to 20:00) — check the [Bus#6014 timetable](https://airportlimousine.co.kr/sub/sub01.php?cat_no=20).

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
var gov = [36.3615, 127.3797];
var doryong = [36.389, 127.3775];
var daejeonstn = [36.33209, 127.4340];
var seoulstn = [37.55413, 126.9714];
var gwangmyeong = [37.41683, 126.8850];
var icn1 = [37.44966, 126.4514];
var icn2 = [37.46832, 126.4340];
L.marker(ibs).addTo(map).bindPopup('<b><a href="https://kko.to/5AYThThWnr" target="maps">IBS Discrete Mathematics Group (IBS 이산수학그룹)</a></b>');
L.marker(gov, {icon: greenIcon}).addTo(map).bindPopup('<b><a href="https://kko.kakao.com/y4Eea2yrof" target="maps">Government Complex Bus Stop (정부청사)</a></b>');
L.marker(doryong, {icon: greenIcon}).addTo(map).bindPopup('<b><a href="https://kko.kakao.com/m17R13IvP0" target="maps">Doryong Bus Stop (대전도룡동고속시외버스정류장)</a></b>');
L.marker(daejeonstn, {icon: greenIcon}).addTo(map).bindPopup('<b><a href="https://kko.kakao.com/q2xzI4nqiG" target="maps">Daejeon Station (대전역)</a></b>');
L.marker(seoulstn, {icon: greenIcon}).addTo(map).bindPopup('<b>Seoul Station (서울역)</b>');
L.marker(gwangmyeong, {icon: greenIcon}).addTo(map).bindPopup('<b>Gwangmyeong Station (광명역)</b>');
L.marker(icn1, {icon: redIcon}).addTo(map).bindPopup('<b>Incheon Airport Terminal 1</b>');
L.marker(icn2, {icon: redIcon}).addTo(map).bindPopup('<b>Incheon Airport Terminal 2</b>');
L.polyline([ibs, doryong, icn1], {color: 'red'}).addTo(map);
L.polyline([ibs, gov, icn1], {color: 'blue'}).addTo(map);
L.polyline([ibs, daejeonstn, seoulstn, icn1], {color: 'green'}).addTo(map);
L.polyline([ibs, daejeonstn, gwangmyeong, icn1], {color: 'black'}).addTo(map);
var bounds = new L.latLngBounds([ibs, gov, doryong, daejeonstn, seoulstn, gwangmyeong, icn1, icn2]);
map.fitBounds(bounds);
</script>

{{ allcontent }}

<a href="/localinfo/" class="btn btn-green">Local Information</a>
