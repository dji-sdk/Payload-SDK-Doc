---
title: Attention
date: 2020-05-08
version: 2.1.0
keywords: [attention, hardware purchase, software version, firmware version]
---
> **NOTE** 
> * This article is **Machine-Translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.
> * This series of documentation introduces the functions of PSDK V2.x.x, as well as the steps and methods of developing payloads using PSDK V2.x.x. If you are still using PSDK V 1.5.x, please download the documentation of [PSDK V1.5.x](https://terra-1-g.djicdn.com/71a7d383e71a4fb8887a310eb746b47f/psdk/payload-sdk-doc-1.0.zip).

Before using PSDK to develop payloads, please read this document carefully to avoid improper operation and accidental damage to the aircraft, hardware platform or payloads.

## Firmware Upgrade
Before to develop the payload，please use **DJI Assistant 2** to upgrade the firmware of the drone and hardware platform, for details please refer to[Firmware Release](../appendix/firmware.html)。

> **NOTE**
> * X-Port and Skyport V2 only support **PSDK V2.x.x**.
> * Skyport only supports **PSDK V1.x.x**.
> * DJI recommended developers use **PSDK V2.xx** with **X-Port** or **Skyport V2** to develop payload.
> * If you still use **PSDK V1.xx** and **Skyport** to develop payload, please download the documentation of [PSDK V1.5.X](https://terra-1-g.djicdn.com/71a7d383e71a4fb8887a310eb746b47f/psdk/payload-sdk-doc-1.0.zip).

## Development and testing
When using PSDK to develop payload, to protect developers from accidents, please note the following:
* When using PSDK to develop payload or testing payload based on PSDK, please remove the blades on the drone;
* When the UAV motor is rotating, please do not get close;
* Do not input high-power current to the power output interface of the drone;


## Disclaimer
* Before using the payload developed by PSDK, please check the laws and regulations of the area where the flight is located, **The safety issues or legal disputes caused by the use of PSDK are not related to DJI, and DJI does not assume any responsibility for using PSDK.**.
* When using the payload developed by PSDK to perform tasks, please follow the instructions in the aircraft user manual to ensure that the aircraft is in good flight status when performing the task, reducing potential safety hazards and the possibility of safety accidents.
* **DJI will not obtain private data of third-party users in any way and for any reason.** Developers should develop **functions to protect user privacy data, such as data encryption and confusion when using PSDK.** DJI will not bear any legal responsibility for the leakage of user ’s privacy data.