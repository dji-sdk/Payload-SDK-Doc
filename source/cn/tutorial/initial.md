---
title: PSDK 初始化
date: 2020-01-17
version: 2.0.0
keywords: [Payload SDK, PSDK, 初始化, RTOS, 移植, 别名]
---
使用PSDK 开发负载设备时，**必须**先注册Platform 模块，再**初始化PSDK 模块**。

## 1. 注册Platform 模块
通过注册Hal 和Osal 层处理函数，使基于PSDK 开发的负载设备控制程序可移植到其他软硬件平台上。

> **注意：** 在RTOS 系统上开发负载设备时，须在RTOS 操作系统的线程中注册Hal 层和Osal 层函数，确保在调度器工作时可被线程正常调用。

* 注册Hal 层函数     
通过注册Hal 层函数，使负载设备控制程序能够移植到其他硬件平台上。

```c
if (PsdkPlatform_RegHalUartHandler(&halUartHandler) != PSDK_RETURN_CODE_OK) {
    printf("psdk register hal uart handler error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

* 注册Osal 层函数   
通过注册Osal 层函数，使负载设备控制程序能够移植到其他开发平台上。

```c
if (PsdkPlatform_RegOsalHandler(&osalHandler) != PSDK_RETURN_CODE_OK) {
    printf("psdk register osal handler error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

> 相关参考：[跨平台移植](./Porting.html)

## 2. PSDK 初始化
使用PSDK 开发负载设备时，必须调用`PsdkCore_Init`接口实现PSDK 的初始化，同时请确保操作系统调度器已经运行，否则PSDK 的主线程将无法正常工作。   
>**说明：** 开发者需要向`PsdkCore_Init`接口传入应用信息，详细内容请参见[“2.补充应用信息”](../workflow/run-the-sample.html).

```c
if (PsdkCore_Init(&userInfo) != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("psdk instance init error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

>**说明** 
> * PSDK 系统初始化完成后，用户可根据使用需求选择指定的功能执行初始化；
> * 用户指定的**所有**功能初始化完成后，<b>必须调用`PsdkCore_ApplicationStart()`接口</b>开始PSDK 应用程序的运行，否则移动端的APP 将<b>无法正常</b>控制负载设备；
> * 若PSDK 初始化失败，请根据初始化失败的返回码检查负载设备初始化的顺序和对应接口的配置信息。

## 设置负载设备别称
使用PSDK 开发的负载设备支持开发者设置负载设备的别称，设置别称后DJI Pilot 或基于MSDK 开发的移动端APP 将显示负载设备的别称。若未设置负载设备的别称，DJI Pilot 或基于MSDK 开发的移动端APP 将显示注册PSDK 应用时设置的名称。

```c
if (PsdkProductInfo_SetAlias("PSDK_APPALIAS") != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("set product alias error.");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```
