---
title: Payload SDK Features - Data Transmission
date: 2018-03-28
keywords: [introduction, overview, Payload SDK]
---

## Direct Data Transmission (UART/CAN)


The direct data transmission feature allows you to send custom data streams between your payload and the Mobile SDK. 

- This channel accepts data on UART/CAN from the payload
- The channel does not enforce any protocols on the data; it will transparently transmit bytes between the PSDK and the MSDK.
- It allows the developer to develop protocols for interpreting this data on the MSDK.
- This feature is analogous to the [Data Transparent Transmission](https://developer.dji.com/onboard-sdk/documentation/guides/component-guide-mobile-communication.html) feature of the Onboard SDK.
 
#### Data Bandwidth Considerations
Transmit data directly between Mobile SDK and SKYPORT via UART/CAN port within the following bandwidth:

<table id="t01">
  <thead>
    <tr>
      <th>Link</th>
      <th>Indicators</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Uplink (form Mobile SDK to Payload)</th>
      <td>Approx. 500B/s on M200</td>        
    </tr>
    <tr>
      <td>Downlink (from Payload to Mobile SDK)</th>
      <td>Approx. 3KB/s on M200</td>        
    </tr>
  </tbody>
</table>


## Network Stream Data Transmission (UDP)

The network stream transmission feature allows the payload to publish high speed bulk data to a network port through UDP. This data is then sent transparently to the Mobile SDK.

#### Video Data Transmission
- The network stream channel greatly simplifies video transmission by providing native video decoding and display in the Mobile SDK, without requiring any coded development on the MSDK.
- To take advantage of this feature, your payload must encode your video data into a specific format and send it to a specific port (the details are given below).
- If your video data is correctly formatted, all of DJI's iOS and Android applications that use the MSDK will be able to display this video with no code changes.
- This also allows backward compatibility with existing mobile applications, as well as greatly enhancing interoperability with DJI cameras and gimbals.

#### Non-Video Data Transmission
- If you are interested in transmitting high speed bulk data that isn't video, the PSDK also gives you that option.
- Your payload can send any data over UDP to a different network port than the video network port, and you need to implement decoding on the Mobile SDK app to parse this data.

#### Network Port Bandwidth Considerations
The bandwidth information of network port data transmission is provided as follows:

<table id="t01">
  <thead>
    <tr>
      <th>Usage condition</th>
      <th>Total bandwidth (downlink data + code stream)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M200 series aircraft with the third-party payload only.</th>
      <td>The maximum theoretical bandwidth is 8Mbps.</td>        
    </tr>
    <tr>
      <td>M210 or M210 RTK, with both DJI camera and the third-party payload.</th>
      <td>The maximum theoretical bandwidth is 4Mbps.</td>        
    </tr>
  </tbody>
</table>


## Comparison : Direct Data Transmission v/s Network Stream Data Transmission

- Usually, for small amount of data, use the direct data transmission link.
- The network link offers higher bandwidth, but this comes at the cost of additional overhead since you need to pack your data into UDP packets.
- For video transmission, the network stream is the better choice
- If you require reliable data transmission, prefer the direct data link over the best-effort UDP channel.