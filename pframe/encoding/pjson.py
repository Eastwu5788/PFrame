# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 17:40'
import datetime
import decimal
import json
try:
    from bson import ObjectId
except ImportError:
    ObjectId = None


class JSONEncoder(json.JSONEncoder):

    def default(self, o):  # pylint: disable=method-hidden

        # 处理datetime
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")

        # 处理日期
        if isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")

        # 处理decimal
        if isinstance(o, decimal.Decimal):
            return float(o)

        if ObjectId and isinstance(o, ObjectId):
            return str(o)

        # 其它默认处理
        return json.JSONEncoder.default(self, o)
