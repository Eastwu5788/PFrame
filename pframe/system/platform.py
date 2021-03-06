# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 17:30'
# sys
import sys


def get_os():
    """
    判断当前操作系统类型
    """
    if sys.platform == 'darwin':
        return 'mac'

    if sys.platform.find('freebsd') != -1:
        return 'freebsd'

    if sys.platform.find('linux') != -1:
        return 'linux'

    if sys.platform.find('win32') != -1:
        return 'windows'

    if sys.platform.find('sunos') != -1:
        return 'solaris'

    return sys.platform


class Platform:
    """
    Return information about the given platform.
    """

    @staticmethod
    def is_darwin(name=None):
        name = name or sys.platform
        return 'darwin' in name

    @staticmethod
    def is_mac(name=None):
        return Platform.is_darwin(name)

    @staticmethod
    def is_freebsd(name=None):
        name = name or sys.platform
        return name.startswith("freebsd")

    @staticmethod
    def is_linux(name=None):
        name = name or sys.platform
        return 'linux' in name

    @staticmethod
    def is_bsd(name=None):
        """ Return true if this is a BSD like operating system. """
        name = name or sys.platform
        return Platform.is_darwin(name) or Platform.is_freebsd(name)

    @staticmethod
    def is_solaris(name=None):
        name = name or sys.platform
        return name == "sunos5"

    @staticmethod
    def is_unix(name=None):  # pylint: disable=unused-argument
        """ Return true if the platform is a unix, False otherwise. """
        return (
                Platform.is_darwin()
                or Platform.is_linux()
                or Platform.is_freebsd()
        )

    @staticmethod
    def is_win32(name=None):
        name = name or sys.platform
        return name == "win32"

    @staticmethod
    def is_windows(name=None):
        return Platform.is_win32(name)

    @staticmethod
    def python_architecture():
        if sys.maxsize > 2 ** 32:
            return "64bit"
        return "32bit"
