---
title: Video Stream Transmission
date: 2020-01-17
version: 2.0.0
keywords: [Video Stream Transmission]
---
> **NOTE:** This article is **Machine-Translated**. If you have any questions about this article, please send an <a href="mailto:dev@dji.com">E-mail </a>to DJI, we will correct it in time. DJI appreciates your support and attention.

## Overview
Before developed the video stream transmission for the payload, the developer needs to develop the function to get the video stream by themselves, according to the [H.264 Format](../guide/payload-criterion.html), after registered the function in the specified interfaces of the PSDK, user use DJI Pilot and Mobile APP which developed based on MSDK could control the payload to transfer the video stream to DJI Pilot or Mobile APP developed based on MSDK.  

> **Reference**
> * The details of the video stream format please refer to [Video Criterion](../guide/payload-criterion.html)
> * The details of the H.264 criterion please refer to <a href="https://www.itu.int/rec/T-REC-H.264-201906-I/en">H.264 Criterion</a>
> * The camera-type payload developed on the Linux could use the video stream transmission function.

## Develope with Video Stream Transmission

### 1. Network Configuration
To convenience the user to obtain the media file in the payload which developed on Linux, please set the parameters of the network, after that please use the command `ping` and `ifconfig` check the network.

* IP:`192.168.5.3`
* Gate:`192.168.5.1`
* Mask: `255.255.255.0`

> **NOTE:** Use the virtual machine to debug the camera-type payload, the developer should set the mode of the virtual machine's network is bridge mode and enable the function "Replicate physical network connection status".

### 2. Created the thread to handle the video stream
* Created the thread     
To avoid blocking the video stream processing thread from other tasks, please create the thread to handle the video stream when develope the camera-type payload based on PSDK.

```c
    if (PsdkOsal_TaskCreate(&s_userSendVideoThread, UserCameraMedia_SendVideoTask, 2048, NULL) != PSDK_RETURN_CODE_OK) {
        PsdkLogger_UserLogError("user send video task create error.");
        return PSDK_RETURN_CODE_ERR_UNKNOWN;
    }
```
* Initialization the thread   
After create the thread to handle the video stream, please initialize the thread and apply the free space to caching the video files.

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

### 3. Get the information of the video stream
Before sending the video stream from the payload which developed based on PSDK, please read the H.264 video files and obtain the information of those files.

* Read the H.264 files       
After get the path of the video files that the user-specified, the payload needs to use the system interface to open the media file.
>**NOTE:** The video stream transmission function of the payload which developed based on PSDK only could transfer the H.264 files, for details please refer to ["Video Criterion"](../guide/payload-criterion.html) 。

```c
    #define VIDEO_FILE_PATH    "../../../../../api_sample/camera_media_emu/media_file/PSDK_0006.h264"

    fpFile = fopen(VIDEO_FILE_PATH, "rb+");
    if (fpFile == NULL) {
        PsdkLogger_UserLogError("open video file fail.");
        exit(1);
    }
```

* Get the information of the H.264 files        
The camera-type payload which developed based on PSDK uses FFmpeg to read the H.264 file's frame rate and frame information.
  * Frame rate: the number of frames that were sent by the camera-type payload in 1s.
* Frame information: the start position and the length of a frame which in the H.264 files.

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

### 4. Analysis the video file
After obtained the information of the video files, the camera-type payload which developed based on PSDK will identify the frame header of the video files.

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

### 5. Send the video files
The camera-type payload which developed based on PSDK sends the video file frame by frame according to the information of the frame.

>**NOTE:** The maximum length of the frame is 65K, over this value, the video file will be disassembled。

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
Use DJI Pilot or the Mobile APP developed based on MSDK could receive and play the media files which in the camera-type payload in the loop.

### 6. Adjust the frame rate
To convenient users to adjust the frame rate of video transmitted by the video stream transmission function the camera-type payload developed based on PSDK can update the status of video stream transmission.

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
