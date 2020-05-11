---
title: Payload Criterion
date: 2020-05-08
version: 2.1.0
keywords: [camera stream, standard, payload standard, equipment interference, hardware, PSDK structure, data transmission, video]
---
> **NOTE** 
> * This article is **Machine-Translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.
> * It is recommended to use **PSDK V2.xx** with the **X-Port** or **SkyPort V2** to develop the payload.
> * X-Port and SkyPort V2 only support the **PSDK V2.xx**
> * SkyPort only supports the **PSDK V1.xx**
> * The Mobile APP is DJI Pilot or a Mobile APP developed by MSDK.
> * The Payload is a device developed by PSDK.
> * The onboard computer is a computing device, such as Manifold, running a drone control program based on OSDK.

## Hardware
> **Prohibited**
> * Shorting the pins
> * Connect to power output device
> * Input the current to aircraft


##### Use M300 RTK
> **NOTE** DJI M200 Series support <b>X-Port, SkyPort V2 and SkyPort </b>.
<table>
<thead>
<tr>
  <th>Pin</th> 
  <th>Hardware</th> 
  <th>Description</th>
 </tr>
</thead>
 <tbody>
<tr>
  <td rowspan="3">General	</td>
  <td>X-Port</td>
  <td>13.6V / 2A</td>
 </tr>
 <tr>
  <td>SkyPort V2</td>
  <td>13.6V / 4A</td>
 </tr>
 <tr>
  <td>SkyPort</td>
  <td>13.6V / 4A</td>
 </tr>
 <tr>
  <td rowspan="2">High Power Apply</td>
  <td>X-Port</td>
  <td>17V / 2.5A</td>
 </tr>
 <tr>
  <td>SkyPort V2</td>
  <td>17V / 4A</td>
 </tr>
 <tr>
  <td>PPS</td>
   <td rowspan="4">X-Port</br>
    SkyPort V2</br>
    SkyPort</td>
  <td>≤3.3V</td>  
 </tr>
 <tr>
  <td>UART</td>
  <td>3.3V TTL Protocol
</td>
 </tr>
 <tr>
  <td>LAN</td>
  <td>LAN IEEE802.3 Protocol</td>
 </tr>
 <tr>
  <td>CAN </td>
  <td>CAN Protocol</td>
 </tr>
</tbody>
</table>


##### Use M200 V2 Series

<table>
<thead>
<tr>
  <th>Pin</th>
  <th>Hardware</th>
  <th>Description</th>
 </tr>
</thead>
 <tbody>
 <tr>
  <td rowspan="3">General</td>
  <td>X-Port</td>
  <td>13.6V / 2A</td>
 </tr>
 <tr>
  <td>SkyPort V2</td>
  <td>13.6V / 4A</td>
 </tr>
 <tr>
  <td>SkyPort</td>
  <td>13.6V / 4A</td>
 </tr>
 <tr>
  <td rowspan="2">High Power Apply</td>
  <td>X-Port</td>
  <td>17V / 2.5A</td>
 </tr>
 <tr>
  <td>SkyPort V2</td>
  <td>17V / 4A</td>
 </tr>
  <tr>
  <td>High Power Apply</td>
  <td>X-Port</br>SkyPort V2</td>
  <td>0～3.3V</td>
 </tr>
 <tr>
  <td>PPS</td>
  <td rowspan="3">X-Port</br>
    SkyPort V2</br>
    SkyPort</td>
  <td>≤3.3V</td>
 </tr>
 <tr>
  <td>UART</td>
  <td>3.3V TTL Protocol</td>
 </tr>
 <tr>
  <td>LAN</td>
  <td>LAN IEEE802.3 Protocol</td>
 </tr>
 <tr>
  <td>CAN</td>
  <td>SkyPort</td>
  <td>CAN Protocol</td>
 </tr>
</tbody>
</table>

##### Use M200 Series
> **NOTE** DJI M200 Series only support <b>SkyPort</b>.
<table>
<thead>
<tr>
  <th>Pin</th>
  <th>Description</th>
 </tr>
