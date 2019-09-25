---
title: 网络端口指南
date: 2019-06-17
keywords: [介绍]
---

## 网络端口配置
使用网络端口传输码流和数据时，配置网络端口网络属性如下：

- IP 地址: 192.168.5.3
- 子网掩码: 255.255.255.0
- 默认网关: 192.168.5.1

## 下行链路数据传输
网络端口通过使用 UDP 协议将下行链路数据（即从 PSDK 到 MSDK ）往 IP 192.168.5.10 ，端口 23002 发送。

## 视频传输
网络端口使用 UDP 协议将视频流往 IP 192.168.5.10，端口 23003 发送。
视频流的要求如下：

- H.264 标准码流
- Baseline/ Main / High Profile（H.264 标准 7.3.2.1.1 中 profile_idc 可选范围为 66/77/100）
- Level Number 不能大于 5.1
- YUV420 格式（H.264 标准 7.3.2.1.1 中 chroma_format_idc 等于 1）
- 8Bit 视频（H.264 标准 7.3.2.1.1 中 bit_depth_luma_minus8 等于 0，bit_depth_chroma_minus8 等于 0）
- 不允许编码器自定义 scaling matrix（H.264 标准 7.3.2.1.1 中 seq_scaling_matrix_present_flag 等于 0，H.264 标准 7.3.2.2 中 pic_scaling_matrix_present_flag 等于 0）
- 仅支持帧格式编码，不支持场编码（H.264 标准 7.3.2.1.1 中 frames_mbs_only_flag 等于 1）
- 仅允许 P 帧和 I 帧，仅允许 P 帧有单个参考帧（H.264 标准 7.3.3 中 slice_type 等于 0 或者 2，H.264 标准 7.3.2.2 中 num_ref_idx_l0_default_active_minus1 必须被解码为 0，H.264 标准 7.3.3 中 num_ref_idx_active_override_flag 等于 0）
- 不支持多 slice group（H.264 标准 7.3.2.2 中 num_slice_groups_minus1 等于 0）
- gop structure 为 Period I，所有 I 帧必须为 IDR 帧，若 gop structure 不符合要求，不保证图传能够从丢包错误中恢复
- Period I 结构中建议 1 秒 1 个 IDR 帧
- 建议视频最大分辨率为 1920*1080
- 建议最大帧率不超过 30fps
- 推荐视频长宽比为 4：3，保证使用 DJI CrystalSky 时画面可以铺满屏幕

开发者可以参考视频流传输例程（Payload_SDK / sample / network_port）。
