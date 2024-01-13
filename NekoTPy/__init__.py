"""
Telegram API Wrapper
~~~~~~~~~~~~~~~~~~~~
A basic wrapper for the Telegram bot API.

:copyright: (c) 2024 NekoMimiOffical
:license: Apache2, see LICENSE for more details
"""

__title__ = 'telegram'
__version__ = "1.1.0"
__author__ = "NekoMimiOffical"
__repository__ = "https://github.com/NekoMimiOffical/NekoTPy"
__license__ = "Apache2"
__build__ = 0x04000A

"""
Build number policy:
~~~~~~~~~~~~~~~~~~~~

The build number is divided into 2 sections
-> the first 2 Hex digits representing a major code
-> the last 4 Hex digits representing a fix code
"""

from .bot import Bot
from .types.user import User
from .types.group import Group
from .types.channel import Channel
