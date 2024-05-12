---
title: Local Information

---
# Local Information 

<div id="map2"></div>
<script language="javascript">
var map = L.map('map2').setView([36.3763,127.3885], 15);
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
pm(2,36.38016, 127.3844, 'IBS Guesthouse/Dormitory  (기초과학연구원 생활관)', 'https://kko.to/aR9OKe2qoC');
pm(3,36.3755, 127.382, 'Shinsaege Department Store (신세계백화점)', 'http://en.shinsegae.cn/store/introduce.do?storeSeq=14');
pm(4,36.37482, 127.3833, 'Shinsegae Expo Tower', 'https://kko.to/POEWMn3-ki'
);
pm(5,36.37481, 127.3893,'DCC 2 (Daejeon Convention Center 2)', 'http://www.dcc.co.kr/eng/main/main.php');
pm(6,36.3782,127.392,"Convenience Stores",'https://kko.to/H2KLcpAZ4v');
pm(7,36.3765, 127.3912,'Golfzone Zoimaru','http://golfzonzoimaru.co.kr/f_coffee' );
pm(8,36.37695, 127.3933, 'ICC Hotel (ICC 호텔)', 'http://hotel.hotelicc.com/view/index.do?SS_SVC_LANG_CODE=ENG');
pm(9,36.37601, 127.392, 'Weltz Tower', 'https://kko.to/n89YwJBrEe');
pm(10,36.37601, 127.3929, 'Lotte City Hotel (롯데시티호텔)', 'https://www.lottehotel.com/daejeon-city/en.html');
pm(11,36.37601, 127.3937, 'GS The Fresh (Grocery Store)','https://kko.to/92PAI8InaC' );
pm(12,36.37601, 127.3947, 'hausD Urban Street Mall (Restaurants / Cafes)','https://kko.to/1zXvUK6QLb' );
pm(13,36.37679, 127.3968, "Farmers 161 (Farmers' Market)", 'https://kko.to/P770F3Lh51');
pm(14,36.3753, 127.3923,'Sungsimdang (Bakery)', 'https://www.sungsimdang.co.kr/31/17');
pm(15,36.37481, 127.3930, 'I-Hotel (아이호텔)', 'https://www.ihotel.co.kr/');
pm(16,36.3685,127.386,'Hanbat Arboretum West (한밭수목원 서원)','https://www.daejeon.go.kr/gar/contentsHtmlView.do?menuSeq=2307');
pm(17,36.3685,127.3893,'Hanbat Arboretum East (한밭수목원 동원)','https://www.daejeon.go.kr/gar/contentsHtmlView.do?menuSeq=2307');
pm(18,36.36677, 127.3871,'Leeungno Museum (이응노 미술관)', 'https://www.leeungnomuseum.or.kr/?en=Us');
pm(19,36.3850075, 127.3795, 'Gaon Residence Hotel','https://www.tripadvisor.com/Hotel_Review-g297887-d7333707-Reviews-Gaon_Residence_Hotel-Daejeon.html');
pm(20,36.3850075, 127.3789, 'Woori Bank (우리은행)','https://kko.to/xXGyuZ4gBq');
pm(21,36.3854, 127.3784, 'Post Office','https://kko.to/xXGyuZ4gBq');
pm(22,36.38058, 127.3783, "McDornald's",'https://kko.to/MzmoTxsZnf');
pm(23,36.37576, 127.3756,"National Science Museum (국립중앙과학관)", 'https://www.science.go.kr/eps');
pm(24,36.368,127.3805,"Mannyeon-dong",'https://kko.to/rrjvSwh-Lo');
</script>

- IBS
  - IBS, Main Entrance <span class="mi">1</span>: The entrance pass can be picked up at the reception in the main lobby. You may need a photo ID to pick up the pass. Since the reception is located in the Building B (Theory Building) already, after passing through the security gate using the entrance pass, go straight until you see the elevator on the right, next to the cafeteria. Take the elevator to the 3rd floor. Discrete Mathematics Group and Extremal Combinatorics and Probabaility Group are located on the left side of the elevator, right above the reception and the main entrance.
  The eduroam Wi-Fi is available. If you don't have the eduroam account, please contact your host to get the guest Wi-Fi account.
  - IBS Guesthouse / Dormitory <span class="mi">2</span> You will need to find the key code in the email instruction in order to enter the building. There is no front desk or reception here. In the emergency, please go to the reception at the main building <span class="mi">1</span>; the security guard will be there for 24 hours. Wi-Fi is available for free.
