# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 17:23'
# sys
import os
import socket

# project
from pframe.util import PY2


def is_ip(value):
    """ Determine if the given string is an IP address.

    :param value: value to check
    :rtype: bool
    """
    if PY2 and os.name == "nt":
        try:
            socket.inet_aton(value)
            return True
        except socket.error:
            return False

    for family in (socket.AF_INET, socket.AF_INET6):
        try:
            socket.inet_pton(family, value)
        except socket.error:
            pass
        else:
            return True

    return False
