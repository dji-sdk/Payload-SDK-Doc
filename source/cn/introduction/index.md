---
title: 什么是PSDK ？
date: 2020-01-17
version: 2.0.0
keywords: [PSDK, 快速开发, 标准化, 应用场景, 开发引导]
---

> **说明:** 本系列文档介绍PSDK V2.0.0 的功能，以及使用PSDK V2.0.0 开发负载设备的步骤和方法，若您仍使用PSDK V 1.5.0 开发负载设备，请下载[PSDK V1.5.0](https://terra-1-g.djicdn.com/71a7d383e71a4fb8887a310eb746b47f/psdk/payload-sdk-doc-1.0.zip) 的文档。

DJI 为支持开发者开发出可挂载在DJI 无人机上的负载设备，提供了Payload SDK（即PSDK）、[X-Port 标准云台](../guide/hardware.html)和[Skyport 转接环](../guide/hardware.html)，方便开发者利用DJI 无人机上如电源、通讯链路及状态信息等**资源**，开发出可挂载在DJI 无人机上的负载设备。

<div style="text-align: center"><p><span>
      <img src="../../../images/PSDK-features.png" width="500" style="vertical-align:middle" alt/></span></p>
</div>

## 主要优势
* **功能丰富且完善**    
通过使用PSDK 提供的如信息获取、数据传输和电源管理等基础功能，以及相机、云台、负载协同和精准定位等高级功能，开发者能够根据行业的应用需求，设计出**功能完善**的负载设备。

* **拓展应用自定义**     
开发者除使用DJI Pilot 控制基于PSDK 开发的负载设备外，通过使用Mobile SDK 也能开发出控制负载设备执行指定动作的**移动端APP**，此外，使用Onboard SDK 能够开发出控制无人机和负载设备**自动执行任务**的控制程序，使用Windows SDK 还能够开发出数据处理软件，并将所开发的软件集成为一套**功能完整的解决方案**。

* **支持服务有保障**      
PSDK 不仅提供了用于开发DJI 无人机负载设备的功能接口和硬件平台，还提供了开发负载设备的**设计标准**，此外，还提供了包括但**不限于**技术支持、负载检测及市场推广等服务，助力并服务开发者使用PSDK 开发出功能完善的无人机负载设备，探索行业应用的无限潜能。

## 典型功能

* <a href="../camera/camera-basic-functions.html"><b>相机功能</b></a>
* <a href="../tutorial/gimbal-control.html"><b>云台控制</b></a>
* <a href="../tutorial/payload-collaboration.html"><b>负载协同</b></a>
* <a href="../tutorial/custom-widget.html"><b>自定义控件</b></a>
* <a href="../tutorial/positioning.html"><b>精准定位</b></a>
* <a href="../tutorial/data-transmission.html"><b>数据通信</b></a>
* <a href="../tutorial/information-manage.html"><b>信息管理</b></a>

## 负载应用
使用PSDK 开发可挂载在DJI 无人机上的负载设备，能够满足不同行业多样化的应用需求：   

<table id="t1">
  <thead style="text-align:center">
    <tr>
      <td rowspan="2" >负载设备</td>
      <td colspan="3">安防</td>
      <td colspan="2">巡检</td>
      <td colspan="3">勘测</td>
      <td colspan="2">环保</td>
      <td colspan="2">更多行业</td>
    </tr>
    <tr>
      <td>治安管理</td>
      <td>消防</td>
      <td>应急救援</td>
      <td>管网巡检</td>
      <td>厂区巡检</td>
      <td>地质测绘</td>
      <td>空间规划</td>
      <td>资源勘探</td>
      <td>生态监测</td>
      <td>生物保护</td>
      <td>......</td>
    </tr>
  </thead>
  <tbody style="text-align:center">
    <tr>
      <td>可变焦相机</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>热成像相机</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>红外相机</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>多目相机</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>星光相机</td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>激光雷达</td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>气体检测仪</td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
    </tr>
    <tr>
      <td>辐射检测仪</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
    </tr>
    <tr>
      <td>水质检测仪</td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
    </tr>
    <tr>
      <td>喊话器</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
      <td> - </td>
    </tr>
    <tr>
      <td>探照灯</td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> ✓ </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
      <td> ✓ </td>
      <td> - </td>
      <td> - </td>
    </tr>
     <tr>
      <td colspan="2" style="border: none;">更多负载......</td>
    <td style="border: none;text-align:center;"></td>
  </tbody>
</table>


## 使用MSDK 和OSDK
* MSDK：使用MSDK 开发的移动端APP 能够控制负载设备执行指定的动作和任务。
* OSDK：使用OSDK 开发的无人机自动控制程序，借助机载计算机（如Manifold 2-C）的强大算力，不仅能够实现对无人机以及无人机负载设备的自动化控制，还能实现图像识别、物体追踪及深度感知等高级应用。