</thead>
 <tbody>
 <tr>
  <td >General</td>
  <td>12.7V / 4A</td>
 </tr>
 <tr>
  <td>PPS</td>
  <td>≤3.3V</td>
 </tr>
 <tr>
  <td>UART</td>
  <td>3.3V TTL Protocol</td>
 </tr>
 <tr>
  <td>LAN</td>
  <td>LAN IEEE802.3 Protocol</td>
 </tr>
 <tr>
  <td>CAN</td>
  <td>CAN Protocol</td>
 </tr>
</tbody>
</table>

## Noise 
<table>
<thead>
 <tr>
      <th>Item</th>
      <th>M200 和M200 V2</th>
      <th>M300 RTK</th>
    </tr>
</thead>
<tbody>
<tr>
  <td>Light Source Flashing	</td>
  <td colspan="2">If the payload is built-in a light source, the light source flashing frequency of the payload cannot be between 0.2 and 50 Hz.</td>
</tr> 
   <tr>
      <td>Light Wave Emission	</td>
      <td colspan="2">The payload cannot emit light with wavelengths between 600 and 700 nm.</td>
    </tr>
  <tr>
      <td>Magnetic Field</td>
      <td colspan="2">The payload should minimize magnetic interference, including but not limited to interference created by ferromagnetic substances producing high-intensity alternating magnetic fields.</td>
  </tr>
    <tr>
      <td rowspan="2">Electromagnetic Noise	</td>
      <td colspan="2">• The payload should not transmit electromagnetic waves in the 1 - 1.7 GHz, 2.3 - 2.6 GHz, and 5.7 - 5.9 GHz bands.</br>• The equivalent isotropic radiated power (EIRP) of the payload should be less than 1W.</td></tr>
    <tr>
      <td>• The payload should not transmit electromagnetic waves in the 1 - 1.7 GHz, 2.4 - 2.5 GHz, and 5.8 - 5.9 GHz bands. </br>• The equivalent isotropic radiated power (EIRP) of the payload should be less than 1W.</td>
      <td>-<td></tr>  
    <tr>
      <td>Acoustic Noise</td>
      <td>The payload cannot transmit or generate 35~45KHz band sound waves.</td>
      <td>-<td>
      </tr>
</tbody>
</table>

## Structural
> **NOTE**
> * To prevent the payload carried on the drone from being affected by the inertia of the drone, impact the battery and the blades, please design the smaller size of the payload.
> * In order to avoid the payload affecting the drone's rotational inertia, please minimize the size of the payload.

#### Operation Notice 
* M200 and M200 V2 series
The weight of the single payload in **600～1200g**, in order to avoid damaging the shock-absorbing ball, please use double to carry the payload. Make sure that the center of gravity of the payload is on the **vertical line of the connection center of the dual-gimbal**.
* M300 RTK
The total weight of the payload on the M300 RTK cannot exceed the maximum payload 2.7Kg; when using the gimbal adapt board, the weight of the payload should be less than 850g. 

#### Generic

<table id="PSDK technical integration NOTEs">
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
      <th>M300 RTK </th>
    </tr>
  </thead>
  <tbody>
      <tr>
      <td>Operation Temperature of the Payload's Case</td>
      <td colspan=2 style="text-align: center">≤70℃</td>
    </tr>
    <tr>
      <td>Weight</td>
      <td>≤1.2kg </td>
      <td> The maximum weight of the payload is 2.7Kg. When using the adapt board, the maximum weight of the payload should not exceed 850g </td>
    </tr>
    <tr>
      <td>Center of Gravity</td>
      <td>＜600g: The center of gravity of the payload should be on theoretical line at the center of the tilt port</br>600g～1200g: The center of gravity of the payload should be on the <b> double gimbal interface center perpendicular line.</b></td>
      <td>Use the gimbal adapt board to mount the payload, the center of gravity of the payload must be on the perpendicular line at the center of the gimbal.</td>
    </tr>
    <tr>
      <td>Structural Interference</td>
      <td colspan=2>When the aircraft is in various flight states, the payload can not interfere with the aircraft structure under various working conditions (the propellers shape will change during flight and the payload will have a certain motion lag relative to the aircraft during flight).</td>
    </tr>
    <tr>
      <td>Vibration</td>
      <td colspan=2>The payload exposure to vibration should be minimized. When the aircraft is turned on, the IMU cannot register as "Moving" on the "Sensors State" page of the DJI PILOT app under various working conditions.</td>
    </tr>
        <tr>
      <td>Trace Path</td>
      <td>The trajectory of the payload must not cover <b>the sensor and the ventilation holes</b> :</br>1. The view of the forward vision sensor: 75° × 60° (horizontal × vertical);</br> 2. The view of the downward vision sensor is 75° × 60° (horizontal × vertical);</br>
