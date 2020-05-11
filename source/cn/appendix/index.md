---
title: 常见问题解答
date: 2020-05-08
keywords: [FAQ, 常见问题]
---
为方便您快速解决所遇到的问题，建议您先在<a href="https://bbs.dji.com/forum-79-1.html?from=developer">DJI 技术支持社区</a>中寻找解决问题的方法；若您的问题无法解决或有其他咨询事项，请使用<a href="https://formcrafts.com/a/dji-developer-feedback-cn">问题反馈</a>表单反馈问题，或向DJI SDK 团队发送<a href="mailto:dev@dji.com">邮件</a>，DJI 感谢您的支持和关注。

## 基础问题
##### 1. Payload SDK 支持哪些飞行平台？
Payload SDK 目前支持Matrice 300 RTK 、Matrice 200 V2 系列与Matrice 200 系列的无人机，有关无人机参数的详细说明请参见[参数对比页面](https://www.dji.com/cn/products/compare-m200-series?site=brandsite&from=nav)。     
DJI 提供了X-Port、SkyPort V2 和SkyPort 适配Matrice 200 系列与Matrice 200 V2 系列的无人机，请在开发负载设备和购买无人机前，认真阅读[负载开发标准](https://developer.dji.com/cn/payload-sdk/documentation/guide/payload-criterion.html)中的内容，正确选购所需使用的硬件平台。

##### 2. 什么是开发模式？
* <a href="https://developer.dji.com/payload-sdk/apply/" target="_blank">注册</a>成为PSDK 的企业用户后，开发者所处的模式为开发模式。 
* 在开发模式下，每个开发者的账号总共可绑定9个负载设备。 

##### 3. 什么是量产模式？
* 获取DJI SDK 的量产授权后，开发者所处的模式为量产模式。 
* 在量产模式下，开发者可绑定负载设备的数量不限。    
* 如需获取PSDK 的量产授权，进入量产模式，请将如下资料发送给 <a href="mailto:dev@dji.com">DJI </a> 审核：
  * 营业执照（扫描件）
  * 负载提案：如负载设备的应用场景、使用方法以及关键功能等；
  * 负载设备的详细信息：如负载设备的参数、草图、样机照片等。

> **注意：** 获取量产授权后负载设备**并未得到DJI 的认证**。

##### 4. PSDK 支持开发何种负载设备？
**在当地法律允许的范围内**，DJI 支持开发者使用PSDK 开发满足使用需求的负载设备，提升无人机在行业应用中的价值。
DJI **不支持**开发者使用PSDK 开发带有大规模杀伤性质的**武器**，或用于**伤害**和**破坏** 用途的设备；**DJI 不承担一切因使用PSDK 而导致的任何法律风险和责任**。

## 费用问题
##### 1. 使用PSDK 开发负载设备是否需要付费？
* 在开发模式下，开发者在购买开发负载设备的[硬件平台](../payloadguide/hardware.html)后，即可在[用户中心](https://developer.dji.com/user/apps/#all)免费下载并使用PSDK 开发负载设备；
* 从开发模式切换为量产模式时，开发者需要获取量产授权：
  * 首款负载（如开发者开发的第一款负载设备为探照灯）的终身授权费用为32000元（人民币）；
  * 之后每款负载（如开发者开发的第二款负载设备为喊话器）的终身授权费用为16000 元（人民币）。

##### 2. 开发负载设备是否必须购买硬件平台？
PSDK 硬件平台是使用PSDK 开发负载设备的必要工具，开发者可以根据实际的需要购买如下硬件平台，有关硬件平台的详细说明请参见[硬件平台](../payloadguide/hardware.html)。
* [X-Port](https://store.dji.com/cn/product/dji-x-port)标准云台
* [Payload SDK 开发套件 2.0](https://store.dji.com/cn/product/psdk-development-kit-v2)
* [Payload SDK 开发板套装](https://store.dji.com/cn/product/psdk-development-kit)
> **提示：** 当负载设备进入量产阶段后，开发者可购买硬件平台套装，如[DJI SKYPORT 转接环套装 V2](https://store.dji.com/cn/product/dji-skyport-adapter-set-v2) 或[DJI SKYPORT 转接环套装](https://store.dji.com/cn/product/dji-skyport-adapter-set) 降低负载设备批量生产的成本。

##### 3. 一个硬件平台是否可以开发多款负载设备？
* 为防止您因违规操作损毁负载设备或无人机，DJI **不建议**您使用同一个硬件平台开发多款负载设备。
* 若您仍使用同一个硬件平台开发多款负载设备，请先在[用户中心](https://developer.dji.com/user/apps/#all)重新注册负载设备，再使用DJI Assistant 2 将新的负载应用和PSDK 硬件平台重新绑定。