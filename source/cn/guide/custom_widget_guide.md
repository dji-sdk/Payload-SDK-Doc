---
title: 自定义控件
date: 2019-09-24
keywords: [控件, 自定义, 自定义控件]
---

## 概述

使用PSDK 开发的负载设备，能够让使用者通过Pilot 以及基于DJI MSDK开发的APP（调用接口`DJIPayloadWidget`），获取负载设备中的各项参数，通过UI 控件控制负载设备执行各种动作，或设置负载设备的参数；将负载设备的功能与遥控器上的预留按键关联后，即可以更便捷的操作方式快速使用负载设备上的功能。

## 功能描述

为确保Pilot 以及基于DJI MSDK开发的APP可获取负载设备中各个功能的参数，生成与各个功能对应的UI控件，请按照固定的格式描述负载设备的功能，详细的参数说明请参见 [控件参数](控件参数)。

### 描述格式 

按照固定格式描述负载设备（基于PSDK 开发）上的各项功能后，可在Pilot 以及基于DJI MSDK开发的APP 中生成与各项功能对应的UI 控件，方便使用者根据实际的应用需要修改负载设备的各项参数。

```
typedef struct {
    uint8_t widgetType;          /*指定控件属性 */  
    uint8_t widgetIndex;         /*指定控件索引 */  
    uint8_t widgetName[APPFUNC_MAX_WIDGET_NAME_SIZE]     /*指定控件名称*/
    union {
        struct { PSDK_EMPTY_STRUCT} buttonAttribute;     /*指定按钮属性*/
        struct { PSDK_EMPTY_STRUCT} switchAttribute;     /*指定开关属性*/
        struct { PSDK_EMPTY_STRUCT} scaleAttribute;      /*指定滑块属性*/
        struct {
                 uint8_t listItemNum;    /*指定列表编号*/
                 uint8_t listItemName[APPFUNC_LIST_MAX_ITEM_NUM]APPFUNC_LIST_MAX_ITEM_NAME_SIZE]; /*指定列表名称*/
                } listAttribute;         /*!< 指定列表属性 */
        struct {
                uint8_t promptChar[APPFUNC_INT_INPUT_BOX_PROMPT_CHAR_MAX_SIZE];    /*指定输入框附加属性*/
               } intInputBoxAttribute;     /*指定输入框属性 */
    } widgetAttribute;
} T_PsdkAppFuncWidgetProperty;

```

> **说明**：有关描述格式的详细说明请参见API文档。

### 控件参数

PSDK 使用5种属性：类型、取值范围、附加属性、名称和索引描述负载产品的功能，Pilot 以及基于DJI MSDK开发的APP 根据功能的属性值，可快速生成按钮、开关、滑块、下拉选择器和输入框5种UI控件，控件参数的详细说明请参见 表1.控件参数，实现效果如 图1.负载设置所示。  

表1.控件参数

<table id="t01">
  <tbody>
    <tr>
      <td>控件类型</td>
      <td>取值范围</td>
      <td>附加属性</td>
      <td>控件名称</td>
      <td>索引</td>
    </tr>
    <tr>
     <td>按钮</td>
      <td>0 / 1</td>
      <td>\</td>
      <td rowspan="5">最长为32 Bytes</td>
      <td rowspan="5"> 0～29</td> 
    </tr>
    <tr>
      <td>开关</td>
      <td>0 / 1</td>
      <td>\</td>
    </tr>
    <tr>
     <td>滑块</td>
      <td>0 ～ 100</td>
      <td>\</td>
    </tr>
     <tr>
     <td>下拉列表</td>
      <td>0 ～ COUNT<sub>list</sub> - 1</td>
      <td>· 选项数量：最多10个<br/>· 选项名称：最长为16 Bytes</td>
    </tr>
       <tr>
     <td>输入框</td>
      <td>-2,147,483,648 ～ 2,147,483,647</td>
      <td>· 输入框：该数值最大为32 bit</td>
    </tr>
  </tbody>
</table>

> **说明**：      
> 
*  COUNT<sub>list</sub> 为选项数量。
*  Pilot 以及基于MSDK 开发的APP，根据负载设备每个功能的索引，按序显示每个功能对应的控件，最多可显示**30个**UI控件。

图1.负载设置

![](../images/introduction/psdk_introduction/pilot_widget.png)

## 按键关联

将控件与遥控器Cendence GL900A 上的预留按键关联后，使用者通过触发预留按键，可以更便捷的操作方式，快速使用负载设备（基于PSDK 开发）上的功能，详细的对应关系请参见 表2.UI控件与预留按键对应关系。
<table id="t02">
表2.UI控件与预留按键对应关系
  <tbody>
    <tr>
      <td>控件类型</td>
      <td>预留按键</td>
      <td>触发</td>
    </tr>
    <tr>
      <td>按钮</td>
      <td rowspan="3">按键：C1-C4/BA-BH </td>
      <td>· 按键按下：触发“按钮”控件按下命令</br>· 按键释放：触发按钮控件释放命令</td>
    </tr>
    <tr>
      <td>开关</td>
      <td>交替触发：按键按下后释放，触发“开关”控件打开或关闭命令</td>
    </tr>
    <tr>
     <td>下拉列表</td>
      <td>单击触发：按键按下后释放，触发选择下一项目的命令</td>
    </tr>
     <tr>
      <td>滑块</td>
      <td>左右拨杆：LD/RD </td>
      <td>拨动触发：拨动拨杆触发滑块控件，可修改滑块数值</td>
    </tr>
       <tr>
    <td>输入框</td>
      <td>调焦旋钮：TD</td>
      <td>旋钮触发：拨动调焦旋钮触发输入框控件，可修改输入框数值</td>
</tr>
  </tbody>
</table>