3. Within the range of 10cm from the ultrasonic sensor, the sensing range is 100°, outside 10cm is 70°;</br>4. Within 15cm from the infrared sensor, the sensing range of the infrared sensor is 60°, and the sensing range outside 15cm is 20°;
</br>5. The range of 10 cm from the front and rear of the drone's fuselage is the air inlet and outlet.</td>
      <td>The trajectory of the payload must not cover <b>the sensor and the ventilation holes</b> :</br>1. The view of the forward vision sensor: 75° × 56° (horizontal × vertical);</br> 2. The view of the upward vision sensor is 64° × 79° (horizontal × vertical);</br>3. The view of the downward vision sensor is 56° × 70° (horizontal × vertical);</br>4. The view of the left and right vision sensor is 79° × 64° (horizontal × vertical);</br>5. The angle of the six-directional infrared sensor is 30°;</br>6. The air inlet and outlet are within 5cm from the bottom and top of the drone.</td>
    </tr>
   </tbody>
</table>

#### Structural for X-Port
##### X-Port‘s structural
Figure 1 display the dimension of X-Port.    
<div>
<div style="text-align: center"><p>Figure 1 The dimension of X-Port（unit：mm）</p>
</div>
<div style="text-align: center"><p><span>
      <img src="../images/XPort-structure.png" width="450" style="vertical-align:middle" alt/></span></p>
</div></div>

##### Payload‘s structural
Before designing the structure of the payload, please choose a tripod, if the size of the payload is limited by the tripod.

<div>
  <table>
    <thead>
      <tr>
        <th> Gimbal Type</th>
        <th> Pitch axis rotation limit (Idle speed) </th>
        <th> Landing Gear Type </th>
        <th> X-Port payload structure limitation </th>
      </tr>
</thead>
<tbody>
<tr>
     <td rowspan=4> Single gimble platform </td>
     <td rowspan=2> Restricted </td>
     <td> Original </td>
     <td> The distance between the lower surface of the payload and the pitch axis is not more than 54mm. </td>
 </tr>
<tr>
    <td> Long </td>
    <td> The distance between the lower surface of the payload and the pitch axis is not more than 72mm. </td>
 </tr>
<tr>
    <td rowspan=2> None </td>
    <td> Original </td>
    <td> The payload must in the mass center, which the diameter of the ball is 118mm.</td>
 </tr>
<tr>
   <td> Long </td>
   <td> The payload must in the mass center, which the diameter of the ball is 154mm. </td>
</tr>
<tr>
<td rowspan=4>Double Gimbal </td>
<td rowspan=2> Restricted </td>
<td> Original </td>
<td> The distance between the lower surface of the payload and the pitch axis is not more than 45mm. </td>
</tr>
<tr>
<td> Long </td>
<td> The distance between the lower surface of the payload and the pitch axis is not more than 63mm. </td>
</tr>
<tr>
<td rowspan=2> None </td>
<td> Original </td>
<td> The payload must in the mass center, which the diameter of the ball is 100mm. </td>
</tr>
<tr>
<td> Long </td>
<td> The payload must in the mass center, which the diameter of the ball is 136mm. </td>
</tr>
</tbody>
</table>
</div>

The requirements of the payload which is mounted on the X-Port is as follows:    
* The width of the pitch on the X-Port is 80mm. The width of the payload couldn't exceed the wheelbase.     
* The weight of the payload must lighter than 450g otherwise the payload may damage the gimbal or the pressure-reducing-ball.     
* The centroid of the normal payload must on the axis line of X-Port，and the payload couldn't strike the X-Port when the payload raised to 45°. The centroid of the payload must on the axis line when the payload’s zoom is in the maximum factor.   
* If the payload touches the ground，please use the Long Landing Gear.    
* Be sure that the port of the payload is completely flat, ensure that the waterproof could be sealed completely.      
* The shell of payload could be aluminum alloy. A plastic or carbon case is not recommended.     

## Data Transmission
##### Use M200 V2 Series or M300 RTK

