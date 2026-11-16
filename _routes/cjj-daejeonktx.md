---
order: 2
title: Use a train
---
{% assign t = site.data.schedules["train-cjj-daejeon"] %}

Cheongju Airport (청주공항) has its own train station, Cheongju Airport Station (청주공항역). It is a walking distance (600m) from Cheongju Airport, which takes about 10 minutes.

You can take a train to Daejeon Station (대전역) from Cheongju Airport Station. The ride takes about **1 hour**. A Mugunghwa (무궁화) ticket costs **KRW 3,900**; an ITX ticket costs KRW 5,900.
The train schedule is available at the [Korail website](http://www.letskorail.com/).

{: .important}
Since Cheongju Airport Station is an unmanned station, to buy a ticket, 
visit the Tourism Information (충청북도 관광안내소) on the 1st floor of the passenger terminal of the airport.
The platform gate opens 15 minutes before each departure.

You can also buy a ticket online at
- [Korail Website (English)](https://www.letskorail.com/english)
- [Mobile Korail Website (English)](https://m.letskorail.com/english)

For visitors from China, it is also possible to buy the train ticket on [WeChat](https://www.minipaycn.com/minipay/wechat.do) or [AliPay](https://www.minipaycn.com/minipay/alipay.do).

As of 2023, it is possible to buy tickets online at above website by using foreign credit cards.

#### Train timetable (Cheongju Airport → Daejeon, as of {{ t.updated }})

| Train | Departure (Cheongju Airport) | Arrival (Daejeon) | Travel time |
| --- | --- | --- | --- |
{% for r in t.rows %}| {{ r.train }}{% if r.type == "ITX" %} (ITX){% endif %} | {{ r.departure }} | {{ r.arrival }} | {{ r.minutes }} min |
{% endfor %}
*Source: Korail open data (recent daily runs). Times can change, so check Korail before you travel.*

{: .note}
You may also buy a ticket to Sintanjin Station (신탄진역) and take a taxi to your final destination. Sintanjin Station is one station before Daejeon Station. 
