---
title: Payload SDK 功能 - 无人机状态数据推送
date: 2019-09-23
keywords: [介绍, 功能, Payload SDK]
---

### 数据推送

Payload SDK 提供有关无人机状态的一些实时信息推送。以下是您的负载如何使用此信息的一些示例：

- 对于相机类，您可以拍摄照片时记录无人机的 GPS/RTK 位置并将其作为元数据存储。
- 对于相机/云台类负载，您可以记录无人机的姿态，并在需要绝对位置和方向的用例中用它来旋转图片。
- 当无人机电池电量低于一定水平时，您可以监控电池电量并关闭负载的某些功能。
- 您可以根据UTC时间戳信息，并结合PPS硬件信号，实现对负载位置的获取，进而实现精准测绘等功能。
- 您可以根据负载类型与负载焦距信息实现与飞行器上其他负载同步变焦等功能。

### 数据推送详情
Payload SDK 提供对无人机状态的访问，参考 Payload SDK API 手册了解详情。

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
      <td> 数据通讯状态</th>
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
    </tr>
    <tr>
      <td>UTC 时间戳</th>
      <td>1Hz</td>        
    </tr>
    <tr>
      <td>负载类型</th>
      <td>10Hz</td>        
    </tr>
    <tr>
      <td>负载焦距信息</th>
      <td>2Hz</td>        
    </tr>
  </tbody>
</table>
