# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re
import json
import sys
import pyperclip

f_cookies = open(
    "F:\\Script\\Daily_Script\\Dev\\NetEase-id-geter\\cookies.txt", 'r')
# 0. 在【https://curl.trillworks.com/】 将网易云网页的curl命令转换为cookies
# 1. 为避免混乱，请尽量使用绝对路径
# 2. 将得到的cookies中倒数第二行('MUSIC_U': ...)最后的逗号删掉!
# 3. 将得到的cookies中第一行的【cookies = 】删掉,使文件以‘{’开头，以‘}’结尾
"""文件示范:
{
    'JSESSIONID-WYYY': 'asd',
    # ...
    'MUSIC_U': 'asd'
}
"""
cookies: dict = json.loads(f_cookies.read().replace('\'', '\"'))
f_cookies.close()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
}


def get_album_info(album_id: str) -> str:
    """
    用英文逗号(,)合并专辑中每首歌的id
    :param album_id: 专辑id(str)
    :return: 专辑中每首歌的id用英文逗号(,)合并后的结果
    """
    tittles: list = []
    song_ids: list = []
    response = requests.get(
        f'http://music.163.com/album?id={album_id}', headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    soup = bs(response.text, features='html.parser')
    # print(soup.prettify())
    """====debug====
    f_debug = open(f'album_{album_id}.html', 'w', encoding='utf-8')
    # f_debug = open(f'album_{album_id}.html', 'w', encoding='utf-8')
    f_debug.writelines(str(soup.prettify()))
    # """
    for each_tittle_div in soup.find_all('div', class_="tit"):
        # print(each_tittle_div)
        for each_tittle_tag in each_tittle_div.find_all('h2', class_="f-ff2"):
            # print(each_tittle_tag)
            if each_tittle_tag.string.parent == each_tittle_tag and each_tittle_tag.string is not None:
                # print('===is tittle:===\n', each_tittle_tag, '\n================')
                tittles.append(str(each_tittle_tag.string))
    # print(tittles)
    if len(tittles) == 1:
        print('标题匹配成功, 请核对:\n【' + tittles[0] + '】')
    elif len(tittles) > 1:
        print('匹配到多个标题, 可能是网易云页面布局改变或要查找的内容已被删除，请前往Issue页面,寻找解决方法或提出Issue\n'
              'Issue页面:http://github.com/unbadfish/NetEase-id-geter/issues')
        print('将显示所有疑似标题:\n【' + '】【'.join(tittles) + '】')
    else:
        print('未匹配到标题, 可能是网易云页面布局改变或要查找的内容已被删除，请前往Issue页面,寻找解决方法或提出Issue\n'
              'Issue页面:http://github.com/unbadfish/NetEase-id-geter/issues')

    for each_song_div in soup.find_all('div', id="song-list-pre-cache"):
        # print(each_song_div)
        for each_song_tag in each_song_div.find_all('a', href=re.compile(r"^/song\?id=\d+$")):
            # print(each_song_tag)
            if each_song_tag.string.parent == each_song_tag and each_song_tag.string is not None:
                song_id_match = re.match(
                    r"^/song\?id=(\d+)$", str(each_song_tag.get('href')))
                if song_id_match:
                    song_ids.append(str(song_id_match.group(1)))
    # print(song_ids)
    if len(song_ids) > 0:
        song_ids_string = ','.join(song_ids)
        print('歌曲id:\n' + song_ids_string)
        return song_ids_string
    else:
        print('未匹配到歌曲id, 可能是网易云页面布局改变或要查找的内容已被删除，请前往Issue页面,寻找解决方法或提出Issue\n'
              'Issue页面:http://github.com/unbadfish/NetEase-id-geter/issues')
        return ''


def get_playlist_info(playlist_id: str) -> str:
    """
    用英文逗号(,)合并歌单中每首歌的id
    :param playlist_id: 歌单id(str)
    :return: 歌单中每首歌的id用英文逗号(,)合并后的结果
    """
    tittles: list = []
    song_ids: list = []
    response = requests.get(
        f'http://music.163.com/playlist?id={playlist_id}', headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    soup = bs(response.text, features='html.parser')
    # print(soup.prettify())
    """====debug====
    f_debug = open(f'playlist_{playlist_id}.html', 'w', encoding='utf-8')
    # f_debug = open(f'playlist_{playlist_id}.html', 'w', encoding='utf-8')
    f_debug.writelines(str(soup.prettify()))
    # """
    for each_tittle_div in soup.find_all('div', class_="tit tit2"):
        # print(each_tittle_div)
        for each_tittle_tag in each_tittle_div.find_all('h2', class_="f-ff2 f-brk"):
            # print(each_tittle_tag)
            if each_tittle_tag.string.parent == each_tittle_tag and each_tittle_tag.string is not None:
                # print('===is tittle:===\n', each_tittle_tag, '\n================')
                tittles.append(str(each_tittle_tag.string))
    # print(tittles)
    if len(tittles) == 1:
        print('标题匹配成功, 请核对:\n【' + tittles[0] + '】')
    elif len(tittles) > 1:
        print('匹配到多个标题, 可能是网易云页面布局改变或要查找的内容已被删除，请前往Issue页面,寻找解决方法或提出Issue\n'
              'Issue页面:http://github.com/unbadfish/NetEase-id-geter/issues')
        print('将显示所有疑似标题:\n【' + '】【'.join(tittles) + '】')
    else:
        print('未匹配到标题, 可能是网易云页面布局改变或要查找的内容已被删除，请前往Issue页面,寻找解决方法或提出Issue\n'
              'Issue页面:http://github.com/unbadfish/NetEase-id-geter/issues')

    for each_song_div in soup.find_all('div', id="song-list-pre-cache"):
        # print(each_song_div)
        for each_song_tag in each_song_div.find_all('a', href=re.compile(r"^/song\?id=\d+$")):
            # print(each_song_tag)
            if each_song_tag.string.parent == each_song_tag and each_song_tag.string is not None:
                song_id_match = re.match(
                    r"^/song\?id=(\d+)$", str(each_song_tag.get('href')))
                if song_id_match:
                    song_ids.append(str(song_id_match.group(1)))
    # print(song_ids)
    if len(song_ids) > 0:
        song_ids_string = ','.join(song_ids)
        print('歌曲id:\n' + song_ids_string)
        return song_ids_string
    else:
        print('未匹配到歌曲id, 可能是网易云页面布局改变或要查找的内容已被删除，请前往Issue页面,寻找解决方法或提出Issue\n'
              'Issue页面:http://github.com/unbadfish/NetEase-id-geter/issues')
        return ''


def get_song_id(song_id: str) -> str:
    """
    返回单曲id
    :param song_id: 单曲id
    :return: 单曲id
    """
    # TODO 查询api, 查找歌曲有效性及信息
    print('您输入的是单曲, id:\n' + song_id)
    return song_id


def get_id(ori_kind: str, ori_id: str) -> str:
    """
    主函数
    :param ori_kind: 类型(str)
    :param ori_id: id(str)
    :return: 每首歌的id用英文逗号(,)合并后的结果
    """
    if ori_kind == 'album':
        return get_album_info(ori_id)
    elif ori_kind == 'playlist':
        return get_playlist_info(ori_id)
    elif ori_kind == 'song':
        return get_song_id(ori_id)
    else:
        print('程序执行有误, 请检查')
        return ''


reg_dict: dict = {r'^http[s]?://music\.163\.com/album\?id=(\d+)': 'album',
                  r'^http[s]?://music\.163\.com/playlist\?id=(\d+)': 'playlist',
                  r'^http[s]?://music\.163\.com/song\?id=(\d+)': 'song',

                  r'^http[s]?://music\.163\.com/#/album\?id=(\d+)': 'album',
                  r'^http[s]?://music\.163\.com/#/playlist\?id=(\d+)': 'playlist',
                  r'^http[s]?://music\.163\.com/#/song\?id=(\d+)': 'song',
                  r'^a([\d]+)$': 'album', r'^album([\d]+)$': 'album',
                  r'^p([\d]+)$': 'playlist', r'^playlist([\d]+)$': 'playlist',
                  r'^song([\d]+)$': 'song'}
print('''author:unbadfish@github
Here I declear that this program is written by MYSELF
Copyright 2020 unbadfish@github
Licensed under the Apache License, Version 2.0
======START======''')
# *debug
# print(get_album_info('96276728'))
# print(get_playlist_info('4866048742'))
# print(get_id('album', '96276728'))
# print(get_id('playlist', '4866048742'))

if len(sys.argv) == 1:
    # *Cycle mode
    while True:
        match_state: bool = False
        print('输入想要查找的内容')
        user_input: str = input()
        if user_input.casefold() == 'bye':
            break
        for each_reg in reg_dict.keys():
            match_input = re.match(each_reg, user_input)
            # print(match_input)
            if match_input:
                match_state: bool = True
                input_id = match_input.group(1)
                input_kind = reg_dict.get(each_reg)
                # print(input_kind, input_id)
                print(f'输入匹配成功, 将查询 {input_kind} {input_id} 的信息')
                pyperclip.copy(get_id(input_kind, input_id))
        if match_state is False:
            print('输入有误, 请检查后重输')
    input('press ENTER key to exit')
elif len(sys.argv) == 2 and sys.argv[1] != '-h':
    # *Arg mode
    match_state: bool = False
    for each_reg in reg_dict.keys():
        match_input = re.match(each_reg, sys.argv[1])
        # print(match_input)
        if match_input:
            match_state: bool = True
            input_id = match_input.group(1)
            input_kind = reg_dict.get(each_reg)
            # print(input_kind, input_id)
            print(f'输入匹配成功, 将查询 {input_kind} {input_id} 的信息')
            get_id(input_kind, input_id)
    if match_state is False:
        print('输入有误, 请检查后重输')
else:
    print('获取网易云id\n用法: \n1. 不带参启动，进入循环模式\n'
          '2. %s 【想要查找的内容】（已知Bug：网址含有\'&\'时会报错。不影响正常使用）' % sys.argv[0])
