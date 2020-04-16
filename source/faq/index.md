---
title: FAQ For PSDK 
date: 2020-01-17
keywords: [FAQ,]
---
Use the <a href="https://djisdksupport.zendesk.com/hc/en-us/community/topics">DJI technical support community</a> was recommend . If your problem cannot be solved or there are other questions, please use the <a herf="https://formcrafts.com/a/dji-developer-feedback-en">problem feedback form</a> to feedback the problem, or sent an <a href="mailto:dev@dji.com">Email</a> to DJI SDK.

## Basic

##### 1. Which drone is Payload SDK compatible with?
Payload SDK currently only supports the Matrice 200 series and Matrice 200 V2 series. For details, please refer to the [Parameter Comparison Page](https://www.dji.com/en/products/compare-m200-series?site=brandsite&from=nav).     
DJI provides X-Port, SkyPort V2 and SkyPort that are compatible with Matrice 200 series and Matrice 200 V2 series. Please read the [Payload Criterion](https://developer.dji.com/payload-sdk/documentation/guide/payload-criterion.html) carefully before developing the payload and purchasing the drone.     

##### 2. What is Development Mode? 
* <a href="https://developer.dji.com/payload-sdk/apply/" target="_blank">Resigned</a> as an user of the PSDK, the developer's mode is the Development Mode.
* In Development Mode, developers can bind 9 payload APPs totally.

##### 3. What is Production Mode?
* After obtaining the DJI SDK's license, the mode is Production Mode.
* In Production Mode, developers can bind an unlimited number of payloads.
* To obtain the license from <a href="mailto:dev@dji.com">DJI </a> , please send the following information for review:
  * Business License (scanned)
  * Payload Proposal: such as Scenarios, Usage Methods, and Ky Functions;
  * Details of the payload: such as Parameters, Sketches, Prototype Photos, etc.
  
>**NOTE：** It's no means that the payload has been certified by DJI, when the developer obtain the License.

##### 4. What kinds of payload does PSDK suppor？
DJI encourages developers to develop the payload which has add-on functionalities of the drone, not including any **weapon or equipment used for destruction**. Any consequence, legal risk, and responsibility brought by the payload have to be taken by the developer themselves.

## Purchase
##### 1. Do I need to pay for using PSDK?
* In Development Mode, developers use PSDK to develop the payload is free，but not for the Hardware;
* When switched from Development Mode to Production Mode, developers need to obtain licenses:
  * For the first payload（for example, the first payload developed by the developer is a searchlight） is $ 5,000;
  * The license fee for fellow payload (for example, the second payload developed by the developer is a megaphone） is $ 2,500.

##### 2. Do I must have to purchase a Hardware Platform to develop payload?
The Hardware Platform is an essential tool to develop the payload based on PSDK. Developers can purchase following Hardware Platforms according to needs:
* [X-Port](https://store.dji.com/product/dji-x-port) 
* [Payload SDK Development Kit 2.0](https://store.dji.com/en/product/psdk-development-kit-v2)
* [Payload SDK Development Kit](https://store.dji.com/en/product/psdk-development-kit)
>**NOTE：** After enters the production Mode , developers can purchase Hardware Platform packages, such as [DJI SKYPORT Adapter Ring Package V2](https://store.dji.com/en/product/dji-skyport-adapter-set-v2) or [DJI SKYPORT Adapter Ring SET](https://store.dji.com/en/product/dji-skyport-adapter-set), to reduce the cost.

##### 3. Could I use the same Hardware Platform to develop multiple payloads?    
* To prevent you from damaging the payload or drone due to illegal operations, DJI does not recommend that you develop multiple payloads equipment using the same Hardware Platform.
* If you still use the same Hardware Platform to develop multiple payloads, please re-register the payload Application in the [user center](https://developer.dji.com/user/apps/#all), and then use DJI Assistant 2 to re-bind the new payload application with the PSDK Hardware Platform.