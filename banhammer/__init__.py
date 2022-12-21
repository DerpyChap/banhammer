# -*- coding: utf-8 -*-
"""
Tom Scott Banhammer Generator
~~~~~~~~~~~~~~~~~~~
Generates GIFs based on Tom Scott's Banhammer.
:copyright: (c) 2019-2022 DerpyChap
:license: ISC, see LICENSE for more details.
"""

__title__ = 'banhammer'
__author__ = 'DerpyChap'
__license__ = 'ISC'
__copyright__ = 'Copyright 2019-2022 DerpyChap'
__version__ = '0.1.3'

from collections import namedtuple
from .generator import Generator

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(
major=0, minor=1, micro=2, releaselevel='final', serial=0)