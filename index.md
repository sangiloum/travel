---
nav_order: 1
title: Travel Instructions to IBS
---
<div class="hero">
  <div class="hero__content">
    <p class="hero__eyebrow">Institute for Basic Science</p>
    <h1>How to get to IBS, Daejeon</h1>
    <p class="hero__lead">Clear, step-by-step directions to the IBS campus for visitors and collaborators.</p>
    <div class="hero__actions">
      <a href="#start" class="btn btn-blue">Choose your starting point</a>
      <a href="#notice" class="btn">Entry requirements</a>
      <a href="/localinfo/" class="btn">Local information</a>
    </div>
  </div>
  <div class="hero__facts">
    <div class="fact">
      <div class="fact__label">Main airport</div>
      <div class="fact__value">
        ICN
        <a href="/icn/" class="fact__link">Terminal 1</a>
        <a href="/icn2/" class="fact__link">Terminal 2</a>
      </div>
    </div>
    <div class="fact">
      <div class="fact__label">Nearest airport</div>
      <div class="fact__value">
        <a href="/cjj/" class="fact__link">Cheongju (CJJ)</a>
      </div>
    </div>
    <div class="fact">
      <div class="fact__label">Main rail hub</div>
      <div class="fact__value">
        <a href="/seoul/" class="fact__link">Seoul Station</a>
      </div>
    </div>
  </div>
</div>

<div class="notice">
  <h3>Returning to the airport</h3>
  <p>Need directions from IBS back to the airport? Use the return guide for the most convenient routes.</p>
  <p><a href="/return/" class="btn btn-blue v-align-middle">How to return to the airport</a></p>
</div>

<h2 id="start">Choose your starting point</h2>
<p class="section-lead">Pick an airport or a major city station to see the best route to IBS.</p>

<div class="grid">
  <div class="card">
    <h3>Airports</h3>
    <div class="tile-grid">
      <a href="/icn/" class="tile tile--featured">
        <span class="tile__title">Incheon International Airport (ICN)</span>
        <span class="tile__sub">Terminal 1 · Major international hub</span>
      </a>
      <a href="/icn2/" class="tile tile--featured">
        <span class="tile__title">Incheon International Airport (ICN)</span>
        <span class="tile__sub">Terminal 2 · Major international hub</span>
      </a>
      <a href="/gmp/" class="tile">
        <span class="tile__title">Gimpo International Airport (GMP)</span>
        <span class="tile__sub">김포공항 · Closer to Seoul</span>
      </a>
      <a href="/cjj/" class="tile tile--featured">
        <span class="tile__title">Cheongju International Airport (CJJ)</span>
        <span class="tile__sub">청주공항 · Closest to Daejeon</span>
      </a>
      <a href="/tae/" class="tile">
        <span class="tile__title">Daegu International Airport (TAE)</span>
        <span class="tile__sub">158 km to IBS</span>
      </a>
    </div>
  </div>

  <div class="card">
    <h3>Rail stations</h3>
    <div class="tile-grid">
      <a href="/seoul/" class="tile tile--featured">
        <span class="tile__title">Seoul Station</span>
        <span class="tile__sub">서울역 · Main rail hub</span>
      </a>
      <a href="/suseo/" class="tile">
        <span class="tile__title">Suseo Station</span>
        <span class="tile__sub">수서역 · SRT hub</span>
      </a>
      <a href="/gwangmyeong/" class="tile">
        <span class="tile__title">Gwangmyeong Station</span>
        <span class="tile__sub">광명역 · KTX access</span>
      </a>
      <a href="/dongdaegu/" class="tile">
        <span class="tile__title">Dongdaegu Station</span>
        <span class="tile__sub">동대구역 · KTX access</span>
      </a>
      <a href="/busan/" class="tile">
        <span class="tile__title">Busan Station</span>
        <span class="tile__sub">부산역 · KTX access</span>
      </a>
    </div>
  </div>
</div>

<h2 id="notice">Entry requirements</h2>
<div class="notice">
  <h3>
    <a href="https://www.k-eta.go.kr/portal/board/viewboarddetail.do?bbsSn=258312">K-ETA (Korea Electronic Travel Authorization) Temporary Exemption</a>
  </h3>
  <p>
    Normally, citizens of some countries do not need a visa to visit Korea, but they must obtain the K-ETA online before flying to Korea.
    The Ministry of Justice of Korea has temporarily exempted the K-ETA for citizens of 52 countries (including the US, Canada, Australia, and most European countries) until December 31, 2026.
    Please check the <a href="https://www.k-eta.go.kr/portal/board/viewboarddetail.do?bbsSn=299707">K-ETA website</a> for details.
  </p>
  <p class="muted">This extension of exemption was announced on December 23, 2025.</p>
  <p>
    Visitors without K-ETA are required to fill out the <a href="https://www.e-arrivalcard.go.kr">e-Arrival card</a> at
    <a href="https://www.e-arrivalcard.go.kr">www.e-arrivalcard.go.kr</a>.
    There is no fee, and you can submit it within 3 days before arrival in Korea.
  </p>
</div>

<h2>Map</h2>
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
