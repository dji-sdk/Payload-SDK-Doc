---
title: 如何使用PSDK ？
date: 2020-01-17
version: 2.0.0
keywords: [注册, 选购, 入门, 学习, 进阶, 高级]
---
> **说明：** 本系列文档介绍PSDK V2.0.0 的功能，以及使用PSDK V2.0.0 开发负载设备的步骤和方法，若您仍使用PSDK V 1.5.0 开发负载设备，请下载[PSDK V1.5.0](https://terra-1-g.djicdn.com/71a7d383e71a4fb8887a310eb746b47f/psdk/payload-sdk-doc-1.0.zip) 的文档。

使用PSDK 开发负载设备前，需要先注册具有PSDK 使用权限的企业账号；使用PSDK 开发负载设备时，需要选购DJI 的**无人机**和开发负载设备的**硬件平台**。    
建议您根据本文提供的开发引导，通过学习开发负载设备时所需的**基础知识**、了解开发负载设备的**各项标准**，借助**实践教程和API 文档**，开发出可挂载在DJI 无人机上**功能完善**的负载设备。

## 1. 注册DJI PSDK 企业账号

* 在<a href="https://developer.dji.com/payload-sdk/apply/" target="_blank">注册</a>成为PSDK 的企业用户时，请务必**认真**阅读使用DJI SDK 的<a href="https://developer.dji.com/cn/policies/privacy/">协议、条款和政策</a>。
* 为方便您获得便捷高效的服务，请**正确地**填写注册信息。

## 2. 选用开发工具
选购开发负载设备时所需使用的无人机、开发平台和硬件平台：

* 选购<a href="https://www.dji.com/cn/products/compare-m200-series?site=brandsite&from=nav" target="_blank" >无人机</a>
* 选购开发负载设备的[开发套件或硬件平台](../guide/hardware.html)
* 选择[开发平台](../guide/platform.html)

> **注意**
> * X-Port 和Skyport V2 仅支持使用**PSDK V2.x.x**；
> * Skyport 仅支持使用**PSDK V1.x.x** ；
> * DJI 将在 **2020年 2月 1日**停止对**PSDK V1.x.x** 和Skyport 的维护，建议使用**X-Port** 或**Skyport V2** 在**PSDK V2.x.x** 的基础上开发负载设备。

## DJI PSDK 开发引导

#### 开发前准备
使用PSDK 开发负载设备前，建议先学习开发负载设备所需的基础知识、了解PSDK 的功能以及负载设备所需满足的标准，根据实际的开发需求选购合适的硬件平台，选择可靠的开发平台。

* 学习无人机基础知识和控制原理：如俯仰、偏航、滚转和升降等基础知识  
* 了解PSDK 可支持的[功能](./feature-list.html)   
* 遵循DJI 的负载设备[设计标准](../guide/payload-criterion.html)   
* 了解[硬件平台](../guide/hardware.html)   
* 选择[开发平台](../guide/platform.html)    

#### 开始开发负载设备
使用PSDK 开发负载设备时，**请正确地连接**所选购的硬件平台、第三方开发板和DJI 的无人机，**正确地配置**负载设备开发环境，通过运行示例代码编译后的程序，了解使用PSDK 开发负载设备的方法。

* 在使用PSDK 开发负载设备前，请先阅读[开发须知](../workflow/attention.html)中的内容，避免因操作不当损毁负载设备或无人机；
* [连接](../workflow/device-connection.html)无人机、硬件平台、第三方开发板和计算机；
* [安装](../workflow/development-environment.html)开发PSDK 的软件，准备相关工具链和库；
* [编译](../workflow/run-the-sample.html)示例代码，通过运行示例程序，了解实现PSDK 各项功能的方法；
* 通过[跨平台移植](../tutorial/Porting.html)，将基于PSDK 开发的负载设备控制程序移植到不同的软硬件平台上。

#### 开发功能完善的负载设备
* 根据[实践教程](../tutorial/initial.html)和PSDK API 文档，开发负载设备。
* 借助[DJI Assistant 2](https://www.dji.com/cn/downloads) 等工具调试负载设备，完善负载设备的功能，提高负载设备的性能。

## 成为DJI 的合作伙伴
DJI 秉承**开放共赢**的合作理念，为开发者提供技术支持、负载检测、渠道推荐以及DJI 生态推广等服务，诚挚携手广大开发者以及合作伙伴共建可持续发展的应用生态。

* 合作伙伴若需批量生产基于PSDK 开发的负载设备（≥ 10台），需要向DJI 申请负载设备量产许可。
* 若合作伙伴开发的负载设备能通过DJI 的负载检测，该负载设备将被DJI 推荐给第三方合作伙伴。
* 若合作伙伴的负载设备能够通过第三方专业机构的检测，在与DJI 签署合作协议后，DJI 将与合作伙伴开展更为深入的合作，如将合作伙伴的负载设备推荐给<a href="https://www.dji.com/cn/products/enterprise#partner-payloads">全球用户</a>等，更多合作事宜请<a href="mailto:dev@dji.com"> 联系我们</a>。

## 获取技术支持服务

* 查看<a href="../faq/index.html">帮助文档</a>

* 在<a href="https://djisdksupport.zendesk.com/hc/zh-cn/community/topics">DJI 技术支持社区</a>中寻求帮助  

* 获取技术支持服务  
	* 使用<a herf="https://formcrafts.com/a/dji-developer-feedback-cn">问题反馈</a>表单  
	* 向DJI SDK 团队，发送<a href="mailto:dev@dji.com">邮件</a>
