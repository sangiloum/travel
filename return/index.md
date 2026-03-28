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
## Incheon Airport (ICN)

The most recommended way to reach the Incheon Airport from Daejeon is to take the airport bus. 
There are frequent buses from 3 am so that you can catch an early morning flight.
It is strongly recommended to buy the ticket early.
It takes up to 3 hours to reach the terminal 1 
and up to 3 hours 18 minutes to reach the terminal 2.

### Incheon Airport by the Airport Bus

For those who want to take the airport bus to the Incheon airport, we’d like to advise you to buy the tickets as early as possible if you have not done so already.

There are two bus stops close to the IBS: Government Complex  (정부청사) <span class="mi">2</span> and Doryong Bus Stop (도룡) <span class="mi">3</span>. Both are acceptable options. Doryong Bus Stop may be slightly closer, but it is unmanned and has only automated ticket machines. In contrast, the Government Complex stop features a staffed ticket office.

The earliest bus from the Daejeon Government Complex departs at 2:59 a.m., and the last bus leaves at 6:25 p.m.


Make sure to board the correct bus. Not only the airport buses but also buses to Seoul and other cities will stop there. 

#### Method 1: Online 
One can reserve the ticket [online at https://txbuse.t-money.co.kr](https://txbuse.t-money.co.kr)
 and print it at the bus stop before you leave. You will likely want the following:
- Departure: Daejeon Gov Complex(airport route) <span class="mi">2</span> (or Daejeondoryong <span class="mi">3</span> if you are staying near Gaon)
- Destination: IncheonAirportT1 or IncheonAirportT2

If you want to use foreign credit cards, you should choose "GLOBAL CARD" in the list of credit cards. For "Card Password", it only needs the first 2 digits of your credit card password, but probably you can type anything, because it doesn't matter much.

For "Resident Registration Number (front 6 digits"), you simply need to type your birthday in YYMMDD format. For the Cellular Phone number, if you don't have the Korean mobile phone number, put any number, for instance the phone number of your host at IBS. That is for the identification. 

After booking the ticket, you'll need to pick up the ticket at the bus stop by using the machine. It'll ask you to identify yourself by using the credit card number that was used to pay for your bus ticket or the phone number.


#### Method 2: Visit the ticket office 
You can also buy the airport ticket in person at the ticket office (and will print it here if you used Method 1). Here is the location of the Deajeon Gov Complex bus stop <span class="mi">2</span>. (It’s 2.3 km away from IBS.) You can also use the Doryong Bus Stop <span class="mi">3</span> to buy the ticket using the machine.

|![Government Complex Bus Stop](/assets/images/dunsan.jpg)|
|:--:|
|*Government Complex Bus Stop* <span class="mi">2</span>|

|![Ticket Machine at the Government Complex Bus Stop](/assets/images/dunsan-ticket.jpg)|![Ticket Office at the Government Complex Bus Stop](/assets/images/dunsan-ticket-office.jpg)|
|:--:|:--:|
|*Ticket Machine for the Incheon Airport at the Government Complex Bus Stop* <span class="mi">2</span>|*Ticket Office at the Government Complex Bus Stop* <span class="mi">2</span> (6am-9:15pm)|

|![Doryong Bus Stop](/assets/images/doryong.jpg)|![Ticket Machines at the Doryong Bus Stop](/assets/images/doryong-ticket.jpg)|
|:--:|:--:|
|*Doryong Bus Stop* <span class="mi">3</span>|*Ticket Machines at the Doryong Bus Stop* <span class="mi">3</span>|


### Incheon Airport by the train

One can take the KTX train from the Daejeon Station <span class="mi">4</span> to Gwangmyeong Station or Seoul station and transfer to the Incheon airport.


## Cheongju Airport (CJJ)

### Cheongju Airport by the taxi

The taxi from IBS to Cheongju airport may cost about 50,000 KRW. 

### Cheongju Airport by the Airport Bus

{% assign s = site.data.schedules["yuseong-cjj"] %}
You can take a bus from Yuseong Complex Terminal (유성복합터미널) to Cheongju Airport (청주공항). The price is 6,500 KRW and the ride takes about 50 minutes. The first bus departs at {{ s.first_bus }} and the last bus departs at {{ s.last_bus }}.

> Current schedule (as of {{ s.updated }})
>
> {{ s.times | join: ", " }}
{: .note-title }

Times can change, so confirm at the Yuseong ticket office or kiosk on the day you depart.


### Cheongju Airport by the Local Train
There is a train stop at the Cheongju Airport. You can take a local train from Daejeon Station to Cheongju Airport. It takes about 1 hour. The airport train stop is a short walking distance to the airport terminal.

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
