---
title: Payload SDK Feature Introduction
date: 2018-03-28
keywords: [introduction, overview, Payload SDK]
---

## System Block Diagram

![](../images/introduction/psdk_introduction/system_block.png)

## Features Overview

Click on the links in the following table to see more details about each feature.

| Features                                                                                       | Description                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Direct Data Transmission](data-transmission.html#direct-data-transmission-UART-CAN)           | Transmit data directly between Mobile SDK and SKYPORT via UART/CAN port                                                                                                                |
| [Network Stream Data Transmission](data-transmission.html#network-stream-data-transmission-udp)| UDP protocol is used when transmit a large number of downlink data via the network port. Mobile SDK provides stream analysis when transmitting the code stream in the specified format |
| [Vehicle State Push Data](aircraft-state-push-data.html)                                       | Push UAV status data to the payload, including GPS information, attitude information, app time and so on                                                                           |
| [Camera & Gimbal Payload Support](camera-gimbal-features.html)                       | Payload SDK provides a set of camera & gimbal interface for user to quick develop a camera & gimbal payload                                                                                                                                             |
| [Mobile SDK Support](integrate-other-dji-sdk-apps.html#mobile-sdk-support)                     | Mobile SDK provides PSDK interface support                                                                                                                                             |
| [DJI Pilot Support](integrate-other-dji-sdk-apps.html#dji-pilot-support)                       | DJI Pilot provides PSDK interface support                                                                                                                                              |

