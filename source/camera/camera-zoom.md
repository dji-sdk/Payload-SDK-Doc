---
title: Zoom Control 
date: 2020-01-17
version: 2.0.0
keywords: [Camera, Zoom, Optical Zoom, Digital Zoom, Continuous Zoom]
---
> **NOTE:** This article is **machine-translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.

## Overview
Before developing the zoom control for the payload, the developer needs to develop the function by themselves, after registered the function in the specified interfaces of the PSDK, the user uses DJI Pilot and Mobile APP which developed based on MSDK could control the payload to zoom.

## Concepts
#### Zoom Mode
* Optical zoom: the camera-type payload changes the structure of the lens. The larger factor makes the scene will be small.
* Digital zoom: the camera-type payload use the specific algorithm to change the area of ​​each pixel on the sensor.
* Continuous zoom: the camera-type payload control the payload's lens move to the specified direction at the specified speed. The first is optical zoom, then is digital zoom. Multiples = optical zoom multiple × digital zoom multiple;
* Tap zoom: the camera-type payload control the gimble rotate to the specified position make the target is in the center of the screen, and then expend the camera according to the zoom factor that user preset. 

#### Zoom Direction
* ZOOM_IN: The zoom factor decreases and the image moves from far to near.
* ZOOM_OUT: The zoom factor increases and the image moves from near to far.

#### Zoom speed

* SLOWEST: Zoom at the slowest speed
* SLOW: Zoom at a slower speed
* MODERATELY_SLOW: Zoom at a slightly slower speed than normal
* NORMAL: The lens is zoomed at normal speed
* MODERATELY_FAST: Zoom slightly faster than normal
* FAST: Zoom at a faster speed
* FASTEST: Zoom at the fastest speed

## Develop Zoom Control function
According to the development platform and the requirements, developers need to develop the meter control function by themselves refer to the function struct `T_PsdkCameraDigitalZoomHandler`、`T_PsdkCameraOpticalZoomHandler` and `T_PsdkCameraTapZoomHandler`, after register the functions to the interface in the PSDK, User use DJI Pilot or Mobile APP developed based on MSDK could control the payload to zoom.

```c
    // Developed the fuction that control the camera-type payload to zoom(digital).
    s_digitalZoomHandler.SetDigitalZoomFactor = SetDigitalZoomFactor; 
    s_digitalZoomHandler.GetDigitalZoomFactor = GetDigitalZoomFactor; 
    // Developed the fuction that control the camera-type payload to zoom(optical).
    s_opticalZoomHandler.SetOpticalZoomFocalLength = SetOpticalZoomFocalLength; 
    s_opticalZoomHandler.GetOpticalZoomFocalLength = GetOpticalZoomFocalLength; 
    s_opticalZoomHandler.GetOpticalZoomFactor = GetOpticalZoomFactor; 
    s_opticalZoomHandler.GetOpticalZoomSpec = GetOpticalZoomSpec; 
    s_opticalZoomHandler.StartContinuousOpticalZoom = StartContinuousOpticalZoom; 
    s_opticalZoomHandler.StopContinuousOpticalZoom = StopContinuousOpticalZoom; 
    // Developed the fuction that control the camera-type payload to zoom(tap zoom).
    s_tapZoomHandler.GetTapZoomState = GetTapZoomState;
    s_tapZoomHandler.SetTapZoomEnabled = SetTapZoomEnabled;
    s_tapZoomHandler.GetTapZoomEnabled = GetTapZoomEnabled;
    s_tapZoomHandler.SetTapZoomMultiplier = SetTapZoomMultiplier;
    s_tapZoomHandler.GetTapZoomMultiplier = GetTapZoomMultiplier;
    s_tapZoomHandler.TapZoomAtTarget = TapZoomAtTarget;
```

## Develop with the Zoom Control
#### 1. Register the Zoom Control function
After develope the zoom control function of the camera-type payload, the developer needs to register the zoom control function in the specified interface, so that the user uses DJI Pilot and Mobile APP developed based on MSDK could control the camera-type payload to zoom.

* Registered the digital zoom function
```c
    returnCode = PsdkPayloadCamera_RegDigitalZoomHandler(&s_digitalZoomHandler);
    if (returnCode != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("camera register digital zoom handler error:%lld", returnCode);
        return returnCode;
```

* Registered the optical zoom function
```c
    returnCode = PsdkPayloadCamera_RegOpticalZoomHandler(&s_opticalZoomHandler);
    if (returnCode != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("camera register optical zoom handler error:%lld", returnCode);
        return returnCode;
```

