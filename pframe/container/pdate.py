# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 15:15'
import datetime
# 3p
from dateutil.relativedelta import relativedelta


def year_begin(time=None):
    """ 指定某个时间的年度开始日期

    :param time: 指定时间
    """
    # 检查入参
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'time' must be type of datetime.datetime")

    return time.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)


def month_begin(time=None):
    """ 获取指定时间的当月开始日期

    Usage:
        >>> month_begin(datetime.datetime(2020, 3, 15))
        datetime.datetime(2020, 3, 1, 0, 0, 0, 0)

    :param time: 指定的时间
    """
    # 检查入参
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'time' must be type of datetime.datetime")

    # Replace
    return time.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


def month_end(time=None):
    """ 获取指定时间的当月最后一天

    Usage:
        >>> month_end(datetime.datetime(2020, 3, 15))
        datetime.datetime(2020, 3, 30, 23, 59, 59, 999)

        >>> month_end(datetime.datetime(2019, 12, 15))
        datetime.datetime(2019, 12, 31, 23, 59, 59, 999)

    :param time: 指定的时间
    """
    # 检查入参
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'time' must be type of datetime.datetime")

    try:
        next_month = time.replace(month=time.month + 1, day=1, hour=23, minute=59, second=59, microsecond=999)
    except ValueError:
        next_month = time.replace(year=time.year + 1, month=1, day=1, hour=23, minute=59, second=59, microsecond=999)

    return next_month - datetime.timedelta(days=1)


def day_begin(time=None):
    """ 获取指定日期的开始

    Usage:
        >>> day_begin(datetime.datetime(2020, 11, 9, 11, 0, 0))
        datetime.datetime(2020, 11, 9, 0, 0, 0)

    :param time: 指定日期
    """
    # 检查入参
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'time' must be type of datetime.datetime")

    return datetime.datetime(time.year, time.month, time.day, hour=0, minute=0, second=0, microsecond=0)


def day_end(time=None):
    """ 获取指定日期的结束

    Usage:
        >>> day_end(datetime.datetime(2020, 11, 9, 11, 0, 0))
        datetime.datetime(2020, 11, 9, 23, 59, 59)

    :param time: 指定日期
    """
    # 检查入参
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'time' must be type of datetime.datetime")

    return datetime.datetime(time.year, time.month, time.day, hour=23, minute=59, second=59, microsecond=999)


def near_days(time=None, period=1):
    """ 获取某个时刻开始的N天之前的日期

     Usage:
        >>> near_days(end=datetime.datetime(2020, 9, 29), period=1)
        datetime.datetime(2020, 9, 28)

    :param time: 截止日期，不填默认为当前时间
    :param period: 日度周期
    :rtype: datetime.datetime
    """
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'end' must be type of datetime.datetime")

    return time - relativedelta(days=period)


def near_months(time=None, period=1):
    """ 获取某个时刻开始的近N个月日期

    Usage:
        >>> near_week(end=datetime.datetime(2020, 9, 29), period=1)
        datetime.datetime(2020, 8, 29)

    :param time: 截止日期，不填默认为当前时间
    :param period: 月度周期
    :rtype: datetime.datetime
    """
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'end' must be type of datetime.datetime")

    return time - relativedelta(months=period)


def near_weeks(time=None, period=1):
    """ 获取从某个时刻开始的近N周日期

    Usage:
        >>> near_week(end=datetime.datetime(2020, 9, 29), period=1)
        datetime.datetime(2020, 9, 22)

    :param time: 截止日期，不填默认为当前日期
    :param period: 周度周期
    :rtype: datetime.datetime
    """
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'end' must be type of datetime.datetime")

    return time - relativedelta(weeks=period)


def near_years(time=None, period=1):
    """ 获取某个时间开始的近N年的日期

    Usage:
        >>> near_year(end=datetime.datetime(2020, 9, 29), period=1)
        datetime.datetime(2019, 9, 29)

    :param time: 截止日期
    :param period: 年度周期
    :rtype: datetime.datetime
    """
    time = time or datetime.datetime.now()
    if not isinstance(time, datetime.datetime):
        raise TypeError("'end' must be type of datetime.datetime")

    return time - relativedelta(years=period)
