---
title: Take a bus
order: 1
---
{% assign s = site.data.schedules["cjj-yuseong"] %}

There is a non-stop bus from Cheongju Airport to Yuseong Complex Terminal (유성복합터미널). It costs KRW 6,500 and takes **50 minutes**.

There is a bus ticket machine outside the Gate 1.
The bus runs from {{ s.first_bus }} to {{ s.last_bus }}.
The bus to Yuseong Intercity Bus Stop will be at the bus platform 2.
> Current schedule (as of {{ s.updated }})
>
> {{ s.times | join: ", " }}
{: .note-title }


|![Gate 1](/assets/images/cjj-gate1.jpg)|![Waiting room and ticket booth](/assets/images/cjj-bus-booth.jpg)|
|:--:|:--:|
|*Gate 1*|*Waiting room and ticket booth*|

### Buying a ticket at the kiosk

|![Kiosk main menu](/assets/images/cjj-machine1.jpeg)|![Check date and destination](/assets/images/cjj-machine4.jpeg)|
|:--:|:--:|
|*1. Tap **English**, then **Purchase ticket**. Cash and card are accepted (no coins).*|*2. Check the departure date, then tap the red **Destination** box to choose where you're going.*|

|![Destination list](/assets/images/cjj-machine3.jpeg)|![Select Yuseong](/assets/images/cjj-machine2.jpeg)|
|:--:|:--:|
|*3. On the destination list, tap the **Daejeon/Sejong** region on the left.*|*4. Select **Yuseong**.*|

|![Select departure time](/assets/images/cjj-machine5.jpeg)|
|:--:|
|*5. Pick a departure time, then pay to print your ticket. Tickets can't be printed within 1 minute of departure.*|

