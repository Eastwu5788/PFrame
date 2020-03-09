# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 13:21'


class PFBaseException(Exception):
    """ PFrame基础异常
    """


class PFExtractionError(PFBaseException):
    """ PFrame提取数据异常
    """
