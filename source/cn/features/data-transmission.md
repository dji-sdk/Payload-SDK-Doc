---
title: Payload SDK 功能 - 数据传输
date: 2019-06-17
keywords: [introduction, overview, Payload SDK]
---

## 数据透传 (UART/CAN)


数据透传功能允许您在 Payload sdk 和 Mobile SDK 之间发送自定义数据流。

- 该通道从负载接收 UART / CAN 上的数据。
- 该通道不会对数据执行任何加密; 它会透明地在 PSDK 和 MSDK 之间传输数据。
- 它允许开发人员开发在 MSDK 上解释这些数据的协议。
- 此功能类似于 Onboard SDK 的[数据透明传输](https://developer.dji.com/onboard-sdk/documentation/guides/component-guide-mobile-communication.html) 功能。
 
#### 数据带宽指标
在以下带宽内通过 UART / CAN 端口直接在 Mobile SDK 和 SKYPORT 之间传输数据：

<table id="t01">
  <thead>
    <tr>
      <th>链路</th>
      <th>指标</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>上行链路 (从 Mobile SDK 到 Payload)</th>
      <td>约 500B/s </td>        
    </tr>
    <tr>
      <td>下行链路 (从 Payload 到 Mobile SDK)</th>
      <td>约 4KB/s </td>        
    </tr>
  </tbody>
</table>


## 网络流数据传输 (UDP)

网络流传输功能允许负载通过 UDP 协议发送大量的下行数据到 Mobile SDK。

#### 视频数据传输
- 网络流通道通过在 Mobile SDK 中提供本地视频解码和显示，大大简化了视频传输，而无需在 MSDK 上进行任何编码开发。
- 要利用此功能，您的负载必须将您的视频数据编码为特定格式并将其发送到特定端口（详细信息在下面给出）。
- 如果您的视频数据格式正确，所有使用 DJI MSDK 的 iOS 和 Android 应用程序都可以在不更改代码的情况下显示此视频。
- 这也可以实现与现有移动应用的向后兼容，并大大增强了与 DJI 相机和平台的互操作性。

#### 非视频数据传输
- 如果您有需要传输大量非视频流数据，PSDK 也会为您提供该选项。
- 您的负载可以通过 UDP 协议将任何数据发送到与视频网络端口不同的网络端口，并且您需要在 Mobile SDK 应用上实施解码来解析此数据。

#### 网络端口带宽指标
网口数据传输的带宽信息提供如下：

<table id="t01">
  <thead>
    <tr>
      <th>使用条件</th>
      <th>总带宽 (下行数据 + 码流)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M200 系列仅使用第三方负载。</th>
      <td>最大理论带宽 8Mbps。</td>        
    </tr>
    <tr>
      <td>M210 及 M210 RTK 双云台版本, 挂载 DJI 云台和第三方负载。</th>
      <td>最大理论带宽 4Mbps。</td>        
    </tr>
  </tbody>
</table>


## 比较：数据透传和网络流数据传输

- 通常，对于少量数据，请使用数据透传通道。
- 网络链路提供了更高的带宽，但这需要额外开发，因为您需要将数据打包到UDP数据包中。
- 对于视频传输，网络流是更好的选择。
- 如果您需要可靠的数据传输，建议选用数据透传通道。
