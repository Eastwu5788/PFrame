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
        rst = datetime_2_timestamp(datetime.datetime(2020, 3, 9))
        # CI运行于travis-ci.com会有时区问题
        assert rst == 1583683200.0 or rst == 1583712000.0