* Registered the tap zoom function

```c
returnCode = PsdkPayloadCamera_RegTapZoomHandler(&s_tapZoomHandler);
if (returnCode != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("camera register tap zoom handler error:%lld", returnCode);
    return returnCode;
}
```

#### 2. Develop with the Digital Zoom function
The program of the payload which developed based on PSDK uses the interface `SetDigitalZoomFactor` and `GetDigitalZoomFactor` to set the zoom factor of the payload, and user use DJI Pilot or Mobile APP developed based on MSDK could get the zoom factor from the payload and control the payload zoom.

```c
    static T_PsdkReturnCode SetDigitalZoomFactor(psdk_f32_t factor)
    {
        PsdkLogger_UserLogDebug("set digital zoom factor:%.2f", factor);
        s_cameraDigitalZoomFactor = factor;

        return PSDK_RETURN_CODE_OK;
    }

    static T_PsdkReturnCode GetDigitalZoomFactor(psdk_f32_t *factor)
    {
        *factor = s_cameraDigitalZoomFactor;
        PsdkLogger_UserLogDebug("get digital zoom factor:%.2f", *factor);

        return PSDK_RETURN_CODE_OK;
    }
```

#### 3. Develop with the Optical Zoom function
The program of the payload which developed based on PSDK uses the interface `SetOpticalZoomFocalLength` and `GetOpticalZoomFocalLength` to control the payload Optical the zoom, and the user uses DJI Pilot or Mobile APP developed based on MSDK could get the zoom factor from the payload and control the payload zoom.

* Set the focal length of the camera-type payload       

```C
    static T_PsdkReturnCode SetOpticalZoomFocalLength(uint32_t focalLength)
    {
        PsdkLogger_UserLogDebug("set optical zoom focal length:%d", focalLength);
        s_cameraOpticalZoomFocalLength = focalLength;

        return PSDK_RETURN_CODE_OK;
    }

    static T_PsdkReturnCode GetOpticalZoomFocalLength(uint32_t *focalLength)
    {
        *focalLength = s_cameraOpticalZoomFocalLength;
        PsdkLogger_UserLogDebug("get optical zoom focal length:%d", *focalLength);

        return PSDK_RETURN_CODE_OK;
    }
```

* Get the focal factor of the camera-type payload           
Zoom factor = zoom focal length ÷ shortest focal length

```c
    static T_PsdkReturnCode GetOpticalZoomFactor(psdk_f32_t *factor)
    {
        *factor = (psdk_f32_t) s_cameraOpticalZoomFocalLength / ZOOM_OPTICAL_FOCAL_MIN_LENGTH;
        PsdkLogger_UserLogDebug("get optical zoom factor:%.2f", *factor);

        return PSDK_RETURN_CODE_OK;
    }
```

* Get the range of optical zoom     

```c
    static T_PsdkReturnCode GetOpticalZoomSpec(T_PsdkCameraOpticalZoomSpec *spec)
    {
        spec->maxFocalLength = ZOOM_OPTICAL_FOCAL_MAX_LENGTH;
        spec->minFocalLength = ZOOM_OPTICAL_FOCAL_MIN_LENGTH;
        spec->focalLengthStep = ZOOM_OPTICAL_FOCAL_LENGTH_STEP;

        PsdkLogger_UserLogDebug("get optical zoom spec Max:%d Min:%d Step:%d", spec->maxFocalLength, spec->minFocalLength,
                                spec->focalLengthStep);
        return PSDK_RETURN_CODE_OK;
    }
```

#### 4. Develop with the Continue Zoom function
The program of the payload which developed based on PSDK use the interface `StartContinuousOpticalZoom` and `StopContinuousOpticalZoom` to start and stop the payload to zoom continuously, and user use DJI Pilot or Mobile APP developed based on MSDK could control the payload start or stop the payload to zoom.

* Start the camera-type payload to zoom     

```c
    static T_PsdkReturnCode StartContinuousOpticalZoom(E_PsdkCameraZoomDirection direction, E_PsdkCameraZoomSpeed speed)
    {
        PsdkLogger_UserLogDebug("start continuous optical zoom direction:%d speed:%d", direction, speed);
        s_isStartContinuousOpticalZoom = true;
        s_cameraZoomDirection = direction;
        s_cameraZoomSpeed = speed;

        return PSDK_RETURN_CODE_OK;
    }
```

