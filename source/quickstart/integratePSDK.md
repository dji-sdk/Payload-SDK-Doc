---
title: Start to use PSDK 
date: 2020-05-08
version: 2.1.0
keywords: [write apps, developemt, SDK, integrate, DJI]
---

Using PSDK to develop the payload please include the header files, static libraries and compiled define  of the corresponding functions of PSDK.

## Include the PSDK

#### Directory structure

* doc:    
    * simple_model: the simple module of the drone and the payload
    * psdk_other_docs:other files such as Coding style
* psdk_lib (Lib andheader)    
    * api_headers: the header of the module, 
    * lib:static library for the different platforms            
* sample   
    * api_sample:the sample for the each module of the PSDK.  
    * platform:Project directory, include compiled file, initial file and the configuration.  
* tools:Binary file tools file2c

#### Include The Library 

The development platform, developers need according to use in the PSDK development kit ` psdk_lib/lib ` choose corresponding platform static library directory.

* Linux
Include the library `libpayloadsdk.a`in the `CMakeLists.txt` as shown below.
```c
link_directories(${CMAKE_CURRENT_LIST_DIR}/../../../../../psdk_lib/lib/aarch64-linux-gnu-gcc)      /*Specify the address of the library*/
link_libraries(${CMAKE_CURRENT_LIST_DIR}/../../../../../psdk_lib/lib/aarch64-linux-gnu-gcc/libpayloadsdk.a)      /*Call the library*/
```

* RTOS  
Add the `payloadsdk.lib` into the project's directory.    

#### Include The header
Each header correspond the each module,for example the `#include "psdk_payload_camera.h"` correspond the PSDK's camera module.     
 * Linux    
Add the `include_directories(../../../../../psdk_lib/api_headers)` into `CMakeLists.txt`, and developer could include the header into the code files.
```c
   #include "psdk_platform.h"
   #include "platform/osal.h"
   #include "platform/hal_uart.h"
```

 * RTOS     
 Add the path of the project into the MDK‘s configuration file, and developer could include the header to develop the payload.
   ```c
   #include "psdk_platform.h"
   #include "platform/osal.h"
   #include "platform/hal_uart.h"
   ```


#### Include the compiler define
> **NOTE** Please add the compiler define before coding. 


Linux 和RTOS according to the compiler define enable the special functions， enable is 1，opposite is 0.    
* Linux:SDK_ARCH_SYS_LINUX = 1                   
* RTOS:PSDK_ARCH_SYS_LINUX = 1             


## PSDK Initialization 
The first step to develop the payload which based on PSDK is Platform module initial and PSDK initial.

#### 1. Register the Platform module
After register the Hal and Osal, the program of the payload developed based on PSDK could be ported to other platforms.

> **NOTE** If you developed the payload on RTOS, you must register the Hal and Osal in the RTOS operating system thread and ensure that the thread can be called normally when the scheduler works.

* Hal Register for the network port    
After register the hal function of the network port, the payload could communicate with the drone using network port.

```c
T_PsdkReturnCode HalNetWork_Config(const char *ipAddr, const char *netMask)
```

> **NOTE**
> * [Configue the parameters of the networl by the automatic](../camera/video-stream-transmission.html), please register the function `PsdkPlatform_RegHalNetworkHandler()`.
> * The payload developed on the Linux support use the network interface communicate with the drone and developer need use command `ifconfig` config this interface and transmit the massage, for details, please refer to`sample/platform/linux/manifold2/hal/hal_network.c`.


* Hal Register for the serial port  
Register the Hal could make the payload port to other hardware platforms.

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

#### 2. PSDK Initialization
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



#### 3. Start to run the application
After initialized all the functions, developer <b>must call the interface `PsdkCore_ApplicationStart()`</b> start to run the program,otherwise the Mobile App couldn't control the paylaod.


## Set The Alias
The payload developed based on PSDK supports developer to set the alias for the payload, and the DJI Pilot or the Mobile APP developed based on MSDK will display the alias of the payload. If not, DJI Pilot or Mobile APP developed based on MSDK will display the name which was registered in the [User Center](https://developer.dji.com/user/apps/#all).

```c
if (PsdkProductInfo_SetAlias("PSDK_APPALIAS") != PSDK_RETURN_CODE_OK) {
    PsdkLogger_UserLogError("set product alias error.");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```