- Hotels
  - Onoma Hotel (오노마호텔) <span class="mi">4</span>, I-Hotel (아이호텔) <span class="mi">15</span>, ICC Hotel (ICC호텔) <span class="mi">8</span>, Lotte City Hotel (롯데시티호텔) <span class="mi">10</span>, Gaon Residence Hotel (가온레지던스호텔) <span class="mi">19</span>
- Groceries: Open every day.
  - GS The Fresh <span class="mi">11</span> (9 am - 11 pm), Farmers 161 <span class="mi">13</span> (9 am - 9 pm; Local produce, fruits, vegetables, etc.)
- Post Office <span class="mi">21</span>
- Banks
  - Shinhan Bank (신한은행) <span class="mi">4</span> (9th Floor), Woori Bank (우리은행) <span class="mi">20</span>
  - ATM of the Woori Bank is located in the 1st floor of the IBS Main Building <span class="mi">1</span>.
- Bakery: Sungsimdang <span class="mi">14</span> (Open at 8 am)
- Cafe (having sandwiches for breakfast)
  - Sungsimdang Cafe (성심당 카페) <span class="mi">14</span> (2nd Floor): 
    Open at 8 am. Brunch menu (Salad, Toast, Sandwich) is available from 8 am to 7 pm. Tea, Coffee.
  - Starbucks (스타벅스) <span class="mi">4</span> (38th Floor, open at 8 am), <span class="mi">7</span> (Open at 7:30 am / 8 am (Wed, Sat, Sun))
  - Paul Bassette (폴바셋) <span class="mi">4</span> (39th Floor). Open at 9 am.
  - Caffe Pascucci: Across the street from <span class="mi">8</span>. Open at 8 am.
- Restaurants
  - Shinsegae Department Store (신세계백화점) <span class="mi">3</span>: B1F for food court, bakeries, grocery. 5th Floor for various restaurants (Korean, Chinese, Indian, Hong Kong, etc.) and another food court called the Hanbat Grand Food Hall (한밭대식당). Outback Stakehouse on 7th Floor.
  - Il Forno (일뽀르노) <span class="mi">4</span> (39th Floor, Italian, Self-service restaurant).
  - Lieto Firenze (리에또피렌체) <span class="mi">7</span> (2nd Floor, Italian). 
  - Foodmaru <span class="mi">7</span> (Food Court. Closed on Monday)
  - Gyeongbokgung Kappo Jeju (경복궁갓포제주) <span class="mi">5</span> (2nd Floor, Korean).
  - Various Restaurants in hausD Street Mall <span class="mi">12</span> (1st Floor, 2nd Floor).
  - Udonya (우동야) <span class="mi">9</span>. Japanese Udon. Run by Sungsimdang.
  - McDonald's <span class="mi">22</span> (24 hours)
  - Mannyeon-dong <span class="mi">24</span> (Various restaurants)
  - [Restaurant Guide Book around Daejeon Convention Center (PDF File)](http://www.micedaejeon.com/images/djec/link/Restaurant_Guide_Book_Around_DCC_Eng.pdf)
- Sightseeing
  - Hanbat Arboretum (한밭수목원) <span class="mi">16</span> <span class="mi">17</span>, Leeungno Museum <span class="mi">18</span>, National Science Museum <span class="mi">23</span>
  - [Daejeon Tour Guide (PDF File)](http://www.djto.kr/boardFileDown.do?file_idx=10883)
- Pharmacy
  - JEONG Pharmacy (정약국) <span class="mi">4</span>. Closed on Sunday. Open at 10am. Closed at 7:30pm on weekdays, 4:30pm on Saturday.
  - ON Pharmacy (온약국) <span class="mi">24</span>.
- Convenience Stores (open 24 hours)
  - Emart24 (이마트24) <span class="mi">6</span> <span class="mi">5</span> (2nd Floor).
  - GS25 located between <span class="mi">11</span> and <span class="mi">12</span>
  - CU <span class="mi">6</span> <span class="mi">9</span>
  - 7Eleven <span class="mi">12</span>

## Other information
{% include tips.md %}