* Stop the camera-type payload zoom   
```c
    static T_PsdkReturnCode StopContinuousOpticalZoom(void)
    {
        PsdkLogger_UserLogDebug("stop continuous optical zoom");
        s_isStartContinuousOpticalZoom = false;
        s_cameraZoomDirection = PSDK_CAMERA_ZOOM_DIRECTION_OUT;
        s_cameraZoomSpeed = PSDK_CAMERA_ZOOM_SPEED_NORMAL;

        return PSDK_RETURN_CODE_OK;
    }
```

* Control the camera to zoom continuously 

```c
    if (cnt % 10 == 0) {
        if (s_isStartContinuousOpticalZoom == true) {
            tempFocalLength = s_cameraOpticalZoomFocalLength;
            if (s_cameraZoomDirection == PSDK_CAMERA_ZOOM_DIRECTION_IN) {
                tempFocalLength += ((int) s_cameraZoomSpeed - PSDK_CAMERA_ZOOM_SPEED_SLOWEST + 1) *
                                   ZOOM_OPTICAL_FOCAL_LENGTH_CTRL_STEP;
            } else if (s_cameraZoomDirection == PSDK_CAMERA_ZOOM_DIRECTION_OUT) {
                tempFocalLength -= ((int) s_cameraZoomSpeed - PSDK_CAMERA_ZOOM_SPEED_SLOWEST + 1) *
                                   ZOOM_OPTICAL_FOCAL_LENGTH_CTRL_STEP;
            }
            if (tempFocalLength > ZOOM_OPTICAL_FOCAL_MAX_LENGTH) {
                tempFocalLength = ZOOM_OPTICAL_FOCAL_MAX_LENGTH;
            }
            if (tempFocalLength < ZOOM_OPTICAL_FOCAL_MIN_LENGTH) {
                tempFocalLength = ZOOM_OPTICAL_FOCAL_MIN_LENGTH;
            }
            s_cameraOpticalZoomFocalLength = (uint16_t) tempFocalLength;
        }
    }
```

Press and hold the zoom button to change the zoom factor, as shown in Figure 1. 


* T: zoom increases
* W: zoom decreases
* R: zoom resets
    > **NOTE:** User could set the default zoom factor of the camera-type payload,the current is 1.0.
<div>
<div style="text-align: center"><p>Figure 1 Zoom Continuously </p>
</div>
<div style="text-align: center"><p><span>
      <img src="../images/camera_zoom_continous.gif" width="500" alt/></span></p>
</div></div>

#### 5. Develop with the Tap Zoom 
The tap zoom function control the gimble rotated to the target position and uses the current focal length to make the object in the center of the screen.

##### Developed in the callback function

* Set the zoom factor      

```c
static T_PsdkReturnCode SetTapZoomMultiplier(uint8_t multiplier)
{
    PsdkLogger_UserLogDebug("set tap zoom multiplier: %d.", multiplier);
    s_tapZoomMultiplier = multiplier;
    return PSDK_RETURN_CODE_OK;
}

static T_PsdkReturnCode GetTapZoomMultiplier(uint8_t *multiplier)
{
    *multiplier = s_tapZoomMultiplier;
    return PSDK_RETURN_CODE_OK;
}
```

* Get the object     
The camera-type payload uses the `TapZoomAtTarget` to receive the object from the Mobile APP, and then calculate the rotation angle of the gimbal according to the target position and the hybrid focal length.

