"""
Telegram API Wrapper
~~~~~~~~~~~~~~~~~~~~
A basic wrapper for the Telegram bot API.

:copyright: (c) 2024 NekoMimiOffical
:license: Apache2, see LICENSE for more details
"""

##[Bob args]######################
__title__ = 'NekoTPy'
__author__ = "NekoMimiOffical"
__author_email__ = "nekomimi@tilde.team"
__description__ = "User-friendly and async ready Telegram bot wrapper inspired by discord.py"
__repository__ = "https://github.com/NekoMimiOffical/NekoTPy"
__bug_tracker__ = "https://github.com/NekoMimiOffical/NekoTPy/issues"
__license__ = "Apache2"
__pyver__ = ">=3.11"
__target__ = "OS Independent"
__requirements__ = ['aiohttp']
##################################

__version__ = '1.1.0'
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
