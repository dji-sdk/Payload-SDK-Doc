---
title: Time Synchronization
date: 2020-01-17
version: 2.0.0
keywords: [Time synchronization]
---
> **NOTE:** This article is **machine-translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.

## Overview
Time Synchronization is a function that synchronizes the time in the payload with the time in the drone, PSDK uses the PPS signal (periodic pulse) to synchronize the time between the payload and the drone, which the drone has RTK, the payload with the "Time Synchronization" function is convenient for the user to use the log、analyze the data and Get the accurate positioning information, etc.

> **NOTE**
>* Drone time: The time of the drone system.
>* Local time: The time on the payload.

## Time Synchronization
The payload mounts on the drone which developed based on PSDK will initialize the time synchronization module after powered on, eliminate the time difference between the payload and the drone, and keep the time of the payload and the drone in sync.

> **NOTE:** Before using the time synchronization function, please keep the communication status between the drone and the RTK satellite in the good condition from DJI Pilot or a Mobile APP developed based on MSDK APP, as shown in Figure 1.

<div>
<div style="text-align: center"><p>Figure 1 Communication Status </p>
</div>
<div style="text-align: center"><p><span>
      <img src="../images/positioning_prerequisites.png" width="500" alt/></span></p>
</div></div>
 
1. Mount the payload on the Gimbal, after the drone is powered on, the payload developed based on PSDK will receive the PPS signal sent from the drone.

2. When the payload detects the rising edge of the PPS signal, the payload needs to record the local time on the payload.

3. The program of the payload developed based on PSDK will get the time on the drone system which triggered the PPS signal.
  > **NOTICE** 
  > * Please ensure that the delay of the time, that between the rising edge of the PPS signal to the payload and the payload record the payload time is less than 1ms.
  > * Please use the hardware interrupt to respond to the PPS signal.
4. The program of the payload developed based on PSDK will calculate the clock difference between the local time of the payload and the drone system time to sync.

5. The payload call interface `PsdkTimeSync_TransferToAircraftTime` converts the local time of the payload to the time on the drone system.

## Develop with the Time Synchronization  
#### 1. PPS pin configuration   
It is necessary to set the parameters of the PPS pin and enable the function of the hardware to receive the PPS signal.

```c
T_PsdkReturnCode PsdkTest_PpsSignalResponseInit(void)
{
    GPIO_InitTypeDef GPIO_InitStructure;

    /* Enable GPIOD clock */
    __HAL_RCC_GPIOD_CLK_ENABLE();

    /* Configure pin as input floating */
    GPIO_InitStructure.Mode = GPIO_MODE_IT_RISING;
    GPIO_InitStructure.Pull = GPIO_NOPULL;
    GPIO_InitStructure.Pin = PPS_PIN;
    HAL_GPIO_Init(PPS_PORT, &GPIO_InitStructure);

    /* Enable and set EXTI Line Interrupt to the lowest priority */
    HAL_NVIC_SetPriority(PPS_IRQn, PPS_IRQ_PRIO_PRE, PPS_IRQ_PRIO_SUB);
    HAL_NVIC_EnableIRQ(PPS_IRQn);

    return PSDK_RETURN_CODE_OK;
}
```

#### 2. Initialization
Before using the "Time Synchronization" to develop the payload, the developer needs to initialize the module of the time synchronization with the following code.

```c
psdkStat = PsdkTimeSync_Init();
if (psdkStat != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("time synchronization module init error.");
    return psdkStat;
}
```

#### 3. Develop and register functions to obtain the time of the payload
The payload developed based on PSDK uses the time synchronization function, it needs to respond to the PPS time synchronization signal pushed by the drone with a hardware interrupt. When the latest PPS signal is triggered, the payload control program developed based on PSDK needs to obtain the time of the payload.

1. Develop and register hardware interrupt handle functions    
Developers need to develop and register the function to handle the hardware interrupt in the specified interface. When the payload receives the rising edge of the PPS signal, the function will handle the PPS signal.

```c
void PsdkTest_PpsIrqHandler(void)
{
    T_PsdkReturnCode psdkStat;
    uint32_t timeMs = 0;

    /* EXTI line interrupt detected */
    if (__HAL_GPIO_EXTI_GET_IT(PPS_PIN) != RESET) {
        __HAL_GPIO_EXTI_CLEAR_IT(PPS_PIN);
        psdkStat = Osal_GetTimeMs(&timeMs);
        if (psdkStat == PSDK_RETURN_CODE_OK)
            s_ppsNewestTriggerLocalTimeMs = timeMs;
    }
}
```
2. Get the local time of the payload when the PPS signal is triggered     
The developer needs to develop and register the function to obtain the local time of the payload when the PPS signal is triggered, in the specified interface. When the payload receives the rising edge of the PPS signal, the payload program would record the local time on the payload.

```c
T_PsdkReturnCode PsdkTest_GetNewestPpsTriggerLocalTimeUs(uint64_t *localTimeUs)
{
    if (localTimeUs == NULL) {
        PsdkLogger_UserLogError("input pointer is null.");
        return PSDK_RETURN_CODE_ERR_PARAM;
    }

    if (s_ppsNewestTriggerLocalTimeMs == 0) {
        PsdkLogger_UserLogWarn("pps have not been triggered.");
        return PSDK_RETURN_CODE_ERR_BUSY;
    }

    *localTimeUs = s_ppsNewestTriggerLocalTimeMs * 1000;

    return PSDK_RETURN_CODE_OK;
}
```
3. Register to obtain the function of the payload local time when the PPS signal is triggered     
Register the function that obtains the payload local time when the PPS signal is triggered, after that the payload control program developed based on PSDK can record the local time of the payload when the PPS signal is triggered.

```c
psdkStat = PsdkTimeSync_RegGetNewestPpsTriggerTimeCallback(s_timeSyncHandler.GetNewestPpsTriggerLocalTimeUs);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("register GetNewestPpsTriggerLocalTimeUsCallback error.");
    return psdkStat;
}
```
#### 4. Time Synchronization
The payload program developed based on PSDK use `PsdkOsal_GetTimeMsobtains` to obtain the local time on the payload and synchronize the time with the drone system.
* Get the local time of the payload
```c
psdkStat = PsdkOsal_GetTimeMs(&currentTimeMs);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("get current time error: %lld.", psdkStat);
    continue;
}
```

* Time conversion    
Converts the local time of the payload to the time in the drone system.

```c
psdkStat = PsdkTimeSync_TransferToAircraftTime(currentTimeMs * 1000, &aircraftTime);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("transfer to aircraft time error: %lld.", psdkStat);
    continue;
}

PsdkLogger_UserLogDebug("current aircraft time is %d.%d.%d %d:%d %d %d.", aircraftTime.year, aircraftTime.month,
                        aircraftTime.day, aircraftTime.hour, aircraftTime.minute, aircraftTime.second,
                        aircraftTime.microsecond);
```

## Products
M210 RTK V2 (PPS Period: 1Hz）