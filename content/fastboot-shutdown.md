---
title: 【记录】fastboot接入电脑后出现press any key to shutdown
date: 2021-03-10
tags: android
author: 星索
category: 杂项
summary: fastboot接入电脑后出现press any key to shutdown
---

#

## 背景

在刷rec的时候手机出现问题，无法进入系统，且fastboot接入电脑后手机出现press any key to shutdown，导致无法刷入rec。

在多次更换驱动，尝试安装各大品牌手机助手后，问题仍然没有得到解决。

在百度贴吧找到如下解决办法，未防止以后再次出现此情况，遂记录。

> https://tieba.baidu.com/p/6119443977?pn=2 60楼

## 解决办法

```bash
@echo off
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags\18D1D00D0100" /v "osvc" /t REG_BINARY /d "0000" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags\18D1D00D0100" /v "SkipContainerIdQuery" /t REG_BINARY /d "01000000" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\usbflags\18D1D00D0100" /v "SkipBOSDescriptorQuery" /t REG_BINARY /d "01000000" /f


pause
```

新建文本文档，复制如上代码，重命名为1.bat, 以管理员方式运行