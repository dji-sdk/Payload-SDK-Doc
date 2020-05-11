---
title: 开始使用PSDK 
date: 2020-05-08
version: 2.1.0
keywords: [write apps, developemt, SDK, integrate, DJI]
---

开发者使用PSDK 开发负载设备时，需要引入PSDK 相应功能的头文件、静态库和编译宏。

## 引入PSDK 开发包

#### PSDK 开发包目录结构
* doc：    
    * simple_model：该文件夹包含无人机和负载设备相关的模型文件
    * psdk_other_docs：其他文件，如编码风格说明
* psdk_lib (库与头文件)    
    * api_headers：该文件夹包含各个功能模块的头文件           
    * lib：该文件夹包含不同平台的静态库        
* sample(示例程序)   
    * api_sample：该文件夹包含PSDK 所有功能模块的示例代码。
    * platform：Sample 工程目录，包括编译文件、初始化文件、用户信息配置等。  
* tools：该文件夹包含二进制转头文件工具file2c

#### 引入静态库
开发者需根据所使用的开发平台，在PSDK 开发包`psdk_lib/lib`目录下选择对应平台的静态库。

* Linux    
在Linux 平台上开发负载设备时，需通过修改`CMakeLists.txt` 中的信息，引入静态库`libpayloadsdk.a`。

```c
link_directories(${CMAKE_CURRENT_LIST_DIR}/../../../../../psdk_lib/lib/aarch64-linux-gnu-gcc)                 /*指定静态库的路径*/
link_libraries(${CMAKE_CURRENT_LIST_DIR}/../../../../../psdk_lib/lib/aarch64-linux-gnu-gcc/libpayloadsdk.a)   /*调用静态库*/
```

* RTOS    
在MDK的工程中，将静态库`payloadsdk.lib`添加到工程文件所在的目录下。   

#### 引入头文件
每个头文件对应PSDK 中的一个功能模块，如 `#include "psdk_payload_camera.h"` 对应PSDK的相机功能。
开发者在开发负载设备前，需要引用所需功能的头文件，引用该头文件后，开发者即可调用该头文件中的接口开发所需的功能。     
 * Linux    
在`CMakeLists.txt` 中添加头文件的引用路径`include_directories(../../../../../psdk_lib/api_headers)`后，开发者即可在代码文件中以如下方式引用头文件。
   ```c
   #include "psdk_platform.h"
   #include "platform/osal.h"
   #include "platform/hal_uart.h"
   ```

 * RTOS     
 在MDK的工程配置中添加头文件路径，开发者在添加头文件的路径后，开发者即可在代码文件中以如下方式引用头文件。
   ```c
   #include "psdk_platform.h"
   #include "platform/osal.h"
   #include "platform/hal_uart.h"
   ```


#### 引入编译宏
> **说明：** 请务必在代码开发前添加编译宏。   

Linux 和RTOS 需通过对应的编译宏使能对应平台所特有的功能，使能：1；关闭：0；    
* Linux ：PSDK_ARCH_SYS_LINUX = 1       
* RTOS  ：PSDK_ARCH_SYS_RTOS = 1


## PSDK 初始化
使用PSDK 开发负载设备时，**必须**先注册Platform 模块，再**初始化PSDK 模块**。

#### 1. 注册Platform 模块
通过注册Hal 和Osal 层处理函数，使基于PSDK 开发的负载设备控制程序可移植到其他软硬件平台上。

> **注意：** 在RTOS 系统上开发负载设备时，须在RTOS 操作系统的线程中注册Hal 层和Osal 层函数，确保在调度器工作时可被线程正常调用。


* 注册Hal 层网口函数
通过注册Hal 层网口函数，负载设备控制程序能够通过网口与无人机通信。

```c
T_PsdkReturnCode HalNetWork_Config(const char *ipAddr, const char *netMask)
```

> **说明**
> * 如需[以自动的方式配置负载设备的网络信息](../camera/video-stream-transmission.html)，请使用`PsdkPlatform_RegHalNetworkHandler()`函数适配Hal 层。
> * 仅基于Linux 开发的负载设备支持开发者使用网口与无人机通信，开发者需通过`ifconfig`命令配置或传输配置信息，详情请参见`sample/platform/linux/manifold2/hal/hal_network.c`。


* 注册Hal 层串口函数     
通过注册Hal 层串口设备的函数，负载设备控制程序能够通过开发平台的串口与无人机通信，实现负载设备控制程序在不同硬件平台上的移植。

```c
if (PsdkPlatform_RegHalUartHandler(&halUartHandler) != PSDK_RETURN_CODE_OK) {
    printf("psdk register hal uart handler error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

* 注册Osal 层函数   
通过注册Osal 层的函数，负载设备控制程序能够访问不同操作系统的内核和资源，实现负载设备控制程序在不同操作系统上的移植。

```c
if (PsdkPlatform_RegOsalHandler(&osalHandler) != PSDK_RETURN_CODE_OK) {
    printf("psdk register osal handler error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

> 相关参考：[跨平台移植](../quickstart/porting.html)


#### 2. PSDK 初始化
使用PSDK 开发负载设备时，必须调用`PsdkCore_Init`接口实现PSDK 的初始化，同时请确保操作系统调度器已经运行，否则PSDK 的主线程将无法正常工作。   
> **说明：** 开发者需要向`PsdkCore_Init`接口传入负载设备的信息，详细内容请参见[运行示例程序](../quickstart/run-the-sample.html)中有关补充应用信息的详细说明。

```c
if (PsdkCore_Init(&userInfo) != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("psdk instance init error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

完成PSDK 系统初始化后，开发者可根据使用需求，初始化所需使用的功能。若PSDK 初始化失败，请根据初始化失败的返回码检查负载设备初始化的顺序和对应接口的配置信息。

#### 3. 开始运行应用程序
在完成初始化用户**所有**指定的功能后，<b>必须调用`PsdkCore_ApplicationStart()`接口</b>开始运行PSDK 应用程序，否则移动端的APP 将<b>无法正常</b>控制负载设备；

## 设置别称
使用PSDK 开发的负载设备支持开发者设置负载设备的别称，设置别称后DJI Pilot 或基于MSDK 开发的移动端APP 将显示负载设备的别称。若未设置负载设备的别称，DJI Pilot 或基于MSDK 开发的移动端APP 将显示注册PSDK 应用时设置的名称。

```c
if (PsdkProductInfo_SetAlias("PSDK_APPALIAS") != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("set product alias error.");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```
