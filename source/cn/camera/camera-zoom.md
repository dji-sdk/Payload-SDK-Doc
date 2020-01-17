---
title: 变焦控制功能
date: 2020-01-17
keywords: [相机, 变焦, 光学变焦, 数码变焦, 连续变焦]
---
## 概述
使用PSDK 提供的变焦控制功能，需要开发者**先实现**相机类负载设备的变焦功能，再将变焦功能的函数注册到指定的接口中，用户通过使用DJI Pilot 以及基于MSDK 开发的移动端APP，即可控制使用PSDK 开发的相机类负载设备在**拍照和录像**模式下，通过正确地变焦，获取所需的影像。

## 基础概念

#### 变焦模式
* 光学变焦，通过改变光学镜头的结构实现变焦，光学变焦倍数越大，能拍摄的景物就越远，反之则近；
* 数码变焦，处理器使用特定的算法，通过改变传感器上每个像素的面积，实现数码变焦；    
* 连续变焦，相机类负载设备控制镜头以指定的速度沿指定的方向运动，相机类负载设备先控制镜头执行光学变焦，当光学变焦达到上限后，相机类负载设备再执行数码变焦，以此实现连续变焦的功能。当前变焦倍数=当前光学变焦倍数 × 当前数码变焦倍数；     
* 指点变焦，用户指定某一目标点后，基于PSDK 开发的相机类负载设备能够控制云台转动，使指定的目标处于画面中心，控制相机类负载设备按照预设的变焦倍数放大图像。    

#### 变焦方向
* ZOOM_IN ：变焦倍数减小，图像由远到近
* ZOOM_OUT ：变焦倍数增大，图像由近到远

#### 变焦速度
* SLOWEST：以最慢的速度变焦
* SLOW：以较慢的速度变焦
* MODERATELY_SLOW：以比正常速度稍慢的速度变焦
* NORMAL：镜头以正常的速度变焦
* MODERATELY_FAST：以比正常速度稍快的速度变焦
* FAST：以较快的速度变焦
* FASTEST：以最快的速度变焦

## 实现变焦功能
请开发者根据选用的**开发平台**以及行业应用实际的使用需求，按照PSDK 中的结构体`s_tapZoomHandler`构造实现相机类负载设备变焦功能的函数，将变焦功能的函数注册到PSDK 中指定的接口后，用户通过使用DJI Pilot 或基于MSDK 开发的移动端APP 能够控制相机类负载设备变焦。

```c
    // 实现控制负载设备执行数码变焦的功能
    s_digitalZoomHandler.SetDigitalZoomFactor = SetDigitalZoomFactor;
    s_digitalZoomHandler.GetDigitalZoomFactor = GetDigitalZoomFactor;
    // 实现控制负载设备执行光学变焦的功能
    s_opticalZoomHandler.SetOpticalZoomFocalLength = SetOpticalZoomFocalLength;
    s_opticalZoomHandler.GetOpticalZoomFocalLength = GetOpticalZoomFocalLength;
    s_opticalZoomHandler.GetOpticalZoomFactor = GetOpticalZoomFactor;
    s_opticalZoomHandler.GetOpticalZoomSpec = GetOpticalZoomSpec;
    s_opticalZoomHandler.StartContinuousOpticalZoom = StartContinuousOpticalZoom;
    s_opticalZoomHandler.StopContinuousOpticalZoom = StopContinuousOpticalZoom;
    // 实现控制负载设备执行指点变焦的功能
    s_tapZoomHandler.GetTapZoomState = GetTapZoomState;
    s_tapZoomHandler.SetTapZoomEnabled = SetTapZoomEnabled;
    s_tapZoomHandler.GetTapZoomEnabled = GetTapZoomEnabled;
    s_tapZoomHandler.SetTapZoomMultiplier = SetTapZoomMultiplier;
    s_tapZoomHandler.GetTapZoomMultiplier = GetTapZoomMultiplier;
    s_tapZoomHandler.TapZoomAtTarget = TapZoomAtTarget;
```

## 使用变焦功能
#### 1. 注册变焦功能
开发者实现相机类负载设备的变焦功能后，需要通过注册接口**注册**各个变焦功能的函数；基于PSDK 开发的负载设备通过调用指定的接口，即可控制相机类负载设备执行变焦，方便用户通过使用DJI Pilot 以及基于MSDK 开发的移动端APP 控制相机类负载设备变焦。      

* 注册数码变焦功能
```c
    returnCode = PsdkPayloadCamera_RegDigitalZoomHandler(&s_digitalZoomHandler);
    if (returnCode != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("camera register digital zoom handler error:%lld", returnCode);
        return returnCode;
```

