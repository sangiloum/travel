---
nav_order: 3
title: Return to the airport
---
# Return to the airport

<div id="map2"></div>
<script language="javascript">
var map = L.map('map2').setView([36.37,127.3885], 13);
L.tileLayer('https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
L.control.scale().addTo(map);
function pm(label, lat, long, title,link) {
    var myIcon=L.divIcon({className:"mi", html:label });
    L.marker([lat, long],{icon:myIcon}).addTo(map)
    .bindPopup('<b><a href="'+link+'" target=_new>'+title+'</a></b>');
}
pm(1, 36.376419, 127.385482, 'IBS Discrete Mathematics Group (IBS 이산수학그룹)', 'https://kko.to/5AYThThWnr');
pm(2, 36.3615, 127.3797, 'Daejeon Government Complex (대전청사) Bus Stop Departure Point', 'https://kko.kakao.com/y4Eea2yrof');
pm(3, 36.389, 127.3775, 'Daejeon Doryong Bus Stop (대전도룡동고속시외버스정류장) Departure Point', 'https://kko.kakao.com/m17R13IvP0');
pm(4, 36.33209, 127.4340, 'Daejeon Station (대전역)', 'https://kko.kakao.com/q2xzI4nqiG');


</script>

## Incheon Airport by the Airport Bus

For those who want to take the airport bus to the Incheon airport, we’d like to advise you to buy the tickets as early as possible if you have not done so already.

There are two bus stops close to the IBS: Government Complex <span class="mi">2</span> and Doryong Bus Stop <span class="mi">3</span>. Both are acceptable options. Doryong Bus Stop may be slightly closer, but it is unmanned and has only automated ticket machines. In contrast, the Government Complex stop features a staffed ticket office.


The earliest bus from the Daejeon Government Complex departs at 2:59 a.m., and the last bus leaves at 6:25 p.m.


### Method 1: Online 
One can reserve the ticket [online at https://txbuse.t-money.co.kr](https://txbuse.t-money.co.kr)
 and print it at the bus stop before you leave. You will likely want the following:
- Departure: Daejeon Gov Complex(airport route) <span class="mi">2</span> (or Daejeondoryong <span class="mi">3</span> if you are staying near Gaon)
- Destination: IncheonAirportT1 or IncheonAirportT2


### Method 2: Visit the ticket office 
You can also buy the airport ticket in person at the ticket office (and will print it here if you used Method 1). Here is the location of the Deajeon Gov Complex bus stop <span class="mi">2</span>. (It’s 2.3 km away from IBS.) You can also use the Doryong Bus Stop <span class="mi">3</span>.
https://maps.app.goo.gl/xd5Di9C8mn8vrbQYA


# Incheon Airport by the train

One can take the KTX train from the Daejeon Station <span class="mi">4</span> to Gwangmyeong Station or Seoul station and transfer to the Incheon airport.
