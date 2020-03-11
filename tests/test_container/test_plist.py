# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 14:33'
# 3p
import pytest

# project
from pframe.container import p_chunks, p_divide
from pframe.container import p_index, p_index_column
from pframe.util import PFExtractionError


class User:

    def __init__(self, uid):
        """ 用户初始化函数
        """
        self.uid = uid


class TestList:

    def test_p_chunks(self):
        """ 测试函数 `p_chunks`
        """
        test_data = [1, 2, 3, 4, 5]
        assert p_chunks(test_data, 3) == [[1, 2, 3], [4, 5]]
        assert p_chunks(test_data, 2) == [[1, 2], [3, 4], [5]]

        test_data = [1, 2, 3, 4]
        assert p_chunks(test_data, 2) == [[1, 2], [3, 4]]
        assert p_chunks(test_data, 3) == [[1, 2, 3], [4]]

    def test_p_divide(self):
        """ 测试函数 `p_divide`
        """
        test_data = [1, 2, 3, 4, 5]
        assert p_divide(test_data, 3) == [[1], [2], [3, 4, 5]]
        assert p_divide(test_data, 2) == [[1, 2], [3, 4, 5]]

        test_data = [1, 2, 3, 4]
        assert p_divide(test_data, 3) == [[1], [2], [3, 4]]

    def test_p_index_smoke(self):
        """ 测试函数 `p_index` 冒烟
        """
        test_data = [[1, 2], [2, 4], [2]]
        assert p_index(test_data, index=0) == [1, 2, 2]

        test_data = [{"key": 2}, {"key": 4}]
        assert p_index(test_data, index="key") == [2, 4]

        test_data = [User(3), {"uid": 5}]
        assert p_index(test_data, index="uid") == [3, 5]

    def test_p_index_raise(self):
        """ 测试函数 `p_index` 异常
        """
        with pytest.raises(TypeError):
            p_index({"id": 1}, index="id")

        with pytest.raises(IndexError):
            p_index([[1, 2], [3]], index=1)

        with pytest.raises(KeyError):
            p_index([{"ud": "1"}], index="id")

        with pytest.raises(PFExtractionError):
            p_index([[1, 2]], index="1")

    def test_p_index_column_smoke(self):
        """ 测试函数 `p_index_column` 冒烟
        """
        test_data = [{"id": 5}, {"id": 6}, {"id": None}]
        assert p_index_column(test_data, index="id") == {5: {"id": 5}, 6: {"id": 6}}

        test_data = [[1, 2], [4, 5]]
        assert p_index_column(test_data, index=0) == {1: [1, 2], 4: [4, 5]}

        user_1, user_2 = User(uid=1), User(uid=2)
        test_data = [user_1, user_2]
        assert p_index_column(test_data, index="uid") == {1: user_1, 2: user_2}

        assert p_index_column(test_data, index="uid", append=True) == {1: [user_1], 2: [user_2]}

    def test_p_index_column_raise(self):
        """ 测试函数 `p_index_column` 异常
        """
        with pytest.raises(TypeError):
            p_index_column({"id": 1}, index="id")

        with pytest.raises(IndexError):
            p_index_column([[1, 2], [3]], index=1)
