# NetEase-id-geter
网易云歌单&amp;专辑歌曲ID提取器

## 使用方法

1. 不带参启动，进入循环模式

2. 【py文件路径】 【想要查找的内容】（中间有空格）（已知Bug：网址含有'&'时会报错。<u>不影响正常使用</u>）

3. 【py文件路径】 -h 查看使用方法

## 关于cookies

requests.get并未考虑cookies，根据用户的反馈情况，未登陆的情况下只能获取10首歌。

请前往[这里](https://curl.trillworks.com/)获得cookies

0. 在【https://curl.trillworks.com/】 将网易云网页的curl命令转换为cookies

1. 为避免混乱，cookies文件请尽量使用绝对路径

2. 将得到的cookies中倒数第二行('MUSIC_U': ...)最后的逗号删掉!

3. 将得到的cookies中第一行的【cookies = 】删掉,使文件以‘{’开头，以‘}’结尾

4. 文件示范

    ```json
    {
        'JSESSIONID-WYYY': 'asd',
        # ...
        'MUSIC_U': 'asd'
    }
    ```

## 友情链接

这个项目是我给[163MusicLyrics](https://github.com/jitwxs/163MusicLyrics)写的配套小程序

链接:https://github.com/jitwxs/163MusicLyrics

## 更新日志
2021-08-24 重构。"优化"了cookies。老版本请前往old文件夹查看

2020-07-15 增加cookies的获得要求

2020-05-14 首个版本
