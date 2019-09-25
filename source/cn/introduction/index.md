---
title: 文档主页
date: 2019-09-24
keywords: [介绍]
---

## DJI Payload SDK 是什么?

DJI Payload SDK ( PSDK ) 是一款转换型 SDK，主要用于让第三方厂家基于 DJI 飞行平台进行负载设备开发。第三方厂家可以使用飞行平台的资源，如电源、通讯链路、状态信息（ GPS 信息、姿态信息、时间日期 ）等。同时，Payload SDK 还提供配套的软件支持，如 Onboard SDK，Mobile SDK，DJI Pilot，DJI Assistant 等。

本文档可帮助开发者开始使用PSDK并了解其细微差别。本网站的结构总结如下。

## 硬件

* [DJI SKYPORT](hardware_introduction.html) 转接环（含开发板和排线）
* DJI X-PORT 标准云台

## 功能

- [功能概述](../features/psdk_introduction.html)
- [数据传输](../features/data-transmission.html)
- [相机和云台功能](../features/camera-gimbal-features.html)
- [无人机状态数据推送](../features/aircraft-state-push-data.html)
- [配套软件支持](../features/integrate-other-dji-sdk-apps.html)

## 快速开始

开发者可以 [运行示例应用程序](../quick-start/index.html) 来运行示例代码，并探索如何使用 Payload SDK 在上面添加功能。 

## 指南

提供 PSDK 组件和接口调试的操作指引。本节有助于解释：

- [网络端口](../guide/network_port.html)
- [SKYPORT 安装](../guide/adapter_install.html)
- [自定义控件](../guide/custom_widget_guide.html)
- [多负载协同](../guide/multi_payload_collaboration.html)
- [定位功能](../guide/positioning_guide.html)

## 开发工作流程

- [与 PSDK 集成](../development-workflow/integrate_sdk.html)
- [构建应用程序](../development-workflow/build-application.html)

## FAQs

可以在 [这里](../faq/index.html) 找到开发者提交的最常见问题（FAQ）的所有答案。
