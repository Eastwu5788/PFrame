# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 13:13'
# sys
import math

# project
from pframe.util.exception import PFExtractionError
from .pobject import p_get


def p_chunks(array, size):
    """ 将数组按切分成固定大小的快

    :param array: 原始数组
    :param size: 每块大小
    """
    if not isinstance(array, list):
        raise TypeError("input params `array` must be type of list")

    return [array[idx:idx + size] for idx in range(0, len(array), size)]


def p_divide(array, size):
    """ 将数组等分成N个小数组

    TODO: 待完善

    :param array: 原始数组
    :param size: 子数组大小
    """
    if not isinstance(array, list):
        raise TypeError("input params `array` must be type of list")

    if len(array) < size:
        raise IndexError("invalid divide size")

    # 按照指固定大小切割前N个数组
    fmt_rst, step = list(), math.floor(len(array) / size)
    for idx in range(0, (size - 1) * step, step):
        fmt_rst.append(array[idx: idx + step])

    fmt_rst.append(array[(size - 1) * step:])
    return fmt_rst


def p_index(array, index=None):
    """ 将字典数组或者多维数组中的数据按index进行提取

    Usage:
        >>> p_index([[0, 1], [2, 3], [4, 5]], index=0)
        [0, 2, 4]
        >>> p_index([{"key1": "value1"}, {"key1": "value2"}], index="key1")
        ["value1", "value2"]

    :param array: 原始数组
    :param index: 提取的索引
    :rtype: list
    """
    if not isinstance(array, (list, tuple)):
        raise TypeError("input params `array` must be type of list or tuple")

    fmt_rst = list()
    for idx, item in enumerate(array):
        # try to extract data from the array or tuple
        if isinstance(item, (list, tuple)) and isinstance(index, int):
            if len(item) <= index:
                raise IndexError("item index out of index at `%d`" % idx)
            fmt_rst.append(item[index])

        # try to extract data from the dictionary
        elif isinstance(item, dict):
            if index not in item:
                raise KeyError("`%s` not in item at index `%d`" % (index, idx))
            fmt_rst.append(item[index])

        # try to extract data from the object
        elif hasattr(item, index):
            fmt_rst.append(getattr(item, index))

        else:
            raise PFExtractionError("can't extract from array at index `%d`" % idx)

    return fmt_rst


def p_index_column(array, index=None, append=False):
    """ 将数组中的数据提取成以value值作为key的字典

    Usage:
        >>> p_index_column([{"id": "5"}, {"id": "6"}], index="id", append=False)
        {"5": {"id": "5"}, "6": {"id": "6"}}
        >>> p_index_column([{"id": "5"}, {"id": "6"}], index="id", append=False)
        {"5": [{"id": "5"}], "6": [{"id": "6"}]}

    :param array: 原始数据
    :param index: 提取的key值
    :param append: 如果遇到key重复，是否将数据进行追加
    :rtype: dict
    """
    if not isinstance(array, (list, tuple)):
        raise TypeError("input params `array` must be type of list or tuple")

    fmt_rst = dict()
    for _, item in enumerate(array):
        value = p_get(item, key=index, default=None)

        # None value can not be key as dict
        if value is None:
            continue

        # append result
        if append:
            exit_value = fmt_rst.get(value, list())
            exit_value.append(item)
            fmt_rst[value] = exit_value

        # return simple dict
        else:
            fmt_rst[value] = item

    return fmt_rst


def is_immutable(obj):
    raise TypeError("%r objects are immutable" % obj.__class__.__name__)


class ImmutableListMixin:
    """ This class if from werkzeug.datastructures.py
    """
    _hash_cache = None

    def __hash__(self):
        if self._hash_cache is not None:
            return self._hash_cache
        rst = self._hash_cache = hash(tuple(self))
        return rst

    def __reduce_ex__(self, protocol):
        return type(self), (list(self),)

    def __delitem__(self, key):
        is_immutable(self)

    def __iadd__(self, other):
        is_immutable(self)

    def __setitem__(self, key, value):
        is_immutable(self)

    def append(self, item):  # pylint: disable=unused-argument
        is_immutable(self)

    remove = append

    def extend(self, iterable):  # pylint: disable=unused-argument
        is_immutable(self)

    def insert(self, pos, value):  # pylint: disable=unused-argument
        is_immutable(self)

    def pop(self, index=-1):  # pylint: disable=unused-argument
        is_immutable(self)

    def reverse(self):
        is_immutable(self)

    def sort(self, cmp=None, key=None, reverse=None):  # pylint: disable=unused-argument
        is_immutable(self)


class ImmutableList(ImmutableListMixin, list):
    """ This class if from werkzeug.datastructures.py
    """

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, list.__repr__(self))
