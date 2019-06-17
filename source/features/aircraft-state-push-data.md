---
title: Payload SDK Features - Aircraft State Push Data
date: 2019-06-17
keywords: [introduction, overview, Payload SDK]
---

### Push Data Description

The Payload SDK provides access to some real-time information about the aircraft's state. Here are some examples of how this information can be used by your payload:

- For camera payloads, you can record the GPS position of the aircraft at the time a picture was taken and store it as metadata
- For camera/gimbal payloads, you can record the attitude of the aircraft and use it to rotate the picture in use cases which demand absolute position and orientation
- You can monitor the battery levels and turn off some functionality of the payload when the aircraft battery drops below a certain level


### Push Data Details
Payload SDK provides access to aircraft state, referring to the Payload SDK API manual for details. 

Currently, the following push data is supported:

<table id="t01">
  <thead>
    <tr>
      <th>Status</th>
      <th>Maximum push frequency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> Data Communication status (including video transmission bandwidth)</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>Flight attitude</th>
      <td>50Hz</td>        
    </tr>
    <tr>
      <td>Battery status</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>GPS data</th>
      <td>1Hz (M200 Series), 10Hz (M200 Series V2)</td>        
    </tr>
    <tr>
      <td>GPS raw data</th>
      <td>5Hz</td>        
    </tr>
    <tr>
      <td>Altitude data</th>
      <td>50Hz</td>        
    </tr>
    <tr>
      <td>Flight status</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>App time and date push</th>
      <td>1Hz</td>        
    </tr>
    <tr> 
      <td>RTK raw data</th>
      <td>20Hz</td>        
    </tr>
  </tbody>
</table>
