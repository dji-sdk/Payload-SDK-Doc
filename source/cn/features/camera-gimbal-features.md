---
title: Payload SDK 功能 - 相机和云台接口
date: 2019-06-17
keywords: [功能, 介绍, Payload SDK]
---

## 相机和云台支持接口
Payload SDK 支持相机和云台类负载，使您的负载能够与 DJI Mobile SDK 和 DJI Pilot 无缝对接。DJI Pilot 为相机和云台负载提供 UI，Mobile SDK 为相机和云台负载提供相应的接口。此支持旨在以下列方式使用：

- Payload SDK 提供的接口由飞机/ MSDK 以与原生 DJI 云台相同的方式进行解释。
- 开发人员有责任根据界面的定义来实现这些功能。
- 例如，PSDK 提供了缩放 API。这意味着当 MSDK 应用程序调用移动端的缩放 API 或 DJI Pilot 上的缩放按钮时，将调用此功能。作为开发人员，您需要为自己的负载实现缩放功能，以便在调用缩放功能时，您的负载通过物理方式执行缩放。

### 相机接口功能支持

<table id="t01">
  <thead>
    <tr>
      <th>接口功能</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>相机工作模式</th>
      <td>拍照模式和录像模式。</td>        
    </tr>
    <tr>
      <td>拍照模式</th>
      <td>单拍、连拍、定时拍照。</td>        
    </tr>
    <tr>
      <td>录像模式</th>
      <td>开始录像和停止录像。</td>        
    </tr>
    <tr>
      <td>SD 卡功能</th>
      <td>获取 SD 卡状态和格式化 SD 卡。</td>        
    </tr>
    <tr>
      <td>测光功能</th>
      <td>测光模式：中央测光、平均测光、点测光。点测光之城设置点测光区域。</td>        
    </tr>
    <tr>
      <td>对焦功能</th>
      <td>支持设置自动对焦的对焦区域。</td>        
    </tr>
    <tr>
      <td>变焦功能</th>
      <td>支持定速变焦和位置变焦。</td>        
    </tr>
  </tbody>
</table>

### 云台接口功能支持

<table id="t01">
  <thead>
    <tr>
      <th>接口功能</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>云台控制</th>
      <td>设置云台角速度/角度/关节角角度。</td>        
    </tr>
    <tr>
      <td>云台回中</th>
      <td>云台回到与机头方向一致。</td>        
    </tr>
    <tr>
      <td>云台模式设置</th>
      <td>支持自由模式、FPV 模式、跟随模式。</td> 
    </tr>
    <tr>
      <td>云台校准</th>
      <td>触发云台校准以及获取云台校准进度与结果。</td>
    </tr>
    <tr>
      <td>云台姿态获取</th>
      <td>获取当前的云台姿态以及是否达到限位。</td>   
    </tr>
  </tbody>
</table>
