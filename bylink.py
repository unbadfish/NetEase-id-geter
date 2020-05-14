# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup as Soup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}


# you can add something else in

print_when_start = '''author:unbadfish@github
Copyright 2020 unbadfish@github
Licensed under the Apache License, Version 2.0
DO NOT use a ".../#/my/m/music/..."link
    Use a link like>>http://music.163.com/playlist?id=123456789
    DO NOT use a link like>>https://music.163.com/#/my/m/music/playlist?id=123456789
'''


def get_id(url):
    id_work = ''
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    doc = response.text
    work = Soup(doc, features='html.parser')
    '''--debug--
    file = open('work' + '.html', mode='w', encoding='utf-8')
    file.writelines(str(work.prettify()))  # can NOT be read by BeautifulSoup,but you can read it more clearly
    # file.writelines(str(work))  # can be read by BeautifulSoup
    # both files can NOT be read by explorer.Test in FireFox
    file.flush()
    file.close()
    # '''
    all_id = work.find_all('a', href=re.compile("/song\?id=[0-9]+"))
    '''all pages use <a href="/song?id=123456">...</a> to mark songs'''
    for one in all_id:
        link = one.get('href')
        match2 = re.match('^.*?/song\?id=([0-9]+).*?$', link)
        one_id = match2.group(1)
        id_work = id_work + one_id + ','
    out_id = id_work[0:-1]  # <<<<<<------
    if out_id != '':
        print(out_id)  # like>>1420663042,1423985980
    else:
        print('404 NOT FOUND')


print(print_when_start)
'''--debug--
get_id('http://music.163.com/playlist?id=123456789')
get_id('http://music.163.com/album?id=66666')
# the in_kind and in_id must be 'str' kind'''
while True:
    i = int(0)
    in_kind = None
    in_id = None
    print('Paste the link')
    user_in = input()
    if user_in.casefold() == 'bye':
        break
    try:
        get_id(user_in)
    except BaseException:
        print('Wrong input.Check again')
input('press ENTER key to exit')
