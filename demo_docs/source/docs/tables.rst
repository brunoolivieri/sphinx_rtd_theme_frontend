.. _TABLE:

=====
Table
=====

Table test


.. raw:: html

   <table border="1" class="docutils wy-table-responsive">
   <tbody>
   <tr>
   <th>Region</th>
   <th>Relevant standards</th>
   <th>Model</th>
   <th>Model</th>
   <th>Model</th>
   <th>Model</th>
   </tr>
   <tr>
   <td>USA</td>
   <td>FCC 15.247</td>
   <td><strong>SikRadio 900MHz</strong>
   
   MIN_FREQ: 902000

   MAX_FREQ: 928000

   NUM_CHANNELS=50 
   
   <strong>Standard:</strong> FCC 15.247
   </td>
   <td><strong>RFD900 868MHz</strong></td>
   <td>
   </td>
   <td>
   </td>
   </tr>
   <tr>
   <td>Canada</td>
   <td>RSS-210 Annex 8.1</td>
   <td><strong>SikRadio 900MHz</strong>

   MIN_FREQ: 902000

   MAX_FREQ: 928000

   NUM_CHANNELS=50


   <strong>Standard</strong>: RSS-210 Annex 8.1   </td>
   <td></td>
   <td></td>
   <td></td>
   </tr>
   <tr>
   <td>Australia</td>
   <td>LIPD-2000 item 52, LIPD-2000 item 17</td>
   <td><strong>SikRadio 900MHz</strong>

   MIN_FREQ: 915000

   MAX_FREQ: 928000

   NUM_CHANNELS>=20


   <strong>Standard</strong>: LIPD-2000 item 52
   </td>
   <td><strong>SikRadio 433MHz</strong>

   MIN_FREQ: 433050
 
   MAX_FREQ: 434790

   TXPOWER<=14

   <strong>Standard</strong>: LIPD-2000 item 17
   </td>
   <td></td>
   <td></td>
   </tr>
   <tr>
   <td>Europe (most countries)</td>
   <td>ETSI EN300 220 7.2.3</td>
   <td><strong>SikRadio 433MHz</strong>

   MIN_FREQ: 433050

   MAX_FREQ: 434790

   TXPOWER< 8

   DUTY_CYCLE 10


   <strong>Standard</strong>: ETSI EN300 220 7.2.3
   </td>
   <td></td>
   <td></td>
   <td></td>
   </tr>
   <tr>
   <td>United Kingdom</td>
   <td>IR2030/1/10</td>
   <td><strong>SikRadio 433MHz</strong>

   MIN_FREQ: 433050

   MAX_FREQ: 434790

   TXPOWER<8

   DUTY_CYCLE 10

   <strong>Standard:</strong> d
   </td>
   <td></td>
   <td></td>
   <td></td>
   </tr>
   <tr>
   <td>New Zealand</td>
   <td>Notice 2007, Schedule 1</td>
   <td><strong>SikRadio 900MHz</strong>

   MIN_FREQ: 921000

   MAX_FREQ: 928000

   <strong>Standard:</strong> Notice 2007, Schedule 1
   </td>
   <td><strong>SikRadio 433MHz</strong> MIN_FREQ: 433050

   MAX_FREQ: 434790 <strong>Standard:</strong> Notice 2007, Schedule 1
   </td>
   <td></td>
   <td></td>
   </tr>
   <tr>
   <td>Brazil</td>
   <td>ANATEL – <a href="http://legislacao.anatel.gov.br/resolucoes/23-2008/104-resolucao-506">Resolução nº 506/2008</a></td>
   <td><strong>SikRadio 433MHz</strong>

   MIN_FREQ: 433000

   MAX_FREQ: 435000

   TXPOWER<=8

   <strong>Standard:</strong> <a href="http://www.cnc.gov.ar/infotecnica/espectro/uso/destacados01.asp">Comisión Nacional de Comunicaciones</a>  </td>
   <td><strong>SikRadio 900MHz</strong>

   MIN_FREQ: 915000

   MAX_FREQ: 928000

   NUM_CHANNELS>=26

   <strong>Standard:</strong> <a href="http://www.cnc.gov.ar/infotecnica/espectro/uso/destacados01.asp">Comisión Nacional de Comunicaciones</a> </td>
   <td></td>
   <td></td>
   </tr>
   <tr>
   <td>Argentina</td>
   <td><a href="http://www.cnc.gov.ar/infotecnica/espectro/uso/destacados01.asp">Comisión Nacional de Comunicaciones</a> </td>
   <td><strong>SikRadio 900MHz</strong>

   MIN_FREQ: 902000

   MAX_FREQ: 928000

   <strong>Standard:</strong> <a href="http://www.cnc.gov.ar/infotecnica/espectro/uso/destacados01.asp">Comisión Nacional de Comunicaciones</a>   </td>
   <td></td>
   <td></td>
   <td></td>
   </tr>
   <tr>
   <td>South Africa</td>
   <td>2008 RR 5.138, Government Gazette No 31127,Notice No 713 of 2008 and
   Government Gazette No 31290,Notice No 926 of 2008
   </td>
   <td><strong>SikRadio 433MHz</strong>

   MIN_FREQ: 433050

   MAX_FREQ: 434790

   TXPOWER<=10mW

   <strong>Standard:</strong> 2008 RR 5.138, Government Gazette No 31127,Notice No 713
   of 2008 and Government Gazette No 31290,Notice No 926 of 2008
   </td>
   <td></td>
   <td></td>
   <td></td>
   </tr>
   </tbody>
   </table>

MAV_CMD_MISSION_START
------------------------

.. raw:: html

   <table border="1" class="docutils">
   <tbody>
   <tr>
   <th>Command Field</th>
   <th>Mission Planner Field</th>
   <th>Description</th>
   </tr>
   
   <tr style="color: #c0c0c0">
   <td><strong>param1</strong></td>
   <td></td>
   <td>The first mission item to run.</td>
   </tr>
   
   <tr style="color: #c0c0c0">
   <td><strong>param2</strong></td>
   <td></td>
   <td>The last mission item to run (after this item is run, the mission ends).</td>
   </tr>
   
   <tr style="color: #c0c0c0">
   <td>param3</td>
   <td></td>
   <td></td>
   </tr>
   
   <tr style="color: #c0c0c0">
   <td>param4</td>
   <td></td>
   <td></td>
   </tr>
   
   <tr style="color: #c0c0c0">
   <td>param5</td>
   <td></td>
   <td></td>
   </tr>
   
   <tr style="color: #c0c0c0">
   <td>param6</td>
   <td></td>
   <td></td>
   </tr>
   
   <tr style="color: #c0c0c0">
   <td>param7</td>
   <td></td>
   <td></td>
   </tr>
   </tbody>
   </table>


   