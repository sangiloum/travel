---
title: Take a bus
order: 1
---
{% assign s = site.data.schedules["cjj-yuseong"] %}

There is a non-stop bus from Cheongju Airport to Yuseong Complex Terminal (유성복합터미널). It costs KRW 6,500 and takes **40 minutes**.

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

|![Ticket Machine](/assets/images/cjj-ticketmachine.jpg)|
|:--:|
|*Ticket Machine*|

