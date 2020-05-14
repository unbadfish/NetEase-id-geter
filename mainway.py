# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup as Soup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

in_search_dict = {'^.*?playlist.*?([0-9]+).*$': 'playlist', '^.*?album.*?([0-9]+).*$': 'album',
                  '^list.*?([0-9]+).*$': 'playlist', '^p([0-9]+)$': 'playlist',
                  '^a([0-9]+)$': 'album'}
# you can add something else in

print_when_start = '''author:unbadfish@github
Here I declear that this program is written by MYSELF
Copyright 2020 unbadfish@github
Licensed under the Apache License, Version 2.0
'''


def get_id(kind, content):
    id_work = ''
    if kind == 'playlist':
        response = requests.get('https://music.163.com/playlist?id=' + content, headers=headers)
        response.encoding = 'utf-8'
        doc = response.text
        work = Soup(doc, features='html.parser')
        # ------
        tittle = work.find_all('h2', class_='f-ff2 f-brk')
        '''I noticed that only playlists' tittle use <h2 class="f-ff2 f-brk">......</h2>
        and its parent tag is <div class="tit">(<h2>)...(<h2>)</div>
        interesting'''
        if str(tittle) != '[]':
            out_tittle = tittle[0].string  # <<<<<<------
        else:
            out_tittle = ''
        all_id = work.find_all('a', href=re.compile("/song\?id=[0-9]+"))
        '''all pages use <a href="/song?id=123456">...</a> to mark songs'''
        for one in all_id:
            link = one.get('href')
            match2 = re.match('^.*?/song\?id=([0-9]+).*?$', link)
            one_id = match2.group(1)
            id_work = id_work + one_id + ','
        out_id = id_work[0:-1]  # <<<<<<------
        if out_tittle != '' and out_id != '':
            print(out_tittle)
            print(out_id)  # like>>1420663042,1423985980
        else:
            print('404 NOT FOUND')
    elif kind == 'album':
        response = requests.get('http://music.163.com/album?id=' + content, headers=headers)
        response.encoding = 'utf-8'
        doc = response.text
        work = Soup(doc, features='html.parser')
        # ------
        tittle = work.find_all('h2', class_='f-ff2')
        '''I noticed that only albums' tittle use <h2 class="f-ff2">...</h2>
        and its parent tag is <div class="tit">(<h2>)...(<h2>)</div>
        interesting'''
        if str(tittle) != '[]':
            out_tittle = tittle[0].string  # <<<<<<------
        else:
            out_tittle = ''
        all_id = work.find_all('a', href=re.compile("/song\?id=[0-9]+"))
        '''all pages use <a href="/song?id=123456">...</a> to mark songs'''
        for one in all_id:
            link = one.get('href')
            match3 = re.match('^.*?/song\?id=([0-9]+).*?$', link)
            one_id = match3.group(1)
            id_work = id_work + one_id + ','
        out_id = id_work[0:-1]  # <<<<<<------
        if out_tittle != '' and out_id != '':
            print(out_tittle)
            print(out_id)  # like>>1420663042,1423985980
        else:
            print('404 NOT FOUND')
    else:
        print('Wrong kind.Try again')
    '''--debug--
    file = open(kind + content + '.html', mode='w', encoding='utf-8')
    # file.writelines(str(work.prettify()))  # can NOT be read by BeautifulSoup,but you can read it more clearly
    file.writelines(str(work))  # can be read by BeautifulSoup
    # both files can NOT be read by explorer.Test in FireFox
    file.flush()
    file.close()
    # '''


print(print_when_start)
'''--debug--
get_id('playlist', '123456789')
get_id('album', '66666')
# the in_kind and in_id must be 'str' kind'''
while True:
    i = int(0)
    in_kind = None
    in_id = None
    print('Paste the share link')
    user_in = input()
    if user_in.casefold() == 'bye':
        break
    print('Checking info...')
    for each_str in list(in_search_dict.keys()):
        in_match = re.match(each_str, user_in)
        if in_match:
            in_kind = in_search_dict.get(each_str)  # get the value
            in_id = in_match.group(1)  # use re
            print(in_kind.capitalize() + 'id:' + in_id)
            break
        else:
            i = i + 1
            # print(i)
    if i == len(in_search_dict) and in_kind is None and in_id is None:
        print('Wrong input.Check again')
    else:
        get_id(in_kind, in_id)
input('press ENTER key to exit')