```c
static T_PsdkReturnCode TapZoomAtTarget(T_PsdkCameraPointInScreen target)
{
    T_PsdkReturnCode psdkStat;
    T_PsdkReturnCode errorCode;
    E_PsdkGimbalRotationMode rotationMode;
    T_PsdkGimbalRotationProperty rotationProperty = {0};
    T_PsdkAttitude3d rotationValue = {0};
    float equivalentFocalLength = 0; // unit: 0.1mm

    PsdkLogger_UserLogDebug("tap zoom at target: x %f, y %f.", target.focusX, target.focusY);

    if (s_isTapZoomEnabled != true) {
        PsdkLogger_UserLogWarn("tap zoom is not enabled.");
        return PSDK_RETURN_CODE_ERR_SYSTEM;
    }
    // Get the start time.
    psdkStat = PsdkOsal_GetTimeMs(&s_tapZoomStartTime);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("get start time error: %lld.", psdkStat);
        errorCode = psdkStat;
        goto err;
    }
    // set the gimbal mode.
    rotationMode = PSDK_GIMBAL_ROTATION_MODE_RELATIVE_ANGLE;
    rotationProperty.relativeAngleRotation.actionTime = TAP_ZOOM_DURATION / 10;
    // Ratate the gimbal.
    equivalentFocalLength = s_cameraOpticalZoomFocalLength * s_cameraDigitalZoomFactor;
    rotationValue.pitch = (int32_t) (
        atan2f((target.focusY - CENTER_POINT_IN_SCREEN_Y_VALUE) * IMAGE_SENSOR_Y_SIZE, equivalentFocalLength) * 1800 /
        PI);
    rotationValue.yaw = (int32_t) (
        atan2f((target.focusX - CENTER_POINT_IN_SCREEN_X_VALUE) * IMAGE_SENSOR_X_SIZE, equivalentFocalLength) * 1800 /
        PI);

    psdkStat = PsdkOsal_MutexLock(s_tapZoomMutex);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("lock tap zoom mutex error: %lld.", psdkStat);
        errorCode = psdkStat;
        goto err;
    }
    // Set the angle and focal length.
    s_tapZoomNewestGimbalRotationArgument.rotationMode = rotationMode;
    s_tapZoomNewestGimbalRotationArgument.rotationProperty = rotationProperty;
    s_tapZoomNewestGimbalRotationArgument.rotationValue = rotationValue;
    s_tapZoomNewestTargetFocalLength = (uint32_t) (equivalentFocalLength * s_tapZoomMultiplier);
    s_isTapZooming = true;
    
    PsdkOsal_SemaphoreTimedWait(s_tapZoomSem, 0);
    psdkStat = PsdkOsal_SemaphorePost(s_tapZoomSem);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("post semaphore of gimbal rotation error: %lld.", psdkStat);
        errorCode = psdkStat;
        goto err;
    }

    psdkStat = PsdkOsal_MutexUnlock(s_tapZoomMutex);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("unlock tap zoom mutex error: %lld.", psdkStat);
        errorCode = psdkStat;
        goto err;
    }

    return PSDK_RETURN_CODE_OK;

err:
    s_isTapZooming = false;
    return errorCode;
}
```

##### Developed in the thread
To avoid blocking the main thread of the payload control program please develop the tap zoom function in the thread.

```c
if (s_isTapZooming == true) {
    // Get the start time.
    psdkStat = PsdkOsal_GetTimeMs(&currentTime);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("get start time error: %lld.", psdkStat);
    }
    // Check the gimbal status
    if ((currentTime - s_tapZoomStartTime) >= TAP_ZOOM_DURATION) {
        s_cameraTapZoomState.zoomState = PSDK_CAMERA_TAP_ZOOM_STATE_IDLE;
        s_cameraTapZoomState.isGimbalMoving = false;
        s_isTapZooming = false;
    }

    psdkStat = PsdkOsal_MutexLock(s_tapZoomMutex);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("lock tap zoom mutex error: %lld.", psdkStat);
    }

    psdkStat = PsdkOsal_SemaphoreTimedWait(s_tapZoomSem, 0);
    if (psdkStat == PSDK_RETURN_CODE_OK) {
        psdkStat = PsdkTest_CameraRotationGimbal(s_tapZoomNewestGimbalRotationArgument);
        if (psdkStat != PSDK_RETURN_CODE_OK)
            PsdkLogger_UserLogError("rotate gimbal error: %lld.", psdkStat);
        else
            s_cameraTapZoomState.isGimbalMoving = true;

        psdkStat = PsdkTest_CameraHybridZoom(s_tapZoomNewestTargetFocalLength);
        if (psdkStat == PSDK_RETURN_CODE_OK) {
            s_cameraTapZoomState.zoomState = s_tapZoomNewestTargetFocalLength >
                                             (s_cameraOpticalZoomFocalLength * s_cameraDigitalZoomFactor)
                                             ? PSDK_CAMERA_TAP_ZOOM_STATE_ZOOM_IN
                                             : PSDK_CAMERA_TAP_ZOOM_STATE_ZOOM_OUT;
        } else if (psdkStat == PSDK_RETURN_CODE_ERR_OUT_OF_RANGE) {
            PsdkLogger_UserLogError("hybrid zoom focal length beyond limit.");
            s_cameraTapZoomState.zoomState = PSDK_CAMERA_TAP_ZOOM_STATE_ZOOM_LIMITED;
        } else {
            PsdkLogger_UserLogError("hybrid zoom error: %lld.", psdkStat);
        }
    }

    psdkStat = PsdkOsal_MutexUnlock(s_tapZoomMutex);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("unlock tap zoom mutex error: %lld.", psdkStat);
    }
}
```

