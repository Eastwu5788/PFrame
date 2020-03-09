# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 17:36'
from pframe.crypto import md5


class TestMd5:

    def test_md5(self):
        """ 测试 `md5` 加密函数
        :return:
        """
        assert md5("123").upper() == "202CB962AC59075B964B07152D234B70"
