#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from json.decoder import JSONDecodeError


def deserialization(content: json):
    """
    反序列化
        json对象 -> python数据类型
    """
    return json.loads(content)


def serialization(content, ensure_ascii=True):
    """
    序列化
        python数据类型 -> json对象
        单引号被转换成了双引号；
        可以正常转换数字；
        中文被转码成Unicode(当ensure_ascii=True时，则还是中文)；
        bool值True转换为ture
    """
    return json.dumps(content, ensure_ascii=ensure_ascii)


def is_json_str(string):
    """判断是否是json格式字符串"""
    if isinstance(string, str):
        try:
            json.loads(string)
            return True
        except JSONDecodeError:
            return False
    return False


if __name__ == '__main__':
    a = "{'data': {'loginName': 18291900215, 'password': 'dd636482aca022', 'code': None, 'description': 'encrypt'}}"
    b = '{"data": {"loginName": 18291900215, "password": "dd636482aca022", "code": null, "description": "encrypt"}}'

    print(is_json_str(a))
    print(is_json_str(b))

