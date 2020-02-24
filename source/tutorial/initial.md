---
title:  PSDK Initialization
date: 2020-01-17
version: 2.0.0
keywords: [Payload SDK, PSDK, initialization, RTOS, Porting]
---
> **NOTE:** This article is **machine-translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.

The first step to develop the payload which based on PSDK is Platform module initial and PSDK initial.

## 1. Register the Platform module
After register the Hal and Osal, the program of the payload developed based on PSDK could be ported to other platforms.

> **NOTICE：** If you developed the payload on RTOS, you must register the Hal and Osal in the RTOS operating system thread and ensure that the thread can be called normally when the scheduler works.

* Hal Register   
Register the Hal could help the payload port to other hardware platforms.

```c
if (PsdkPlatform_RegHalUartHandler(&halUartHandler) != PSDK_RETURN_CODE_OK) {
    printf("psdk register hal uart handler error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

* Osal Register   
Register the Osal could help the payload port to other development platforms.

```c
if (PsdkPlatform_RegOsalHandler(&osalHandler) != PSDK_RETURN_CODE_OK) {
    printf("psdk register osal handler error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

> Reference: [Port](./Porting.html)

## 2. PSDK Initialization
To develop the payload based on the PSDK, you must initialize the PSDK with the following code.please ensure that the operating system scheduler is running, otherwise, the main thread of the PSDK couldn't work.
>**NOTE:** Developer needs to pass the application information to the interface, for details, please see [“2. Add the user’s information”](workflow/run-the-sample.html).

```c
if (PsdkCore_Init(&userInfo) != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("psdk instance init error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

>**NOTE** 
> * After initialized the PSDK, developer could initialize the function which developed.
> * After initialized all the functions, developer must call the `PsdkCore_ApplicationStart()` to start the function, otherwise, the Mobile APP cannot control the payload.
> * If the initialization is failed, please check the initialization sequence of the payload and the configuration of the corresponding interface according to the return code.

## Set The Nickname
The payload developed based on PSDK supports developer to set the nickname name for the payload, if not, DJI Pilot or Mobile APP developed based on MSDK will display the name which was registered in the [User Center](https://developer.dji.com/user/apps/#all).

```c
if (PsdkProductInfo_SetAlias("PSDK_APPALIAS") != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("set product alias error.");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```
