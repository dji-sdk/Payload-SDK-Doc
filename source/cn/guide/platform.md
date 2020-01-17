---
title: 选择开发平台
date: 2020-01-17
keywords: [开发须知, 硬件选购, 软件版本, 固件版本]
---
请根据不同平台对PSDK 功能的支持差异、负载设备程序的资源占用情况以及PSDK 支持的**工具链**选择开发负载设备的软硬件平台。

## 功能差异
由于RTOS 平台没有网口，因此在RTOS 平台上使用PSDK 开发的负载设备**不支持**使用
*视频流传输功能* 、 *媒体文件回放下载功能* 和 *高速数据传输功能*。

## 资源占用
#### Linux
使用Manifold 2-C 运行在Linux 平台上基于PSDK 开发的负载设备控制程序，程序运行时的资源占用情况如下所示：        
* 栈：约 12288 字节
* 堆：约 40960 字节
* Text 段：455380 字节
* Data 段：3584 字节
* Bss 段：52568 字节
* CPU 占用：7.2 %

#### RTOS 
使用STM32F407IGH6-EVAL 运行在RTOS 平台上基于PSDK 开发的负载设备控制程序，程序运行时的资源占用情况如下所示：      
* Text 段：271896 字节
* Data 段：1664 字节
* Bss 段：63240 字节
* CPU 占用：20 %

## 选择开发平台
PSDK 支持使用如下工具编译基于PSDK 开发的负载设备，请根据选用的**开发平台**正确地选择工具链。
> **说明：** 为方便您降低开发成本，提高开发效率，建议使用下述编译链，若有其他特殊需求，请联系<a href="mailto:dev@dji.com">SDK 技术支持团队</a>。

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