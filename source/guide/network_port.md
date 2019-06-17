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
The requirements of the video stream are as below:

- H.264 stream, recommended interval of I frame of 1 second, without B frame
- Recommended frame rate not exceeding 30 fps
- Non-GDR coding strategy
- Baseline/ Main / High Profiles
- Level Number of less than 5.1
- For other format requirements, please refer to the documentation for the APP and mobile device used
- Up to 8KB for sending a single package when using UDP

Developers can refer to the video stream transmission routines (Payload_SDK/sample/network_port).
