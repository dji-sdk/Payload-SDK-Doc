---
title: Payload SDK 功能 - 飞机状态数据推送
date: 2019-06-17
keywords: [介绍, 功能, Payload SDK]
---

### 推送数据描述

Payload SDK 提供有关飞机状态的一些实时信息推送。以下是您的负载如何使用此信息的一些示例：

- 对于相机类，您可以拍摄照片时记录飞机的 GPS 位置并将其作为元数据存储。
- 对于相机/云台类负载，您可以记录飞机的姿态，并在需要绝对位置和方向的用例中用它来旋转图片。
- 当飞机电池电量低于一定水平时，您可以监控电池电量并关闭负载的某些功能。


### 推送数据详情
Payload SDK 提供对飞机状态的访问，参考 Payload SDK API 手册了解详情。

目前，支持以下推送数据：

<table id="t01">
  <thead>
    <tr>
      <th>状态</th>
      <th>最大推送频率</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> 数据通讯状态 (包括视频传输带宽)</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>飞行姿态</th>
      <td>50Hz</td>        
    </tr>
    <tr>
      <td>电池状态</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>GPS 数据</th>
      <td>1Hz（M200系列），10Hz（M200系列V2）</td>        
    </tr>
    <tr>
      <td>GPS 原始数据</th>
      <td>5Hz</td>        
    </tr>
    <tr>
      <td>海拔高度</th>
      <td>50Hz</td>        
    </tr>
    <tr>
      <td>飞行状态</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>App 时间日期推送</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>RTK 原始数据</th>
      <td>20Hz</td>        
   
