# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-11 10:15'
# project
from pframe.container import p_chunks, p_divide


def example_p_chunks():
    """ 演示 `p_chunks` 函数
    """
    example_data = [1, 2, 3, 4, 5]

    print(p_chunks(example_data, 2))
    print(p_chunks(example_data, 3))


def example_p_divide():
    """ 演示 `p_divide` 函数
    """
    example_data = [1, 2, 3, 4, 5, 6, 7, 8]

    print(p_divide(example_data, 3))
    print(p_divide(example_data, 2))

    example_data = [1, 2, 3, 4]
    print(p_divide(example_data, 3))


if __name__ == "__main__":
    example_p_divide()
