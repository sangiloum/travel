---
title: Using the Airport Bus to go to Daejeon directly
order: 1
---
{% assign s = site.data.schedules["icn-govcomplex"] %}

For most visitors, this is the most recommended method to visit IBS.
From the Incheon Airport, you can take the airport bus to the Daejeon Government Complex. The bus will take you directly. The bus ride will take roughly **2 hours 45 minutes**.

You can buy bus tickets inside the airport.
You can easily find the ticket counter and pay by your credit card or cash. There are also several bus ticket machines.
Please purchase the ticket for **Daejeon Government Complex (대전청사)** Bus Stop.
#### Bus Schedule (as of {{ s.updated }})

| Departure | Class | Fare for an Adult (KRW) |
| :--: | :--: | :--: |
{% for row in s.rows %}| {{ row.time }} | {{ row.class }} | {{ row.fare }} |
{% endfor %}

{: .note}
The prices are almost same for all four stops in Daejeon (North Daejeon, Daedeok Culture Center
     (Doryong), Government Complex, and Daejeon Bus Terminal). Although the Daedeok Culture Center is also close to IBS, there are not many taxis waiting at the stop. 
     If you don't mind walking with luggage, 
     then it is possible to get off at the Daedeok Culture Center (Doryong) stop and walk for 30 minutes to IBS.
     Otherwise, it is difficult to get a taxi at this location, and we recommend the Government Complex stop.

```mermaid
flowchart TD;
subgraph ICN["Incheon Airport"]
direction LR
    icn2["Terminal 2"]  
    --20 min. -->icn1["Terminal 1"]
end
subgraph Daejeon
direction LR
    nd["North 
    Daejeon
    북대전"]
    --> doryong["Daedeok Culture Center
     (Doryong)
    대덕문화센터(도룡)"]
    --5 min.--> gov["Daejeon 
    Government Complex
    대전청사"]
    --> dt["Daejeon 
    Bus Terminal
    대전복합터미널"]
end

ICN == 2 hours 35 min.==>Daejeon
```





The bus to Daejeon will be at **bus platform 11A-3**.
The ticket will have your departure time and your seat number.
There is no bathroom on the bus. Sometimes the bus stops at the highway rest area for 10 or 20 minutes.

|![Inside Ticket Office (Gate 11)](/assets/images/icn1-bus-ticket.jpg)|![Bus Ticket](/assets/images/icn-bus-ticket2.jpg)|
|:--:|:--:|
|*Inside Ticket Office (Gate 11)*|*Bus Ticket*|
|![Bus Platform 11A-3](/assets/images/icn-t1-platform.jpg)|![Bus](/assets/images/icn-bus.jpg)|
|*Bus Platform 11A-3*|*Bus to Daejeon*|



- Price: KRW 26,100 for deluxe and KRW 34,000 for premium. Night buses (after 10pm) are 10% more expensive.
- Schedule: Earliest at {{ s.first_bus }}. Last at {{ s.last_bus }}.
- [Online booking](https://intercitybuse.tmoney.co.kr/) at [https://intercitybuse.tmoney.co.kr/](https://intercitybuse.tmoney.co.kr/) :  You can check the time schedule and the current availability of the seats. 
  - Departure: IncheonAirportT1
  - Destination: DaejeonGovComplex

It was announced that foreign credit cards (VISA, Master, JCB, UnionPay) would work on this website from July 2024. Please let us know if it worked. If you want to use foreign credit cards, you may want to choose "GLOBAL CARD" in the list of credit cards. For "Card Password", it only needs the first 2 digits of your credit card password. For "Resident Registration Number (front 6 digits"), you simply need to type your birthday in YYMMDD format. For the Cellular Phone number, if you don't have the Korean mobile phone number, put any number. That is for the identification. For the Card Password, you only need to put the first 2 digits of your credit card PIN code.

![Daejeon Government Complex (대전청사) Bus Stop](/assets/images/govcomplexstop.jpg)

Other than a very small sign, there is no written signage and this bus stop doesn't appear on many maps. Don't let that stop you as many people get off buses here; so many that there is always a queue of taxis waiting to pick up passengers. Some visitors reported that a stranger approached them to offer a ride for a cash; do not follow them. 