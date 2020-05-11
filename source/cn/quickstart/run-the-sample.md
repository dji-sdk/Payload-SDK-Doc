---
title: 运行示例程序
date: 2020-05-08
version: 2.1.0
keywords: [Payload SDK]
---
在注册PSDK 企业账号后，请下载PSDK 提供的示例代码并在示例代码中补充应用信息，通过编译、调试和烧录等操作获得示例程序。在DJI Assistant 2 上绑定DJI 的硬件平台后，即可运行示例程序，借助示例程序了解使用PSDK 开发负载设备的方法。

> **提示：** 如需将RTOS 或Linux 的示例代码运行在其他开发板或操作系统中，请参考 [跨平台移植](../tutorial/Porting.html)。  

## 获取示例代码
在 <a href="https://developer.dji.com/payload-sdk/apply/" target="_blank">注册</a>成为DJI PSDK 的企业用户后，即可下载DJI PSDK 开发包，在PSDK 开发包中获取DJI 提供的示例代码，借助示例代码了解使用PSDK 开发负载设备的方法，使用示例代码快速开发出功能完善的出负载设备。     

## 创建负载应用
获取使用PSDK 开发负载产品的[权限](https://developer.dji.com/payload-sdk/apply) 后，请在[用户中心](https://developer.dji.com/user/apps/#all) 创建负载应用，获取应用ID 和应用秘钥，如 图1.填写应用信息 所示。 
<div>
<div style="text-align: center"><p>图1. 填写应用信息</p>
</div>
<div style="text-align: center"><p><span>
      <img src="../../images/APPinfo.png" width="240" style="vertical-align:middle" alt/></span></p>
</div></div>

> **注意：** 为提高您的开发效率，请在示例代码中**正确**填写*应用的名称*、*ID*、*Key*和*开发者账号*，否则编译后的示例程序将无法正常运行。

## 运行RTOS 示例代码

> **说明：**本文以**STM32F407IGH6-EVAL** 为例，介绍运行RTOS 示例代码的步骤和方法。 

#### 烧录 Bootloader 
1. 使用Keil MDK IDE 打开位于`sample/platform/rtos_freertos/stm32f4_eval/project/mdk_bootloader/`目录下的工程文件`psdk_demo_bootloader.uvprojx`。
2. 使用Keil MDK IDE 编译工程为示例程序。
3. 将编译后的示例程序**烧录**到负载设备中（如STM32F407IGH6-EVAL）。

> **相关参考**
> * 实现Bootloader：`platform/rtos_freertos/stm32f4_eval/bootloader`
> * Bootloader工程目录：`platform/rtos_freertos/stm32f4_eval/project/mdk_bootloader`

#### 补充应用信息
1. 使用Keil IDE 打开位于`sample/platform/rtos_freertos/stm32f4_eval/project/mdk_release/`目录下的工程文件`psdk_demo.uvprojx`。
2. 在 `sample/platform/rtos_freertos/stm32f4_eval/application/app_info.h` 文件中补充应用的名称、ID、Key和开发者账号。

```
#define USER_APP_NAME               "your_app_name"
#define USER_APP_ID                 "your_app_id"
#define USER_APP_KEY                "your_app_key"
#define USER_DEVELOPER_ACCOUNT      "your_developer_account"
```

#### 编译并烧录
* 使用Keil MDK IDE 编译示例代码为示例程序。
* 编译示例代码后，将编译后的程序**烧录**到负载设备中（如STM32F407IGH6-EVAL）。
* 如需调试示例程序，请将串口调试工具的波特率设置为：`921600`。

## 运行Linux 示例代码
> **说明：** 本文以Manifold 2-C 为例，介绍运行Linux 示例代码的步骤和方法。

#### 补充应用信息
* 在 `sample/platform/linux/manifold2/application/app_info.h` 文件中替换应用的名称、ID、Key和开发者账号。

```
#define USER_APP_NAME               "your_app_name"
#define USER_APP_ID                 "your_app_id"
#define USER_APP_KEY                "your_app_key"
#define USER_DEVELOPER_ACCOUNT      "your_developer_account"
```

* 在 `sample/platform/linux/manifold2/hal/hal_uart.c` 文件的 `LINUX_UART_DEV` 宏中填写串口名称。

```
#define LINUX_UART_DEV   "dev/your_com"
```
* 通过`ifconfig`命令，查看当前与无人机通讯的网口设备名称，并填写到`sample/platform/linux/manifold2/hal/hal_network.c` 文件的 `LINUX_NETWORK_DEV` 宏中。

  ```c
  #define LINUX_NETWORK_DEV    "your_network_name"
  ```
#### 编译示例程序

* **编译示例代码**
进入示例代码的目录： `sample/platform/linux/manifold2/project`，使用如下命令将示例代码编译为示例程序。
  1. `mkdir build`
  2. `cd build`
  3. `cmake ..`
  4. `make`

* **执行示例程序**
  * 进入示例程序的目录： `sample/platform/linux/manifold2/project/build`
  * 使用`sudo ./psdk_demo`命令运行示例程序

## 应用绑定
通过DJI Assistant 2 将SkyPort V2 与示例程序绑定后，当负载设备挂载在无人机上时，负载设备将自动运行开发者编译或烧录的示例程序。

> **说明** 
> * 使用DJI Assistant 2 绑定或调试负载设备时，请先在软件右上角的“配置”标签中打开 **“数据授权”** 开关，否则DJI Assistant 2 将无法正常绑定或调试负载设备。
> * 初次绑定SkyPort V2 后，在不同的无人机上使用同一个SkyPort V2 时，无需重新绑定示例程序。

1. 将负载设备（如Manifold 2-C）或开发板（如STM32F407IGH6-EVAL）挂载在DJI 的无人机上，同时将DJI 的无人机连接到计算机；
2. 使用**应用信息**中的**账号**登陆DJI Assistant 2 ，单击“Payload SDK ”选项卡，进入PSDK 硬件平台界面；
3. 在PSDK 硬件平台界面，单击“绑定”按钮，绑定硬件平台、示例程序和DJI 无人机；
4. 绑定成功后，PSDK 硬件平台界面中的绑定状态将显示为`已绑定`，如 图2. 应用绑定 所示；
5. 应用绑定成功后，负载设备将自动运行示例程序。

<div>
<div style="text-align: center"><p>图2. 应用绑定</p>
</div>
<div style="text-align: center"><p><span>
      <img src="../../images/binding.png" width="600" style="vertical-align:middle" alt/></span></p>
</div></div>

## 绑定故障排查
#### 1. SkyPort V2 故障排查
<table id="3">
  <thead>
    <tr>
      <th>错误代码</th>
      <th>错误说明</th>
      <th>解决方案</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>无法获取负载信息</td>
      <td>1. 确认硬件平台正常连接</br>2. 确认基于PSDK 开发的负载设备控制程序已正常运行</td>      
    </tr>
    <tr>
      <td>2</td>
      <td>开发者账号非法</td>
      <td>请确认负载设备控制程序中的用户信息与所绑定的转接环的用户信息相同</td>
    </tr>
    <tr>
      <td>3</td>
      <td>无法获取认证信息</td>
      <td rowspan=5>请将负载设备中的日志信息提交给DJI 技术支持团队排查相应的问题</td>  
    </tr>
    <tr>
      <td>4</td>
      <td>SkyPort 校验失败</td>
    </tr>
    <tr>   
      <td>5</td>
      <td>认证信息错误</td>
    </tr>
       <tr>   
      <td>6</td>
      <td>存储绑定信息失败</td>
    </tr>
       <tr>   
      <td>7</td>
      <td>无法获取SN 号</td>
    </tr>
    </tbody>
</table>

#### 2. 应用服务故障排查
<table id="3">
  <thead>
    <tr>
      <th>错误代码</th>
      <th>错误说明</th>
      <th>解决方案</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>400</td>
      <td>SN 不存在</td>
      <td rowspan=5>请将负载设备中的日志信息提交给DJI 技术支持团队排查相应的问题</td>         
    </tr>
    <tr>
      <td>500</td>
      <td>服务器异常</td>
    </tr>
    <tr>
      <td>700</td>
      <td>未找到负载设备的应用程序</td>
    </tr>
    <tr>
      <td>701</td>
      <td>数据校验失败</td>
    </tr>
    <tr>   
      <td>702</td>
      <td>绑定关系错误</td>
    </tr>
       <tr>   
      <td>703</td>
      <td>绑定数量超过限制</td>
      <td>在开发模式下，每个开发者最多可绑定10个负载设备控制程序</td>
    </tr>
    </tbody>
</table>

#### 3. 调参软件故障排查
<table id="3">
  <thead>
    <tr>
      <th>错误代码</th>
      <th>错误说明</th>
      <th>解决方案</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>3</td>
      <td>网络异常</td>
      <td>请确认您的计算机能够访问互联网</td>   
    </tr>
    <tr>
      <td>4</td>
      <td>调参软件错误</td>
      <td rowspan=2>重新安装调参软件或重新启动计算机</td>   
    </tr>
    <tr>
      <td>5</td>
      <td>FTP 错误</td>
    </tr>
    </tbody>
</table>


## 编译故障排查
#### 使用Keil MDK 编译示例代码时报错：“error：L6050U”
* 故障原因：Keil MDK 未激活。
* 解决方法：使用Keil MDK编译示例代码前请先激活Keil MDK。
