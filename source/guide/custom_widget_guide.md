---
title: Custom Widget
date: 2019-09-23
keywords: [Custom Widget]
---

## Overview

Users could obtain parameters from the payload, which developed by PSDK use Pilot and APP, if developed based on DJI MSDK (interface `DJIPayloadWidget`), also could control the payload or modify parameters through the UI control. Associated the payload function with the button on the remote control, could help the user more convenient.

## Function

To ensure the Pilot and the MSDK-based APP can obtain the parameters of each function from the payload and generate UI controls corresponding to the function, which described the format. For detailed parameter see [Control Parameters](#control-parameters).

### Format

Describing the functions of the payload (developed on the PSDK) in the format, the UI controls could be generated in the Pilot and the MSDK-developed APP makes the user modify the parameters.

```
typedef struct {
    uint8_t widgetType;             /*!< Specifies widget type.
                                         This parameter can be any value of ::E_PsdkAppFuncWidgetType */
    uint8_t widgetIndex;            /*!< Specifies widget index.
                                         @note The value is a unique index for the widget, starting at 0.
                                         DJI Pilot widget show sequence relay on the widgetIndex.*/
    uint8_t widgetName[APPFUNC_MAX_WIDGET_NAME_SIZE];/*!< Specifies widget name string.
                                                              @note Widget name max length is #APPFUNC_MAX_WIDGET_NAME_SIZE */
    union {
        struct {
            PSDK_EMPTY_STRUCT
        } buttonAttribute;          /*!< Specifies button widget attribute. */
        struct {
            PSDK_EMPTY_STRUCT
        } switchAttribute;          /*!< Specifies switch widget attribute. */
        struct {
            PSDK_EMPTY_STRUCT
        } scaleAttribute;           /*!< Specifies scale widget attribute. */
        struct {
            uint8_t listItemNum;    /*!< Specifies list item number */
            uint8_t listItemName[APPFUNC_LIST_MAX_ITEM_NUM][APPFUNC_LIST_MAX_ITEM_NAME_SIZE];
            /*!< Specifies list item names.
                 @note list item name max length is #APPFUNC_LIST_MAX_ITEM_NAME_SIZE */
        } listAttribute;            /*!< Specifies list widget attribute. */
        struct {
            uint8_t promptChar[APPFUNC_INT_INPUT_BOX_PROMPT_CHAR_MAX_SIZE];
            /*!< Specifies input box additional prompt string.
                 @note its max length is #APPFUNC_INT_INPUT_BOX_PROMPT_CHAR_MAX_SIZE */
        } intInputBoxAttribute;     /*!< Specifies input box widget attribute. */
    } widgetAttribute;
} T_PsdkAppFuncWidgetProperty;

```

> NOTE：For detailed description about the format, please see the API documents.

### Control Parameters

The PSDK uses five attributes: type, range, additional attribute, name, and index to describe the capabilities of the payload. Pilot and MSDK-based APP can generate 5 kinds of UI controls: button, switch, slider, drop-down option, and input box. For details refer to Table1. Control Parameters. The effect is shown in Figure1. Load settings.

<table id="t01">
Table1. Control Parameters
  <tbody>
     <tr>
       <td>Control Type</td>
       <td>Range</td>
       <td>Additional Properties</td>
       <td>Name</td>
       <td>Index</td>

     </tr>
     <tr>
      <td> Button</td>
       <td>0 / 1</td>
       <td>-</td>
       <td rowspan="5">32 Bytes at most.</td>
       <td rowspan="5"> 0~29</td>
     </tr>
     <tr>
       <td>Switch</td>
       <td>0 / 1</td>
       <td>-</td>
     </tr>
     <tr>
      <td>Slider</td>
       <td>0 to 100</td>
       <td>-</td>
     </tr>
      <tr>
      <td>Dropdown List</td>
       <td>0 to COUNT<sub>list</sub> - 1</td>
       <td>Options: Up to 10<br/> Option Name: Up to 16 Bytes</td>
     </tr>
        <tr>
      <td>Input Box</td>
       <td>-2,147,483,648 ～ 2,147,483,647</td>
       <td>Input Box: This maximum value is 32 bit.</td>
     </tr>
   </tbody>
</table>

> NOTE：      
> 
>*  COUNT<sub>list</sub> is the number of options.
>*  Pilot and the MSDK-developed APP use the index to display the controls corresponding with each function, and the UI controls must less than **30**.

Figure1.Setting Payload  

![](../images/introduction/psdk_introduction/pilot_widget.png)

## Association

Associated the index of the control type with the reserved button on the remote controller Cendence GL900A, users can get access to functions on payload (developed basis on PSDK) products more easily. For details, see Table2 Relationship between UI Controls and reserved buttons. 

<table id="t02">
Table 2. Relationship between UI Controls and reserved buttons.
  <tbody>
    <tr>
      <td>Control Type</td>
      <td>Reserved Button</td>
      <td>Trigger</td>
    </tr>
    <tr>
      <td> Button</td>
      <td rowspan="3">Keys: C1-C4/BA-BH </td>
      <td>Button press: Triggers the “button”control to press the command</br>Button Release: Trigger button control to release command </td>
    </tr>
    <tr>
      <td>Switch</td>
      <td> Flip Trigger: Release after the button is pressed, Trigger the "switch" control to open or close the command</td>
    </tr>
    <tr>
     <td>Dropdown List</td>
      <td>Click Trigger: Press the button and release it, trigger the command to select the next item</td>
    </tr>
     <tr>
      <td>Slider</td>
      <td> Left and right lever: LD/RD </td>
      <td>Toggle Trigger: Trigger the lever to trigger the slider control to modify the slider value</td>
    </tr>
       <tr>
    <td>Input Box</td>
      <td> Focusing Knob: TD</td>
      <td>Knob Trigger: Trigger the focus knob to trigger the input box control, you can modify the input box value</td>
</tr>
  </tbody>
</table>
