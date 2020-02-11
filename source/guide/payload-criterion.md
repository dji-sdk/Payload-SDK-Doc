---
title: Payload Criterion
date: 2020-01-17
version: 2.0.0
keywords: [camera stream, standard, payload standard, equipment interference, hardware, PSDK structure, data transmission, video]
---
> **NOTE** 
> * This article is **machine-translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.
> * It is recommended to use **PSDK V2.xx** with the **X-Port** or **Skyport V2** to develop the payload.
> * X-Port and Skyport V2 only support the **PSDK V2.xx**
> * Skyport only supports the **PSDK V1.xx**
> * The Mobile APP is DJI Pilot or a Mobile APP developed by MSDK.
> * The Payload is a device developed by PSDK.
> * The onboard computer is a computing device, such as Manifold, running a drone control program based on OSDK.

## Hardware
> **prohibited**
> * Shorting the pins
> * Connect to power output device
> * Input current to aircraft


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
  <td>Skyport V2</td>
  <td>13.6V / 4A</td>
 </tr>
 <tr>
  <td>Skyport</td>
  <td>13.6V / 4A</td>
 </tr>
 <tr>
  <td rowspan="2">High Power Apply</td>
  <td>X-Port</td>
  <td>17V / 2.5A</td>
 </tr>
 <tr>
  <td>Skyport V2</td>
  <td>17V / 4A</td>
 </tr>
 <tr>
  <td>PPS</td>
  <td rowspan="3">X-Port</br>
    Skyport V2</br>
    Skyport</td>
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
  <td>Skyport</td>
  <td>CAN Protocol</td>
 </tr>
</tbody>
</table>

##### Use M200 Series
> **NOTE:** DJI M200 Series only support <b>Skyport</b>。
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
      <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
      <td>Acoustic Noise</td>
      <td>The payload cannot transmit or generate 35~45KHz band sound waves.
</td>
    </tr>
    <tr>
      <td>Light Source Flashing	</td>
      <td>If the payload is built-in a light source, the light source flashing frequency of the payload cannot be between 0.2 and 50 Hz.</td>
    </tr>
    <tr>
      <td>Light Wave Emission	</td>
      <td>The payload cannot emit light with wavelengths between 600 and 700 nm.</td>
    </tr>
    <tr>
      <td>Magnetic Field</td>
      <td>The payload should minimize magnetic interference, including but not limited to interference created by ferromagnetic substances producing high-intensity alternating magnetic fields.</td>
    </tr>
    <tr>
      <td rowspan="2">Electromagnetic Noise	</td>
      <td>The payload should not transmit electromagnetic waves in the 1 - 1.7 GHz, 2.4 - 2.5 GHz, and 5.8 - 5.9 GHz bands. The equivalent isotropic radiated power (EIRP) of the payload should be less than 1W.</td>
    </tr>
    <tr>
      <td>The payload should not transmit electromagnetic waves in the 1 - 1.7 GHz, 2.3 - 2.6 GHz, and 5.7 - 5.9 GHz bands. The equivalent isotropic radiated power (EIRP) of the payload should be less than 1W.</td>
    </tr>
</tbody>
</table>

## Structural
> **NOTE**
> * To prevent the payload carried on the drone from being affected by the inertia of the drone, impact the battery and the blades, please design the size of the load equipment reasonably;
> * When the weight of the payload is over 600g, please submit the payload to DJI for evaluation.

<table id="PSDK technical integration NOTEs">
  <thead>
    <tr>
      <th>Item</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
      <tr>
      <td>Operation Temperature of the Payload Case</td>
      <td>≤70℃</td>
    </tr>
    <tr>
      <td>Weight</td>
      <td>≤1200g </td>
    </tr>
    <tr>
      <td>Center of Gravity</td>
      <td>＜600g: The center of gravity of the payload should be on thevertical line at the center of the tilt port</br>600g～1200g: The center of gravity of the payload should be on the <b> double gimbal interface Center</b></td>
    </tr>
    <tr>
      <td>Structural Interference</td>
      <td>When the aircraft is in various flight states, the payload can not interfere with the aircraft structure under various working conditions (the propellers shape will change during flight and the payload will have a certain motion lag relative to the aircraft during flight).</td>
    </tr>
    <tr>
      <td>Vibration</td>
      <td>The payload exposure to vibration should be minimized. When the aircraft is turned on, the IMU cannot register as "Moving" on the "Sensors State" page of the DJI PILOT app under various working conditions.</td>
    </tr>
        <tr>
      <td>Trace Path</td>
      <td>The payload should not enter the field of view of the vision sensor, ultrasonic sensor, and infrared sensor under various working conditions. The forward vision sensor has a 75° horizontal field of view and a 60° vertical field of view. The downward vision sensor has a 75° field of view from left to right and a 60° field of view from nose to rear. The ultrasonic sensor has a 100° vertical field of view within a 10 cm range and 70° outside of a 10 cm range. The infrared sensor has a 60° vertical field of view within a 15 cm range, and 20° outside of 15cm.</td>
    </tr>
   </tbody>
</table>

## Data Transmission
##### Use M200 V2 Series

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

##### use M200 Series

> **NOTE:** DJI M200 Series only supports <b>Skyport</b> to transfer the data to Mobile APP, which developed based on MSDK.

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
      <td>ingle Gimbal：≤ 8192Kbps</br>Double Gimbals：other ≤ 4096Kbps</td>
    </tr>
</tbody>    
</table>


## Video
Use PSDK to developed the Payload **must** use the **H.264** standard.

1. The maximum video resolution should small than 1920 × 1080.
2. The maximum frame rate should slowly than 30fps, and the maximum bit rate should small than 8Mbps.
3. The recommended video aspect ratio is 4: 3 (when using DJI CrystalSky, the screen can fill the screen).

>**NOTE:** When using the H.264 encoding standard, the GOP encoding structure must use Period I (intra-frame encoded frames, one IDR frame will be inserted every 1 second to ensure that image data can be recovered if lost).

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

>**Reference:** <a href="https://www.itu.int/rec/T-REC-H.264-201906-I/en">H.264 Protocol</a>



