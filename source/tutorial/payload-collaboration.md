---
title: Payload Coordination
date: 2020-05-08
version: 2.1.0
keywords: [Payload Coordination]
---
> **NOTE** This article is **Machine-Translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.

## Overview
Payload coordination is a mode of controlling multiple payloads to work, searchlights and cameras in coordination could meet the needs of nighttime search; supplementary lights and zoom cameras in coordination could meet the needs of inspection tasks; the visible light camera and the spectrum camera in coordination could meet the needs of the detection task.

> **NOTE** Using DJI Pilot could control the payload in coordination,for details please refer to the <a href="https://www.dji.com/cn/matrice-200-series-v2/info#downloads" target="_blank" rel="external">User's Manual</a> or DJI Pilot.

## Develop with the Payload Coordination
The payload on the Gambal could obtain the information of others，such as camera type、focal length and zoom data, etc.

> **NOTE** 
> * Please mount the payload which developed based on PSDK on the Gimbal Ⅱ, and the Gimbal I only support mount the specified <a href="#t01">payload</a>.
> * If the payload which developed based on PSDK already has the functions of taking pictures, recording and Gambal control, the payload has the coordination function.
> * This tutorial introduces how to develop the payload coordination (coordinated zoom) by using the camera's type.

#### 1. Initialization
Before using the "Payload Coordination" to develop the payload, developer need to initialize the module of the payload coordination with the following code.

```c
if (PsdkPayloadCollaboration_Init() != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("payload collaboration module init error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

#### 2. Obtain the information of the payload

* Obtain the type of the payload

```
psdkStat = PsdkPayloadCollaboration_GetCameraTypeOfPayload(requestedPayloadMountPosition, &cameraType);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    continue;
}
PsdkLogger_UserLogDebug("camera type of payload mounted on NO.%d gimbal connector is %d.",
                        requestedPayloadMountPosition, cameraType);
```

* Obtain the zoom of the camera's payload

```c
psdkStat = PsdkPayloadCollaboration_GetCameraOpticalZoomSpecOfPayload(requestedPayloadMountPosition,
                                                                      &cameraOpticalZoomSpec);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    continue;
}
PsdkLogger_UserLogDebug(
    "camera optical zoom specification of payload mounted on NO.%d gimbal connector, maxFocalLength: %d, minFocalLength: %d, focalLengthStep: %d.",
    requestedPayloadMountPosition, cameraOpticalZoomSpec.maxFocalLength,
    cameraOpticalZoomSpec.minFocalLength, cameraOpticalZoomSpec.focalLengthStep);
```

* Obtain the focal length of the camera's payload

```c
psdkStat = PsdkPayloadCollaboration_GetCameraHybridZoomFocalLengthOfPayload(requestedPayloadMountPosition,
                                                                            &cameraHybridZoomFocalLength);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    continue;
}
PsdkLogger_UserLogDebug(
    "camera hybrid zoom focal length of payload mounted on NO.%d gimbal connector, focalLength: %d.",
    requestedPayloadMountPosition, cameraHybridZoomFocalLength);
```


<div>
<div style="text-align: center"><p> Figure 1 The parameters of the payload </p>
</div>
<div style="text-align: center"><p><span>
      <img src="../images/payload_collaboration_camera_info_push.png" width="500" alt/></span></p>
</div></div>

## Products
<table id="t01">
  <thead>
    <tr>
      <th>Function</th>
      <th>Sync Control</th>
      <th>Sync Zoom</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Products </th>
      <td>M210 V2、M210 RTK V2、M300 RTK</td>
      <td>M210、M210 RTK、M210 V2、M210 RTK V2、M300 RTK</td>
    </tr>
    <tr>
      <th>DJI‘s Payload</th>
      <td>ZENMUSE XT、ZENMUSE XT2;</br>ZENMUSE X7、ZENMUSE Z30;</br>ZENMUSE X4S、ZENMUSE X5S、ZENMUSE XT S;</br>ZENMUSE H20、ZENMUSE H20T</td>
      <td>ZENMUSE XT2、ZENMUSE X4S;</br>ZENMUSE X5S、ZENMUSE X7ZENMUSE Z30;</br>ZENMUSE H20、ZENMUSE H20T</td>
    </tr>
  </tbody>
</table>

> **NOTE** Only Matrice 300 RTK supports ZENMUSE H20 and ZENMUSE H20T.