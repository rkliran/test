#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Variable(object):
    """全局变量池"""

    def __init__(self):
        super().__init__()

    def set(self, key, value):
        setattr(self, key, value)

    def get(self, key):
        return getattr(self, key)

    def has(self, key):
        return hasattr(self, key)


is_vars = Variable()

if __name__ == '__main__':
    is_vars.set('name', 'hoou')
    print(is_vars.get('name'))
    import re
    inputstr = 'hello 111 world 111'
    #replacestr = inputstr.replace('111','222')
    #print(replacestr)
    replacestr = re.sub('\d+', '222', inputstr)
    print(replacestr)
    print(id(is_vars))
    print(hasattr(is_vars, 'name'))
    print(getattr(is_vars, 'name'))

