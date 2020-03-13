# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 15:15'
import datetime


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
