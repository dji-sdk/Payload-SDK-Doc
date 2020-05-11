---
title: 时间同步
date: 2020-05-08
version: 2.1.0
keywords: [时间同步]
---
## 概述
时间同步是一个用于同步负载设备时间和无人机时间的功能，PSDK 通过PPS 信号（周期性的脉冲）同步负载设备和**具有RTK 功能的无人机**的时间。具有“时间同步”功能的负载设备，能够方便用户顺利地使用日志排查无人机飞行过程中的各类故障、分析传感器采样的数据以及获取精准的定位信息等功能。

> **本文所指**
>* 无人机时间：无人机系统的时间。
>* 本地时间：负载设备上的时间。

## 时间同步
安装在无人机上的使用PSDK 开发的负载设备在上电后，将初始化时间同步功能模块，消除负载设备和无人机的时钟差，同步负载设备和无人机的时间。
> **说明：** 使用时间同步功能前，请通过移动端APP 确认无人机与RTK 卫星间保持良好的通信状态；该移动端APP 可为DJI 发布的APP，如DJI Pilot，也可为基于MSDK 开发的移动端APP，如 图1.查看卫星通信状态 所示。  
<div>
<div style="text-align: center"><p>图1.查看卫星通信状态 </p>
</div>
<div style="text-align: center"><p><span>
      <img src="../../images/positioning_prerequisites.png" width="500" alt/></span></p>
</div></div>
 
1. 将负载设备安装在无人机的云台上，在无人机上电后，使用PSDK 开发的负载设备将接收到无人机发送的PPS 硬件脉冲信号；
2. 当负载设备检测到PPS 信号的上升沿时，负载设备需要记录负载设备上的本地时间；
3. PSDK 的底层处理程序将获取与PPS 信号同步的无人机系统上的时间。

    > **注意** 
    > * 请确保PPS 信号上升沿到达负载至负载记录本地时间之间的延迟低于1ms。
    > * 请使用硬件中断的形式实现 PPS 信号的响应。
4. PSDK 的底层处理程序将计算负载设备本地的时间与无人机系统时间的时钟差，实现负载设备与无人机系统时间的同步。  
5. 负载设备通过`PsdkTimeSync_TransferToAircraftTime`接口将负载设备本地的时间转换为无人机系统上的时间。

## 使用时间同步功能
#### 1. 配置PPS 引脚参数
为了使PPS 引脚能够正确接收PPS 信号，需要设置PPS 引脚的各项参数，并开启PPS 硬件引脚的功能，接收PPS 时间同步信号。

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

#### 2. 时间同步功能模块初始化
使用时间同步功能，需要初始化时间同步模块。

```c
psdkStat = PsdkTimeSync_Init();
if (psdkStat != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("time synchronization module init error.");
    return psdkStat;
}
```

#### 3. 开发并注册获取负载设备上本地时间的函数
基于PSDK 开发的负载设备在使用时间同步功能时，需要以硬件中断的方式响应无人机推送的PPS 时间同步信号；当最新的PPS 信号被触发时，基于PSDK 开发的负载设备控制程序，需要获取到负载设备本地的时间。

1. 开发并注册硬件中断处理函数      
开发者需要实现硬件中断处理功能，并将处理硬件中断的函数注册到指定的接口中，当负载设备接收到PPS 信号的上升沿时，硬件中断处理函数能够处理PPS 时间同步信号。

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

2. 获取PPS 信号被触发时负载设备的本地时间    
开发者需要实现获取PPS 信号被触发时负载设备上本地时间的功能，并将该功能的函数注册到指定的接口中。当负载设备接收到PPS 信号的上升沿时，基于PSDK 开发的负载设备控制程序能够记录PPS 信号被触发时负载设备上的本地时间。

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

3. 注册获取PPS 信号被触发时负载设备本地时间的函数     
注册获取PPS 信号被触发时负载设备本地时间功能的函数后，需要将该函数注册到负载设备控制程序中，当负载设备接收到PPS 信号的上升沿时，基于PSDK 开发的负载设备控制程序，能够记录PPS 信号被触发时负载设备的本地时间。
 
```c
psdkStat = PsdkTimeSync_RegGetNewestPpsTriggerTimeCallback(s_timeSyncHandler.GetNewestPpsTriggerLocalTimeUs);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("register GetNewestPpsTriggerLocalTimeUsCallback error.");
    return psdkStat;
}
```


#### 4. 时间同步
使用PSDK 开发的负载设备控制程序通过`PsdkOsal_GetTimeMs`获取负载设备上的本地时间并将负载设备上的时间转换为无人机系统的时间。

* 获取负载设备本地的时间

```c
psdkStat = PsdkOsal_GetTimeMs(&currentTimeMs);
if (psdkStat != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("get current time error: %lld.", psdkStat);
    continue;
}
```

* 时间转换      
将负载设备本地的时间转换为无人机系统上的时间。

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

## 适配产品
M210 RTK V2（PPS 信号频率：1Hz）
M300 RTK（PPS 信号频率：1Hz）