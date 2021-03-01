---
title: 使用Github Action 部署RSS2MOBI并发送到kindle
date: 2021-02-25
tags: github, github action, rss, kindle
author: 星索
category: 计算机
summary: 使用Github Action 部署RSS2MOBI并发送到kindle
---

## 说明

之前一直是使用的kindleear，但后来发现kindlear有时候抓取的内容并不理想（版本很久了），更新的时候提示GAE需要绑定信用卡，但无奈暂时没有申请信用卡，故使用本项目进行RSS2MOBI。

## 准备

1. 项目地址 https://github.com/carey036/GenBooks.git
2. github账号
3. 一个支持smtp的邮箱（仅测试过outlook，其他邮箱如果问题请提交Issues
4. RSS订阅地址

## 开始操作

1、fork本项目https://github.com/carey036/GenBooks.git![forkl](.\images\forkl.jpg)

2、 在已经fork好的项目里面，依次点击Setting -> Secrets -> New repository secret![secret](.\images\secret.jpg)

3、 配置文件

```json
{
       "title":"RSSDaily - GenBook",
       "feeds":[
           {
               "name":"知乎热榜",
               "url":"https://rsshub",
               "saveimg":false,
               "imgquality":100
           },
           {
               "name":"example",
               "url":"https://最后一个不要写逗号/",
               "saveimg":false,
               "imgquality":100,
               "css":""
           }
       ],
       "note":"请按照本格式书写feed源,saveimg是意思是是否保存图片（保存图片可能会导致排版错误），imgquality为压缩图片的比例，100表示不压缩，图片过多时，不压缩会导致文件较大",
       "emailinfo":{
           "note":"是否通过邮件发送",
           "enable":false,
           "to":"the email you want to receive",
           "from":"your email",
           "smtp":"you email smtp serve adress",
           "port":25,
           "pwd":"your pwd",
           "note2":"是否上传epub或者mobi，仅当enable为true时可用，webdav同",
           "epub":true,
           "mobi":true
       },
       "webdav":{
           "enable":false,
           "server":"https://dav.jianguoyun.com/dav/",
           "user":"@189.cn",
           "pwd":"",
           "epub":true,
           "mobi":true
       },
       "telegram":{
           "enable":false,
           "token":"",
           "chat_id":"",
           "epub":true,
           "mobi":true
       },
       "Github":{
           "enable":false,
           "epub":false,
           "mobi":false
       }
   }
```
   修改上面的title，feeds，emailinfo，如果想通过其他方式上传，也可以修改对应的配置

| 项目      | 说明                            |
| --------- | ------------------------------- |
| title     | 生成的mobi杂志名称              |
| feeds     | 你的订阅信息，其中css为可选选项 |
| emailinfo | kindle订阅信息                  |

   feeds说明

| key        | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| name       | 【必须】该订阅的名称，显示在目录中                           |
| url        | 【必须】订阅的url地址                                        |
| saveimg    | 【必须】是否保存rss订阅中的图片，true/false                  |
| imgquality | 【必须】图片压缩比例，100为不压缩，输入1-100整数即可         |
| css        | 【可选】转换为书籍时如果有显示错误，如部分字体过小过大，可通过css调节 |

   email说明

| key    | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| enable | 【必须】是否启用邮件发送，true/false                         |
| to     | 【必须】你的kindle收件箱/你想接受文件的邮箱                  |
| from   | 【必须】你的邮箱                                             |
| smtp   | 【必须】smtp服务器地址                                       |
| port   | 【必须】smtp服务器端口                                       |
| pwd    | 【必须】smtp服务器的密码，一般为邮箱密码，qq邮箱可能有所不同 |
| epub   | 【必须】是否发送epub，true/false                             |
| mobi   | 【必须】是否发送mobi，true/false                             |

   **请根据以上信息自行配置文件，然后复制整个文件备用**

4、建三个secret，name填上图三个即可，对应的Value为下表

| Name        | Value                                              |
| ----------- | -------------------------------------------------- |
| CONFIG      | 第三步中设置好的配置文件                           |
| GITHUBEMAIL | 登录github时使用的邮箱                             |
| GITHUBUSER  | 你的github用户名，点击头像，显示的Signed in as XXX |

5、登录z.cn/myk，点击 首选项 -> 个人文档设置 -> 已认可的发件人电子邮箱列表，添加你的邮箱

6、点击github中的 Action， 启用action，然后点击star，项目就已经完全配置好了。稍后就能收到kindle的推送了

## 额外操作

### 修改封面

替换代码文件中的 /config/cover.jpg，即可替换封面。注意：图片过大可能会导致生成文件体积过大

### 修改推送时间

修改代码文件中.github/workflows/jobs.yml的 - cron: 后面的数字，以修改时间

![time](.\images\time.jpg)

默认为早上六点和下午6点各推送一次