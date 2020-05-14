# NatEast-id-geter
网易云歌单&amp;专辑歌曲ID提取器

## 使用方法

+ mainway:输入歌单或专辑的网址等，对应关系如下

    ```python
    in_search_dict = {'^.*?playlist.*?([0-9]+).*$': 'playlist', '^.*?album.*?([0-9]+).*$': 'album', '^list.*?([0-9]+).*$': 'playlist', '^p([0-9]+)$': 'playlist', '^a([0-9]+)$': 'album'}
      # ...
    While True:
          # ...
        for each_str in list(in_search_dict.keys()):
            in_match = re.match(each_str, user_in)
            if in_match:
                in_kind = in_search_dict.get(each_str)  # get the value
                in_id = in_match.group(1)  # use re
    ```

+ bylink:输入歌单或专辑的网址，主要的作用是网易云防止哪天偷偷改歌单和专辑的网址……不过这个对输入的要求更加严格：

    > ‘’’DO NOT use a ".../#/my/m/music/..."link
    >     Use a link like>>http://music.163.com/playlist?id=123456789
    >     DO NOT use a link like>>https://music.163.com/#/my/m/music/playlist?id=123456789‘’’
    >
    > (代码原注释)

+ byjsonfull:输入“字符串”(见str-get.md)

+ byjsonshort:输入“短字符串”(见str-get.md)

+ byre:输入“字符串”或“短字符串”(见str-get.md)

## 依赖环境

Python(这不是废话吗)

BeautifulSoup4

+ 使用`pip install beautifulsoup4`安装

<u>如有使用.exe可执行文件的需要，欢迎提出issue并附上邮箱地址，exe文件是真的大……</u>

## 原理简述

使用requests获取网页，使用BeautifulSoup解析

当然byjson和byre就没有获取网页的过程了

## 友情链接

这个项目是我给[163MusicLyrics](https://github.com/jitwxs/163MusicLyrics)写的配套小程序

链接:https://github.com/jitwxs/163MusicLyrics