---
nav_order: 3
title: Return to the airport
has_children: true
has_toc: false
---
# Return to the airport

Which airport are you flying out of?

- **Incheon Airport (ICN)** — most international flights. Allow up to 3 hours by the airport bus.
- **Cheongju Airport (CJJ)** — the closest airport, about 51 km from IBS, with flights to Jeju, Japan, Taipei, Vietnam, the Philippines, and Mongolia.
- **Gimpo Airport (GMP)** — domestic flights and short-haul international flights such as Tokyo Haneda, Osaka, and Shanghai Hongqiao.

<div class="destination-grid">
  <a href="/return/icn/" class="destination-card">
    <span class="destination-card__name">Incheon Airport (ICN)</span>
    <span class="destination-card__korean">인천국제공항</span>
  </a>
  <a href="/return/cjj/" class="destination-card">
    <span class="destination-card__name">Cheongju Airport (CJJ)</span>
    <span class="destination-card__korean">청주국제공항</span>
  </a>
  <a href="/return/gmp/" class="destination-card">
    <span class="destination-card__name">Gimpo Airport (GMP)</span>
    <span class="destination-card__korean">김포국제공항</span>
  </a>
</div>

<div id="map"></div>
<script language="javascript">
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
var icn1 = [37.44966, 126.4514];
var cjj = [36.72261, 127.4965];
var gmp = [37.56535, 126.8011];
L.marker(ibs).addTo(map).bindPopup('<b><a href="https://kko.to/5AYThThWnr" target="maps">IBS Discrete Mathematics Group (IBS 이산수학그룹)</a></b>');
L.marker(icn1, {icon: redIcon}).addTo(map).bindPopup('<b><a href="/return/icn/">Incheon Airport (ICN)</a></b>');
L.marker(cjj, {icon: redIcon}).addTo(map).bindPopup('<b><a href="/return/cjj/">Cheongju Airport (CJJ)</a></b>');
L.marker(gmp, {icon: redIcon}).addTo(map).bindPopup('<b><a href="/return/gmp/">Gimpo Airport (GMP)</a></b>');
var bounds = new L.latLngBounds([ibs, icn1, cjj, gmp]);
map.fitBounds(bounds);
</script>
