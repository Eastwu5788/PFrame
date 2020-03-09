# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 14:33'
# sys
import datetime
# project
from pframe.container import timestamp_2_datetime
from pframe.container import datetime_2_timestamp


class TestTime:

    def test_timestamp_2_datetime(self):
        """ 测试函数 `timestamp_2_datetime`
        """
        assert timestamp_2_datetime(1583739275, fmt="%Y-%m-%d") == "2020-03-09"

    def test_datetime_2_timestamp(self):
        assert datetime_2_timestamp(datetime.datetime(2020, 3, 9)) == 1583683200.0