* 注册光学变焦功能
```c
    returnCode = PsdkPayloadCamera_RegOpticalZoomHandler(&s_opticalZoomHandler);
    if (returnCode != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("camera register optical zoom handler error:%lld", returnCode);
        return returnCode;
```

* 注册指点变焦功能
```c
returnCode = PsdkPayloadCamera_RegTapZoomHandler(&s_tapZoomHandler);
if (returnCode != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("camera register tap zoom handler error:%lld", returnCode);
    return returnCode;
}
```

#### 2. 使用数码变焦功能
基于PSDK 开发的负载设备控制程序调用`SetDigitalZoomFactor`和`GetDigitalZoomFactor`接口能够控制负载设备执行数码变焦，用户使用DJI Pilot 以及基于MSDK 开发的移动端APP 能够控制相机类负载设备的执行数码变焦，同时获取负载设备数码变焦的系数。

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

#### 3. 使用光学变焦功能
基于PSDK 开发的负载设备控制程序调用`SetOpticalZoomFocalLength`和`GetOpticalZoomFocalLength`接口能够控制负载设备执行光学变焦，用户使用DJI Pilot 以及基于MSDK 开发的移动端APP 能够控制相机类负载设备执行光学变焦，同时获取负载设备光学变焦的系数。

* 设置光学变焦相机的焦距       

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

* 获取相机类负载设备的变焦系数         
获取相机类负载设备当前的光学焦距后，根据变焦系数的计算公式，能够计算相机类负载设备当前的变焦系数（变焦系数 = 当前焦距 ÷ 最短焦距）。    

```c
    static T_PsdkReturnCode GetOpticalZoomFactor(psdk_f32_t *factor)
    {
        *factor = (psdk_f32_t) s_cameraOpticalZoomFocalLength / ZOOM_OPTICAL_FOCAL_MIN_LENGTH;
        PsdkLogger_UserLogDebug("get optical zoom factor:%.2f", *factor);

        return PSDK_RETURN_CODE_OK;
    }
```

* 获取光学变焦的范围      

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

#### 4. 使用连续变焦功能
基于PSDK 开发的负载设备控制程序调用`StartContinuousOpticalZoom`和`StopContinuousOpticalZoom`接口能够控制负载设备开始或停止执行连续变焦，用户使用DJI Pilot 以及基于MSDK 开发的移动端APP 能够控制相机类负载设备执行连续变焦。

* 控制相机类负载设备开始变焦     
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

* 控制相机类负载设备停止变焦      
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

* 控制相机持续变焦

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

持续按住变焦按钮可改变变焦倍数，如 图1.连续变焦 所示。

* T : 放大焦距（放大变焦倍数）
* W : 缩小焦距（缩小变焦倍数）
* R : 还原相机的焦距
    > **说明：** 根据实际的使用需要，可设置相机类负载设备默认的变焦倍数，当前为1.0。
<div>
<div style="text-align: center"><p>图1.连续变焦 </p>
</div>
<div style="text-align: center"><p><span>
      <img src="../images/camera_zoom_continous.gif" width="500" alt/></span></p>
</div></div>

#### 5. 实现指点变焦功能
当用户开始使用“指点变焦”功能后，使用PSDK 开发的相机类负载设备将根据用户指定的目标点位置以及当前的焦距，先控制云台旋转，将目标对象置于画面中心，再控制负载设备变焦。

##### 通过注册回调函数的方式实现指点变焦功能

* 设置指点变焦的变焦系数     

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

* 获取指点变焦的对象     
使用PSDK 开发的相机类负载设备通过`TapZoomAtTarget`接口获取用户在移动端APP 中指定的变焦对象，在确认指点变焦功能开启后，根据目标点位置和混合焦距，计算云台转动角度，控制相机转动。

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
    //获取指点变焦功能开始的时间
    psdkStat = PsdkOsal_GetTimeMs(&s_tapZoomStartTime);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("get start time error: %lld.", psdkStat);
        errorCode = psdkStat;
        goto err;
    }
    //设置云台相机指点变焦的模式
    rotationMode = PSDK_GIMBAL_ROTATION_MODE_RELATIVE_ANGLE;
    rotationProperty.relativeAngleRotation.actionTime = TAP_ZOOM_DURATION / 10;
    // 控制云台转动
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
    // 设置相机类负载设备云台的转动角度和变焦焦距
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

##### 在线程中实现指点变焦功能
为避免负载设备在旋转云台和控制变焦时，阻塞负载设备控制程序的主线程，请在线程中实现指点变焦功能。

```c
if (s_isTapZooming == true) {
    // 获取指点变焦功能开始的时间
    psdkStat = PsdkOsal_GetTimeMs(&currentTime);
    if (psdkStat != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("get start time error: %lld.", psdkStat);
    }
    // 检查执行指点变焦功能时相机变焦的状态和云台的状态
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