# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 14:33'
# sys
import datetime
import re

# 3p
import pytest

# project
from pframe.container import current_datetime, current_time
from pframe.container import datetime_2_str, str_2_datetime


class TestDatetime:

    # 日期 + 时间正则 2019-09-01 12:00:00
    reg_datetime = r"^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$"
    # 日期正则
    reg_date = r"^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"
    # 时间正则
    reg_time = r"^(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$"

    def test_current_datetime(self):
        """ 测试函数 `current_datetime`
        """
        assert isinstance(current_datetime(), datetime.datetime)

    def test_current_time(self):
        """ 测试函数 `current_time`
        """
        datetime_str = current_time("%Y-%m-%d %H:%M:%S")
        assert re.match(self.reg_datetime, datetime_str)

        date_str = current_time("%Y-%m-%d")
        assert re.match(self.reg_date, date_str)

        time_str = current_time("%H:%M:%S")
        assert re.match(self.reg_time, time_str)

    def test_str_2_datetime(self):
        """ 测试函数 `str_2_datetime`
        """
        result = str_2_datetime("2018-09-10", fmt="%Y-%m-%d")
        assert result == datetime.datetime(2018, 9, 10)

        result = str_2_datetime("2018-09-11 12:00:00", fmt="%Y-%m-%d %H:%M:%S")
        assert result == datetime.datetime(2018, 9, 11, 12)

        assert str_2_datetime(datetime.datetime(2019, 1, 20)) == datetime.datetime(2019, 1, 20)

        with pytest.raises(TypeError):
            str_2_datetime(123)

    def test_datetime_2_str(self):
        """ 测试函数 `datetime_2_str`
        """
        result = datetime_2_str(datetime.datetime(2019, 1, 20), fmt="%Y-%m-%d")
        assert result == "2019-01-20"

        result = datetime_2_str(datetime.datetime(2019, 1, 20), fmt="%Y-%m-%d %H:%M:%S")
        assert result == "2019-01-20 00:00:00"

        with pytest.raises(TypeError):
            datetime_2_str("2019-01-20")
