---
title: 视频流传输
date: 2020-01-17
version: 2.0.0
keywords: [视频流传输]
---
## 概述
使用PSDK 提供的视频流传输控制功能，开发者**需要先实现**获取视频流文件码流的功能，按照[H.264编码格式](../guide/payload-criterion.html)对视频流编码，并结合视频的帧率等参数，调用指定的接口发送视频流数据；用户通过使用DJI Pilot 以及基于MSDK 开发的移动端APP，能够获取相机类负载设备上实时的视频数据。

> **相关参考**
> * 有关视频流格式的详细说明请参见[视频标准](../guide/payload-criterion.html)
> * 有关H.264 标准码流的相关参考请参见<a href="https://www.itu.int/rec/T-REC-H.264-201906-I/en">H.264 码流标准</a>
> * 仅基于Linux 开发的相机类负载设备支持视频流传输功能。

## 使用视频流传输功能

#### 1. 配置网络参数
为确保用户能够顺利获得相机类负载设备中的媒体文件，请以**手动**的方式设置相机类负载设备的网络参数：

* IP 地址：`192.168.5.3`
* 网  关 ： `192.168.5.1`
* 子网掩码：`255.255.255.0`

IP 地址设置完成后，使用`ping` 和`ifconfig` 命令查看相机类负载设备和飞机间的网络状态。

> **说明：** 若使用虚拟机调试相机类负载设备，请将虚拟机的网络适配器设置为桥接模式，并启用复制物理网络连接状态。

#### 2. 创建视频流处理线程
* 创建视频流处理线程     
为避免因其他任务阻塞视频流处理线程，导致视频流传输时出现花屏和绿屏的问题，请在使用PSDK 开发相机类负载设备时，单独创建视频流处理线程。

```c
    if (PsdkOsal_TaskCreate(&s_userSendVideoThread, UserCameraMedia_SendVideoTask, 2048, NULL) != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("user send video task create error.");
        return PSDK_RETURN_CODE_ERR_UNKNOWN;
    }
```
* 视频流处理线程初始化     
使用PSDK 开发的相机类负载设备在创建视频流处理线程后，需要先初始化线程状态并向相机类负载设备申请用于缓存视频流文件的内存空间。

```c
videoFilePath = PsdkOsal_Malloc(PSDK_MEDIA_FILE_PATH_LEN_MAX);
    videoFilePath = PsdkOsal_Malloc(PSDK_MEDIA_FILE_PATH_LEN_MAX);
    if (videoFilePath == NULL) {
        PsdkLogger_UserLogError("malloc memory for video file path fail.");
        exit(1);
    }

    transcodedFilePath = PsdkOsal_Malloc(PSDK_MEDIA_FILE_PATH_LEN_MAX);
    if (transcodedFilePath == NULL) {
        PsdkLogger_UserLogError("malloc memory for transcoded file path fail.");
        exit(1);
    }

    frameInfo = PsdkOsal_Malloc(VIDEO_FRAME_MAX_COUNT * sizeof(T_TestPayloadCameraVideoFrameInfo));
    if (frameInfo == NULL) {
        PsdkLogger_UserLogError("malloc memory for frame info fail.");
        exit(1);
    }
    memset(frameInfo, 0, VIDEO_FRAME_MAX_COUNT * sizeof(T_TestPayloadCameraVideoFrameInfo));
```

#### 3. 获取视频流文件信息
使用PSDK 开发的相机类负载设备在发送视频流文件前，须读取相机类负载设备本地的H.264 文件，获取视频流文件的信息。

* 读取相机类负载设备本地的H.264 文件       
用户指定负载设备上**准确的**H.264 文件所在的路径后，基于PSDK 开发的相机类负载设备通过系统接口，打开用户指定的视频流文件。
>**说明：** PSDK 的视频流传输功能仅支持传输H.264 格式的视频流文件，有关H.264 格式的标准详情请参见[“视频标准”](../guide/payload-criterion.html) 。

```c
    #define VIDEO_FILE_PATH    "../../../../../api_sample/camera_media_emu/media_file/PSDK_0006.h264"

    fpFile = fopen(VIDEO_FILE_PATH, "rb+");
    if (fpFile == NULL) {
        PsdkLogger_UserLogError("open video file fail.");
        exit(1);
    }
```

* 获取H.264 文件的信息        
基于PSDK 开发的相机类负载设备使用ffmpeg 读取指定的H.264 文件的帧率、帧信息和总帧数。
  * 帧率：相机类负载设备在1s 内可发送的帧的数量
  * 帧信息：H.264 视频流文件内一帧的起始位置和该帧的长度

