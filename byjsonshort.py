# -*- coding: UTF-8 -*-

import json

'''
Copyright 2020 unbadfish@github
Licensed under the Apache License, Version 2.0
'''


def get_id_json(in_string):
    id_work = ''
    try:
        json_str = json.loads(in_string)
        # print(json_str)  # Then you can see that all 'null' values are changed to 'None'
        dicts_work1 = json_str.get('trackIds')  # dicts_work1 is a list of many dicts
        for each_dict in dicts_work1:
            each_id = each_dict.get('id')  # There must be two quotation marks
            id_work = id_work + str(each_id) + ','
        out_id = id_work[0:-1]
        print(out_id)  # like>>1420663042,1423985980
    except BaseException:
        print('Try again.You should input a string like:')
        print('{"trackIds":[{"id":1420663042,"v":5,"alg":null},{"id":1423985980,"v":6,"alg":null}]}')


while True:
    # in_str = '{"trackIds":[{"id":1420663042,"v":5,"alg":null},{"id":1423985980,"v":6,"alg":null}]}'
    # test string
    print('Paste the string')
    user_in = input()
    if user_in.casefold() == 'bye':
        break
    get_id_json(user_in)
    # break
