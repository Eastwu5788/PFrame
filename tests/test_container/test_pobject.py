# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 14:33'
# 3p
import pytest
# project
from pframe.container import p_get


class User:

    def __init__(self, uid, age):
        self.uid = uid
        self.age = age


class TestObject:

    def test_p_get_smoke(self):
        """ 函数 `p_get` 冒烟测试
        """
        test_data = {"uid": 13, "age": 1}
        assert p_get(test_data, key="uid") == 13
        assert p_get(test_data, key="sex") is None

        test_data = [1, 2, 3, 5]
        assert p_get(test_data, key=2) == 3

        test_data = User(13, 2)
        assert p_get(test_data, key="uid") == 13
        assert p_get(test_data, key="sex") is None

    def test_p_get_raise(self):
        """ 函数 `p_get` 异常测试
        """
        with pytest.raises(IndexError):
            p_get([1, 2, 3], key=3)
