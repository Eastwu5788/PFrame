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
from pframe.container import near_weeks, near_months, near_years
from pframe.container import year_begin
from pframe.container import near_days


class TestPDate:

    def test_year_begin(self):
        """ 测试函数 `year_begin`
        """
        assert year_begin() == datetime.datetime(2020, 1, 1, 0, 0, 0, 0)

    def test_month_begin(self):
        """ 测试函数 `month_begin`
        """
        assert month_begin(datetime.datetime(2020, 3, 15)) == datetime.datetime(2020, 3, 1, 0, 0, 0, 0)

    def test_month_end(self):
        """ 测试函数 `month_end`
        """
        assert month_end(datetime.datetime(2020, 3, 15)) == datetime.datetime(2020, 3, 31, 23, 59, 59, 999)
        assert month_end(datetime.datetime(2019, 12, 15)) == datetime.datetime(2019, 12, 31, 23, 59, 59, 999)

    def test_near_days(self):
        """ 测试函数 `near_days`
        """
        assert near_days(datetime.datetime(2020, 9, 17), period=2) == datetime.datetime(2020, 9, 15)

    def test_near_weeks(self):
        """ 测试函数 `near_weeks`
        """
        assert near_weeks(datetime.datetime(2020, 9, 17), period=2) == datetime.datetime(2020, 9, 3)

    def test_near_months(self):
        """ 测试函数 `near_months`
        """
        assert near_months(datetime.datetime(2020, 9, 7), period=2) == datetime.datetime(2020, 7, 7)

    def test_near_years(self):
        """ 测试函数 `near_years`
        """
        assert near_years(datetime.datetime(2020, 9, 7), period=2) == datetime.datetime(2018, 9, 7)

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

    def test_year_begin_raise(self):
        """ 测试函数 `year_begin` 异常
        """
        with pytest.raises(TypeError):
            year_begin("2020-09-1")

    def test_near_weeks_raise(self):
        """ 测试函数 `near_weeks` 异常
        """
        with pytest.raises(TypeError):
            near_weeks("2020-09-1")

    def test_near_months_raise(self):
        """ 测试函数 `near_months` 异常
        """
        with pytest.raises(TypeError):
            near_months("2020-09-1")

    def test_near_years_raise(self):
        """ 测试函数 `near_years` 异常
        """
        with pytest.raises(TypeError):
            near_years("2020-09-1")

    def test_near_days_raise(self):
        """ 测试函数 `near_days` 异常
        """
        with pytest.raises(TypeError):
            near_days("2020-09-1")