<table>
<thead>
    <tr>
      <th>Type</th>
      <th>Direction</th>
      <th>Limitation</th>
    </tr>
  </thead>
<tbody>
 <tr>
    <td rowspan="4">Command Channel</td>
    <td rowspan="1">Mobile APP ➟ Payload</td>
    <td rowspan="4">≤4096B/s</td>
    </tr>
     <tr>
      <td>Payload ➟ Mobile APP </td>
    </tr>
    <tr>
      <td>Onboard Computer ➟ Payload</td>
    </tr>
    <tr>
      <td>Payload ➟ Onboard Computer</td>
    </tr>
    <tr>
      <td>High-speed data transmission channel</td>
      <td>Payload ➟ Mobile APP</td>
      <td>Single Gimbal：≤ 8192Kbps</br>Double Gimbals：other ≤ 4096Kbps</td>
    </tr>
</tbody>    
</table>

##### Use M200 Series

> **NOTE** DJI M200 Series only supports <b>SkyPort</b> to transfer the data to Mobile APP, which developed based on MSDK.

<table>
<thead>
    <tr>
      <th>Type</th>
      <th>Direction</th>
      <th>Limitation</th>
    </tr>
  </thead>
<tbody>
 <tr>
       <td rowspan="2">Command Channel</td>
      <td>Mobile APP ➟ Payload</td>
      <td>≤500B/s</td>
    </tr>
    <tr>
      <td>Payload ➟ Mobile APP</td>
      <td>≤3072B/s</td>
    </tr>
    <tr>
      <td>High-speed data transmission channel	</td>
      <td>Payload ➟ Mobile APP</td>
      <td>ingle Gimbal：≤ 8192Kbps</br>Multi Gimbals：other ≤ 4096Kbps</td>
    </tr>
</tbody>    
</table>


## Video
Use PSDK to developed the Payload **must** use the **H.264** standard.

1. The maximum video resolution should small than 1920 × 1080.
2. The maximum frame rate should slowly than 30fps, and the maximum bit rate should small than 8Mbps.
3. The recommended video aspect ratio is 4: 3 (when using DJI CrystalSky, the screen can fill the screen).

> **NOTE** When using the H.264 encoding standard, the GOP encoding structure must use Period I (intra-frame encoded frames, one IDR frame will be inserted every 1 second to ensure that image data can be recovered if lost).

<table>
  <thead>
    <tr>
      <th>Item</th>
      <th>H.264 Item</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
 <tr>
      <td>Level </td>
      <td> Level Number</td>
      <td> ＜5.1 </td>
</tr>
<tr>
      <td>profile_idc</td>
      <td>7.3.2.1.1</td>
      <td> Baseline=66，Main=77，High=100 </td>
</tr>
<tr>
      <td>YUV420 Format </td>
      <td>7.3.2.1.1</td>
      <td>chroma_format_idc=1 </td>
</tr>
<tr>
      <td>8Bit video </td>
      <td>7.3.2.1.1</td>
      <td>bit_depth_luma_minus8=0</br>bit_depth_chroma_minus8=0 </td>
</tr>
<tr>
      <td>Not allowed customization,Scaling Matrix </td>
      <td> 7.3.2.1.1</br>7.3.2.2 </td>
      <td>seq_scaling_matrix_present_flag=0 </br>
      pic_scaling_matrix_present_flag=0 </td>
</tr>
<tr>
      <td>Only supports frame format encoding, not field encoding </td>
      <td>7.3.2.1.1 </td>
      <td>frames_mbs_only_flag=1</td>
</tr>
<tr>
      <td>Only P-frames and I-frames are allowed, and P-frames have a single reference frame </td>
      <td>7.3.3 </br> 7.3.2.2 </br> 7.3.3 </td>
      <td> slice_type = 0 or 2 </br>num_ref_idx_l0_default_active_minus1=0 </br> num_ref_idx_active_override_flag=0</td>
</tr>
<tr>
      <td>Not support Muti-Slice Group </td>
      <td>7.3.2.2 </td>
      <td>num_slice_groups_minus1=0 </td>
</tr>
</tbody>
</table>

> **Reference:** <a href="https://www.itu.int/rec/T-REC-H.264-201906-I/en">H.264 Protocol</a>



