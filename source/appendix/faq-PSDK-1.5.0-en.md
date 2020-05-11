---
title: FAQ (For PSDK 1.5.x)
date: 2020-05-08
keywords: [FAQ, Frequently Asked Questions]
---

In order to help you solve the problems quickly, we recommend that you could go to <a href="https://forum.dji.com/forum-139-1.html?from=developer"> DJI Technical Support Community </a> to find the solution; if you have other questions, please use <a href="https://formcrafts.com/a/dji-developer-feedback-cn"> Issue Form </a> to feedback the question, or send an <a href="mailto:dev@dji.com"> E-mail </a> to DJI SDK team. DJI appreciates your support and attention.

> **NOTE** DJI won't develope the PSDK V1.5.x and SkyPort on February 1st, 2020. It is recommended to use [X-Port](https://store.dji.com/product/dji-x-port) or [SkyPort V2](https://store.dji.com/product/psdk-development-kit-v2) and PSDK V2.x.x to develop the payload.

## SkyPort
#### What is the model of the SkyPort coaxial port connector?
DF56C-40S-0.3V

#### How to handle the error "Firmware Exception" 
Please check the version of DJI Assistant 2 (2.0.8 and above), and upgrade the DJI Assistant 2 to the latest version.

#### How to change the SkyPort's firmware?
Please modify the version number in the PSDK sample code `app_info.h` file.
After specifying the version number, users can not to use the SkyPort's latest firmware.

#### How to handle "The developer account is illegal"
* Please confirm that the account in DJI Assistant 2, the application and the payload program (`app_info.h file`) are the same developer account.
* Please confirm that the information such as APP name, APP ID, and APP KEY have been correctly filled into the file `app_info.h`.

#### DJI Assistant 2 cannot get information from the payload
Please follow the steps to confirm the status of the payload:
1. Please confirm that the payload's program has been written or burned into the development board successfully;
2. Please confirm that the working mode is serial mode (the three blue lights are all on, otherwise click KEY2);
3. Please set the mode is serial mode, on the DJI Assistant 2;
4. Select the UART interface (baud rate:115200) at the SKYPORT setting page.

> **NOTE**
> * If you want to get the information pushed by the payload, please turn on the switch.
> * IF you want to get the battery information of the drone, turning on the push battery information switch and call the `batteryInfoMsgCallBack ()` interface to get the battery information of the drone.

## Compilation 
#### Cannot generate .bin file when compiling sample code with Keil MDK
* Cause: The location of the sample code is not specified.
* Solution: Please specify the location of the sample code to be compiled in Keil MDK. The default path is `C:\Keil_v5\ARM\ARMCC\Bin\fromelf.exe.\Objects\psdk_demo.axf --bin--output.\psdk_demo.bin`, as shown in Figure 3. Specifying the location of the sample code.

<div>
<div style = "text-align: center"> <p> Figure 3. Specifying the location of the sample code </p>
</div>
<div style = "text-align: center"> <p> <span>
      <img src = "../images/faq/1.png" width = "600" style = "vertical-align: middle" alt /> </span></p>
</div></div>


## Interface problems
#### What is the difference between gpsInfoMsg and gpsRawDataMsg?
* `gpsInfoMsg`: This interface is used to obtain the GPS fusion data of the drone: the data processed by GPS, GLONASS, BeiDou, Galileo and four GNSS data (radian system).
* `gpsRawDataMsg`: This interface is used to obtain GPS raw data.

#### How to use the log print interface in PSDK 1.5.x  
Please use the UART 1 interface and call the `void LOG_Init (void)` interface:

```c
void LOG_Init (void)
{
    UART_Init (UART_NUM_1, 460800);
    isLogInit = 1;
}
```

When debugging the payload, please make sure that the baud rate is 460800, otherwise, the content in the log may be garbled.

#### How to get the debugging information of the payload
Please set `APPLICATION_TEST` to TRUE in the header` app_config.h`.

#### How to enable the text input box function
Please set the value of `textInputBoxDisplayControlFlag` in the test_app_func.c file to` PSDK_APPFUNC_TEXT_INPUT_BOX_DISPLAY`.

#### How to get the status of the payload?
Please use `E_Constants_Psdk_Motor_State` and` E_Constants_Psdk_Land_State` in `T_UavStateMsg` to get the status of the drone motor and landing.