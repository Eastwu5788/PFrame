# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 15:00'
import collections

from pframe.util.compat import iteritems


def p_merge(from_dict, to_dict):
    """ 合并两个字典，支持深度合并

    Usage:
        >>> p_merge({"1": "2", "3": "4"}, {"3": "5"})
        {"1": "2", "3": "4"}

        >>> p_merge({"1": {"2": 3, "4": 5}}, {"1": {"5": 5}})
        {"1": {"2": 3, "4": 5, "5": 5}}

    :param from_dict: 原始字典
    :param to_dict: 目标字典
    """
    for key, value in from_dict.items():
        # 如果value和目标dict中的值都为dict时，进行深度合并
        if key in to_dict.keys()\
                and isinstance(to_dict[key], collections.Mapping) \
                and isinstance(value, collections.Mapping):
            p_merge(value, to_dict[key])
        else:
            to_dict[key] = value

    return to_dict


def is_immutable(obj):
    raise TypeError("%r objects are immutable" % obj.__class__.__name__)


class ImmutableDictMixin:
    """ This class if from werkzeug.datastructures.py
    """

    _hash_cache = None

    def _iter_hashitems(self):
        return iteritems(self)

    def __hash__(self):
        if self._hash_cache is not None:
            return self._hash_cache
        rst = self._hash_cache = hash(frozenset(self._iter_hashitems()))
        return rst

    def setdefault(self, key, default=None):  # pylint: disable=unused-argument
        is_immutable(self)

    def update(self, *args, **kwargs):  # pylint: disable=unused-argument
        is_immutable(self)

    def pop(self, key, default=None):  # pylint: disable=unused-argument
        is_immutable(self)

    def popitem(self):
        is_immutable(self)

    def __setitem__(self, key, value):
        is_immutable(self)

    def __delitem__(self, key):
        is_immutable(self)

    def clear(self):
        is_immutable(self)


class ImmutableDict(ImmutableDictMixin, dict):
    """ This class if from werkzeug.datastructures.py
    """

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, dict.__repr__(self))

    def copy(self):
        return dict(self)

    def __copy__(self):
        return self
