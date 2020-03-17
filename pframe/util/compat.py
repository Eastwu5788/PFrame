# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 17:25'
import sys

PY2 = sys.version_info[0] == 2


if PY2:
    iteritems = lambda d, *args, **kwargs: d.iteritems(*args, **kwargs)  # noqa: E731

else:
    iteritems = lambda d, *args, **kwargs: iter(d.items(*args, **kwargs))  # noqa: E731
