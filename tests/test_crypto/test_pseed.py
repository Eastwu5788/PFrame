# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 17:42'
# project
from pframe.crypto import seed


class TestSeed:

    def test_seed(self):
        """ 测试 `seed` 函数
        """
        assert len(seed(10)) == 10
