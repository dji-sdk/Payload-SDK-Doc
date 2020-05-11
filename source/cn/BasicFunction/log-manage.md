---
title: 日志管理
date: 2020-05-08
version: 2.1.0
keywords: [Payload SDK, 日志, 日志颜色, 日志标识]
---
## 概述
PSDK 的日志管理功能支持通过如串口、终端或USB 等日志输出方法，输出Debug、Info、Warn和Error 四种类型的日志；使用能够显示日志颜色的终端工具，如Putty 等能够以不同的颜色显示不同类型的日志。        
基于PSDK 开发的负载设备输出的日志结构如下：日志颜色起始符 + 系统时间 + 模块名称 + 日志等级标识 + 日志内容 + 日志颜色结束符  
## 基础概念
#### 日志标识符
使用**不支持**显示日志颜色的调试工具查看日志时，会显示日志的颜色标识符。  
* 日志颜色：不同类型的日志，其标识颜色也不同。XShell、SecureCRT及Putty 等工具能够根据日志的等级，以不同的颜色显示不同类型的日志。 

* 日志颜色起始标识符：
	* 黑色：`\033[30m`、红色：`\033[31m`、绿色：`\033[32m`  
	* 黄色：`\033[33m`、蓝色：`\033[34m`、紫色：`\033[35m`  
    * 青色：`\033[36m`、白色：`\033[37m`  
* 日志颜色结束标识符：`\033[0m`  

#### 日志信息
* 系统时间：负载设备上电时，负载设备的时间为负载设备系统的时间，当负载设备与无人机完成时间同步后，负载设备的时间将与无人机的时间同步(ms)。
* 模块名称：PSDK 模块的名称（该名称无法被修改），用户打印接口的模块名称为“module_user”。
* 日志内容：单条日志最多不超过500 个字节（bytes）。
* 日志等级：日志的等级从高到低为Debug、Info、Warn和Error，日志管理功能模块可打印不高于指定等级的所有日志。  
  <div><div><p>表1. 日志等级说明</p></div><div>
	<table>
	<thead>
	<tr>
		<td>日志等级</td>
		<td>日志内容</td>
		<td>输出接口</td>
		<td>日志颜色</td>
	</tr>
	</thead>
	<tbody>
	<tr>
		<td>Debug - 4</td>
		<td>调试信息</td>
		<td>PsdkLogger_UserLogDebug</td>
		<td>White</td>
	</tr>
	<tr>
		<td>Info - 3</td>
		<td>关键信息</td>
		<td>PsdkLogger_UserLogInfo</td>
		<td>Green</td>
	</tr>
	<tr>
		<td>Warn - 2</td>
		<td>警告信息</td>
		<td>PsdkLogger_UserLogWarn</td>
		<td>Yellow</td>
	</tr>
	<tr>
		<td>Error - 1</td>
		<td>系统错误</td>
		<td>PsdkLogger_UserLogError</td>
		<td>Red</td>
	</tr>
	</tbody>
</table></div></div>

## 使用日志管理功能
使用PSDK 日志管理功能，需要先初始化日志打印接口，设置日志等级，通过注册日志打印函数，实现日志管理功能。

> **说明：** 本教程以“使用STM32 在RTOS 系统上通过串口打印日志信息”为例，介绍使用日志管理功能的方法和步骤。

##### 1. 初始化串口并注册日志输出方法
在RTOS 系统上使用PSDK 开发负载设备的日志管理功能时，建议使用串口打印日志信息。 

```c
static T_PsdkReturnCode PsdkUser_Console(const uint8_t *data, uint16_t dataLen)
{
    UART_Write(PSDK_CONSOLE_UART_NUM, (uint8_t *) data, dataLen);
    return PSDK_RETURN_CODE_OK;
}

UART_Init(PSDK_CONSOLE_UART_NUM, PSDK_CONSOLE_UART_BAUD);
```

##### 2. 注册日志打印接口
使用PSDK 的日志管理功能，需要初始化日志打印方法`printConsole`，设置所需打印的日志等级和该日志对应的打印方法，并通过`PsdkLogger_AddConsole()`注册到负载设备控制程序中。
> **注意：** 使用PSDK 开发的负载设备最多支持使用**8种**日志打印方法。

```c
T_PsdkLoggerConsole printConsole = {
    .consoleLevel = PSDK_LOGGER_CONSOLE_LOG_LEVEL_INFO,
    .func = PsdkUser_Console,
};

if (PsdkLogger_AddConsole(&printConsole) != PSDK_RETURN_CODE_OK) {
    printf("psdk add console print error");
    return PSDK_RETURN_CODE_ERR_UNKNOWN;
}
```

##### 3. 输出日志信息
调用日志打印函数输出日志信息，日志输出结果如 图1.日志信息 所示。

```
PsdkLogger_UserLogError("psdk log console test.");
PsdkLogger_UserLogWarn("psdk log console test.");
PsdkLogger_UserLogInfo("psdk log console test.");
PsdkLogger_UserLogDebug("psdk log console test.");
```

<div>
<div style="text-align: center"><p>图1.日志信息 </p>
</div>
<div style="text-align: center"><p><span>
      <img src="../../images/log.png" width="500" alt/></span></p>
</div></div>

> **说明：** 日志的等级为Info，因此负载设备中类型为Info、Warn 及Error 的日志将被输出在终端上，类型为Debug 的日志将不会被打印出来。

## 日志查看

* Linux：
  * 在Clion IDE 上使用 [Grep Console](https://plugins.jetbrains.com/plugin/7125-grep-console/)可过滤负载设备的日志文档
  * 使用grep命令：在终端中执行`./demo_linux_ubuntu | grep 'Info'`过滤所需的日志信息，更多使用方法请使用`man grep`查询

* RTOS：使用串口查看工具如SecureCRT、XShell或Putty 等工具查看日志信息

