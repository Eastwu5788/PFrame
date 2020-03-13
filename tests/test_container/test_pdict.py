# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 15:10'
from pframe.container import p_merge


class TestDict:

    def test_deep_merge(self):
        """ 测试深度合并函数 `p_merge`
        :return:
        """
        assert p_merge({"1": "2", "3": "4"}, {"3": "5"}) == {"1": "2", "3": "4"}
        assert p_merge({"1": {"2": 3, "4": 5}}, {"1": {"5": 5}}) == {"1": {"2": 3, "4": 5, "5": 5}}
