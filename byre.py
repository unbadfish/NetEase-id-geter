# -*- coding: UTF-8 -*-

import re

'''
Copyright 2020 unbadfish@github
Licensed under the Apache License, Version 2.0
'''


def get_id_re(in_string):
    id_work = ''
    try:
        match1 = re.finditer('"id":([0-9]+,)"v":[0-9]*?,"alg":[a-z]+?', in_string)  # find all
        for each_match in match1:
            each_id = each_match.group(1)
            id_work = id_work + each_id
        out_id = id_work[0:-1]
        print(out_id)  # like>>1420663042,1423985980
    except BaseException:
        print('Try again.You should input a string like:')
        print('{"trackIds":[{"id":1420663042,"v":5,"alg":null},{"id":1423985980,"v":6,"alg":null}]}')


while True:
    # in_str = '{"trackIds":[{"id":1420663042,"v":5,"alg":null},{"id":1423985980,"v":6,"alg":null}]}'
    # print(get_id_re(in_str))
    # test string
    print('Paste the string')
    user_in = input()
    if user_in.casefold() == 'bye':
        break
    get_id_re(user_in)
    # break