```c
        psdkStat = PsdkPlayback_VideoFileTranscode(videoFilePath, "h264", transcodedFilePath,
                                                   PSDK_MEDIA_FILE_PATH_LEN_MAX);
        if (psdkStat != PSDK_RETURN_CODE_OK) {
            PsdkLogger_UserLogError("transcode video file error: %lld.", psdkStat);
            continue;
        }

        psdkStat = PsdkPlayback_GetFrameRateOfVideoFile(transcodedFilePath, &frameRate);
        if (psdkStat != PSDK_RETURN_CODE_OK) {
            PsdkLogger_UserLogError("get frame rate of video error: %lld.", psdkStat);
            continue;
        }

        psdkStat = PsdkPlayback_GetFrameInfoOfVideoFile(transcodedFilePath, frameInfo, VIDEO_FRAME_MAX_COUNT,
                                                        &frameCount);
        if (psdkStat != PSDK_RETURN_CODE_OK) {
            PsdkLogger_UserLogError("get frame info of video error: %lld.", psdkStat);
            continue;
        }

        psdkStat = PsdkPlayback_GetFrameNumberByTime(frameInfo, frameCount, &frameNumber,
                                                     startTimeMs);
        if (psdkStat != PSDK_RETURN_CODE_OK) {
            PsdkLogger_UserLogError("get start frame number error: %lld.", psdkStat);
            continue;
        }

```

#### 4. 视频流文件解析
基于PSDK 开发的相机类负载设备获取视频流文件的信息后，将解析视频流文件的内容，识别视频流文件的帧头。

```c
dataBuffer = calloc(frameInfo[frameNumber].size, 1);
        if (dataBuffer == NULL) {
            PsdkLogger_UserLogError("malloc fail.");
            goto free;
        }

        ret = fseek(fpFile, frameInfo[frameNumber].positionInFile, SEEK_SET);
        if (ret != 0) {
            PsdkLogger_UserLogError("fseek fail.");
            goto free;
        }

        dataLength = fread(dataBuffer, 1, frameInfo[frameNumber].size, fpFile);
        if (dataLength != frameInfo[frameNumber].size) {
            PsdkLogger_UserLogError("read data from video file error.");
        } else {
            PsdkLogger_UserLogDebug("read data from video file success, len = %d B\r\n", dataLength);
        }
```

#### 5. 发送视频流文件
基于PSDK 开发的相机类负载设备在解析视频流文件并识别视频流文件的帧头后，将以逐帧的方式发送视频流文件。
>**注意:** 基于PSDK 开发的相机类负载设备最长可发送的帧为65K，若帧的长度超过65k，则需拆解该帧发送。

```c
while (dataLength - lengthOfDataHaveBeenSent) {
            lengthOfDataToBeSent = USER_UTIL_MIN(DATA_SEND_FROM_VIDEO_STREAM_MAX_LEN,
                                                 dataLength - lengthOfDataHaveBeenSent);
            psdkStat = PsdkPayloadCamera_SendVideoStream((const uint8_t *) dataBuffer + lengthOfDataHaveBeenSent,
                                                         lengthOfDataToBeSent);
            if (psdkStat != PSDK_RETURN_CODE_OK) {
                PsdkLogger_UserLogError("send video stream error: %lld.", psdkStat);
                goto free;
            }
            lengthOfDataHaveBeenSent += lengthOfDataToBeSent;
        }
```

使用DJI Pilot 或基于MSDK 开发的移动端APP 向相机类负载设备发送视频流传输命令后，移动端APP 将能接收并循环播放相机类负载设备中的媒体文件。

#### 6.调整帧速率
使用PSDK 开发的相机类负载设备能够更新视频流发送的状态，方便用户调整视频流传输模块传输视频的帧速率。

```c
psdkStat = PsdkPayloadCamera_GetVideoStreamState(&videoStreamState);
        if (psdkStat == PSDK_RETURN_CODE_OK) {
            PsdkLogger_UserLogDebug(
                "video stream state: realtimeBandwidthLimit: %d, realtimeBandwidthBeforeFlowController: %d, busyState: %d.",
                videoStreamState.realtimeBandwidthLimit, videoStreamState.realtimeBandwidthBeforeFlowController,
                videoStreamState.busyState);
        } else {
            PsdkLogger_UserLogError("get video stream state error.");
        }

```
