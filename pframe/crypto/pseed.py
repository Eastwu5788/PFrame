# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 17:38'
import random
import string


def seed(length=32):
    """ 生成指定长度的随机字符串

    :param length: 期望生成的字符串长度
    """
    base_str = string.digits + string.ascii_letters
    return ''.join([random.choice(base_str) for _ in range(length)])
