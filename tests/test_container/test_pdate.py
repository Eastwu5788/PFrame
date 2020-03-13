# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 15:26'
# sys
import datetime
import pytest

# project
from pframe.container import month_end, month_begin


class TestPDate:

    def test_month_begin(self):
        """ 测试函数 `month_begin`
        """
        assert month_begin(datetime.datetime(2020, 3, 15)) == datetime.datetime(2020, 3, 1, 0, 0, 0, 0)

    def test_month_end(self):
        """ 测试函数 `month_end`
        """
        assert month_end(datetime.datetime(2020, 3, 15)) == datetime.datetime(2020, 3, 31, 23, 59, 59, 999)
        assert month_end(datetime.datetime(2019, 12, 15)) == datetime.datetime(2019, 12, 31, 23, 59, 59, 999)

    def test_month_begin_raise(self):
        """ 测试函数 `month_begin` 异常
        """
        with pytest.raises(TypeError):
            month_begin("2010-10-11")

    def test_month_end_raise(self):
        """ 测试函数 `month_end` 异常
        """
        with pytest.raises(TypeError):
            month_end("2010-10-11")
