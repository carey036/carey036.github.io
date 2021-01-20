---
title: Gridea主题修复
date: 2021-01-19
tags: Blog, Gridea, use.fontawesome.com
author: 星索
category: 杂项
summary: 解决Gridea主题中因含有use.fontawesome.com导致加载时间过长的问题
---
因use.fontawesome.com疑似被墙，所以调用all.css的主题会导致加载时间过长，导致博客访问速度变慢，下面是解决方案：


1. 打开Gridea，点击左下角设置![image-20210119123517166](.\images\image-20210119123517166.png)

2. 查看【站点源文件路径】，在资源管理器中打开路径
![image-20210119123553739](.\images\image-20210119123553739.png)
![image-20210119123611561](.\images\image-20210119123611561.png)

3. 依次点击[themes]->[正在使用的theme名称]->[templates]->[_blocks]或者[includes]![image-20210119123822628](.\images\image-20210119123822628.png)

4. 使用记事本打开[head.ejs]，找到【\<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous"\>】并删除![image-20210119124016496](.\images\image-20210119124016496.png)
5. 重新发布