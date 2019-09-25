---
title: Payload Coordination
date: 2019-09-23
keywords: [multi, coordination]
---

## Overview

Payload coordination is a working mode，which could meet the special needs of the task. For example, the searchlight and the camera could meet the needs of the night synchronization task for illumination synchronization, the fill light and the zoom camera could meet the inspection task for precise fill light, visible light cameras and spectral cameras could meet the needs of multi-bandwidth imaging for inspection tasks.
  
## Coordination

The payload device developed by the PSDK realizes the action synchronization by receiving the control command; after receiving the synchronizing signal, such as the photographing event, the payload could acquiring the parameters of the main payload to synchronous focus and FOV. The cooperation process is as follows:

* After installing the payload, turn on the remote controller and drone.
* The drone could output a coordinated signal to the load device:
* The main payload receives the control command from the controller and performs the same action;
* The auxiliary payload receives the command or signals implement coordination.

## Command

After users send a control command to the drone, the payload will receive the control command and perform the same action.

* Photo: Use `ShootPhoto` can make payload taking pictures simultaneously.
* Recording: Use `RecordVideo` can make payload taking videos simultaneously.
* Gimbal: Use `ControlAngle` and `ControlJointAngle` to obtain gimbal/tilt angle and joint angle to achieve synchronization.

> **Note**: For detailed description, refer to the API documentation in [PSDK Package](https://developer.dji.com/payload-sdk/downloads/). 

## Signal

After receiving the synchronization signal, the drone will retrieve the model and focal length of the main load device and send it to the auxiliary payload, the auxiliary payload will modify the focus according to the real-time focal length of the main payload. By the device model, the user can get the parameters of the main payload to realize the FOV synchronization.

* Model: Use `otherPayloadTypeMsgCallback` could get the model of main  payload.
* Focal Length: Use `otherPayloadFocalLengthMsgCallback` could get the focal length of the main payload in real time.

## Optimal

* **Only** M210 V2，M210 RTK V2 support action synchronization。
* **Only** M210, M210 RTK，M210 V2, M210 RTK V2 support synchronous zoom。
* The main payload **must** be ZENMUSE XT，ZENMUSE XT2，ZENMUSE X5S，ZENMUSE X7，ZENMUSE Z30，ZENMUSE X4S。

>**NOTE**：Only ZENMUSE X5，ZENMUSE Z30 support synchronous zoom.
