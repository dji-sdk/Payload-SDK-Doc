---
title: 选择开发平台
date: 2020-05-08
version: 2.1.0
keywords: [开发须知, 硬件选购, 软件版本, 固件版本]
---
请根据操作系统和开发平台对PSDK 功能的支持差异、负载设备程序的资源占用情况以及PSDK 支持的**工具链**，选择开发负载设备的操作系统和开发平台。

## 选择操作系统
#### 功能差异
由于RTOS 平台没有网口，因此在RTOS 平台上使用PSDK 开发的负载设备**不支持**使用
*视频流传输功能* 、 *媒体文件回放下载功能* 和 *高速数据传输功能*。

#### 资源占用
###### Linux
使用Manifold 2-C 运行在Linux 平台上基于PSDK 开发的负载设备控制程序，程序运行时的资源占用情况如下所示：        
* 栈：约 12288 字节
* 堆：约 36864 字节
* Text 段：641742 字节
* Data 段：3808 字节
* Bss 段：21992 字节
* CPU 占用：7.2 %

###### RTOS 
使用STM32F407IGH6-EVAL 运行在RTOS 平台上基于PSDK 开发的负载设备控制程序，程序运行时的资源占用情况如下所示：      
* Text 段：315184 字节
* Data 段：1760 字节
* Bss 段：84848 字节
* CPU 占用：30 %

## 选择开发平台
PSDK 支持使用如下工具编译基于PSDK 开发的负载设备，请根据选用的**开发平台**正确地选择工具链。
> **说明：** 有关跨平台移植的详细说明请参见[跨平台移植](../quickstart/porting.html)。

<table id="toolchain">
<thead>
<tr>
   <th>工具链名称</th>
   <th>目标平台</th>
   <th>典型芯片型号</th>
   <th>推荐开发平台</th>
</tr>
</thead>
<tbody>
<tr>
   <td>aarch64-linux-gnu-gcc</td>
   <td>aarch64-linux-gnu</td>
   <td>NVIDIA Jetson TX2、Rockchip RK3399 pro</td>
   <td>Manifold2-G、瑞芯微Toybrick开发板</td>
</tr>
<tr>
   <td>gcc</td>
   <td>x86_64-linux-gnu</td>
   <td>64位intel处理器，如 Intel Core i7-8550U</td>
   <td>Maniflod2-C</td>
</tr>
<tr>
   <td>arm-linux-gnueabi-gcc</td>
   <td>arm-linux-gnueabi</td>
   <td>ZYNQ、I.MX6Q</td>
   <td>-</td>
</tr>
<tr>
   <td>arm-linux-gnueabihf-gcc</td>
   <td>arm-linux-gnueabihf</td>
   <td>支持硬件浮点运算的处理器，如OK5718-C等</td>
   <td>-</td>
</tr>
<tr>
   <td>armcc</td>
   <td>Cortex M系列MCU</td>
   <td>STM32F407、STM32F103</td>
   <td>STM32F407-Eval、STM32F407探索者开发板等</td>
</tr>
<tr>
   <td>arm-himix100-linux-gcc</td>
   <td>arm-himix100-linux</td>
   <td>hi3516EV系列芯片</td>
   <td>-</td>
</tr>
<tr>
   <td>arm-himix200-linux-gcc</td>
   <td>arm-himix200-linux</td>
   <td>hi3516C系列芯片</td>
   <td>-</td>
</tr>
<tr>
   <td>aarch64-himix100-linux-gcc</td>
   <td>aarch64-himix100-linux</td>
   <td>hi3559C</td>
   <td>-</td>
</tr>
<tr>
   <td>arm-hisiv300-linux-uclibcgnueabi-gcc</td>
   <td>arm-hisiv300-linux-uclibcgnueabi</td>
   <td>hi3516A系列芯片</td>
   <td>-</td>
</tr>
<tr>
   <td>arm-hisiv400-linux-gnueabi-gcc</td>
   <td>arm-hisiv400-linux-gnueabi</td>
   <td>hi3516A系列芯片</td>
   <td>-</td>
</tr>
<tr>
   <td>arm-hisiv500-linux-uclibcgnueabi-gcc</td>
   <td>arm-hisiv500-linux-uclibcgnueabi</td>
   <td>hi3519系列芯片</td>
   <td>-</td>
</tr>
<tr>
   <td>arm-hisiv600-linux-gnueabi-gcc</td>
   <td>arm-hisiv600-linux-gnueabi</td>
   <td>hi3519系列芯片</td>
   <td>-</td>
</tr>
</tbody>
</table>

> **说明：** 开发者需根据所使用的开发平台，选择指定编译链的静态库。若开发包中没有所需编译链的静态库，请提供开发负载设备时使用的**开发平台的型号**、**编译链的型号**和**编译链的安装包**发送给<a href="mailto:dev@dji.com">SDK 技术支持团队</a>，我们将为您准备相应的工具链。

