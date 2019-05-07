---
title: Network Port Guide
date: 2019-01-25
keywords: [introduction]
---

## Network Port Configuration
Configure the network port network properties as below when using the network port to transmit code stream and data:

- IP address: 192.168.5.3
- Subnet mask: 255.255.255.0
- Default gateway: 192.168.5.1

## Downlink Data Transmission
The network port sends downlink data (i.e. from PSDK to MSDK) to the IP 192.168.5.10 and port 23002 by using the UDP protocol

## Video Transmission
The network port sends video stream to the IP 192.168.5.10 and port 23003 by using the UDP protocol.
The requirement of the video stream are as below:

- h264 stream, GOP encoding, I frame interval of 30 with the rest of P frame
- Up to 8KB for sending a single package when using UDP

Developers can refer to the video stream transmission routines (Payload_SDK/sample/network_port).
