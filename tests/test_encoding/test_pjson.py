# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 17:43'
# sys
import datetime
import decimal
import json

# project
from pframe.encoding import JSONEncoder


class TestJSONEncoder:

    def test_json_encoder(self):
        """ 测试 JSONEncoder 的功能
        """
        test_data = datetime.datetime(2019, 1, 1)
        assert json.dumps(test_data, cls=JSONEncoder) == test_data.strftime('"%Y-%m-%d %H:%M:%S"')

        test_data = datetime.date(2019, 1, 1)
        assert json.dumps(test_data, cls=JSONEncoder) == test_data.strftime('"%Y-%m-%d"')

        assert json.dumps(decimal.Decimal(1.1), cls=JSONEncoder) == "1.1"
