---
title: 文档主页
date: 2018-09-13
keywords: [介绍]
---

## DJI Payload SDK 是什么?

DJI Payload SDK ( PSDK ) 是一款转换型 SDK，主要用于让第三方厂家基于 DJI 飞行平台进行负载设备开发。第三方厂家可以使用飞行平台的资源，如电源、通讯链路、状态信息（ GPS 信息、姿态信息、时间日期 ）等。同时，Payload SDK 还提供配套的软件支持，如 Onboard SDK，Mobile SDK，DJI Pilot，DJI Assistant 等。

本文档可帮助开发人员开始使用PSDK并了解其细微差别。本网站的结构总结如下。

## 硬件套件

PSDK 硬件套件包括 DJI SKYPORT转接环，开发板和连接两个组件的同轴线。

有关此硬件套件的详细信息，请参见 [硬件介绍](hardware_introduction.html) 页面.

## 功能

- [功能概述](../features/psdk_introduction.html)
- [数据传输](../features/data-transmission.html)
- [相机和云台功能](../features/camera-gimbal-features.html)
- [飞机状态数据推送](../features/aircraft-state-push-data.html)
- [配套软件支持](../features/integrate-other-dji-sdk-apps.html)

## 快速开始

开发者可以 [运行示例应用程序](../quick-start/index.html) 运行示例代码，并探索如何使用 Payload SDK 在上面添加功能。 

## 指南

提供 PSDK 组件和接口调试的操作指引。本节有助于解释：

- [网络端口](../guide/network_port.html)
- [SKYPORT 安装](../guide/adapter_install.html)

## 开发工作流程

- [与 PSDK 集成](../development-workflow/integrate_sdk.html)
- [构建应用程序](../development-workflow/build-application.html)

## FAQs

可以在 [这里](../faq/index.html) 找到开发人员提交的最常见问题（FAQ）的所有答案。
