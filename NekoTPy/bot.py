"""
Bot wrapper
~~~~~~~~~~~

:license: (c) 2024 NekoMimiOfficial Apache2
"""

from .cables import ConnectionRouter
from .dispatcher import Dispatcher

import asyncio
import aiohttp

class Bot:
    def __init__(self, *, loop=None, **kwargs) -> None:
        self.API = 'https://api.telegram.org/'
        self.FILE_API = 'https://api.telegram.org/file/'

        self.token = None
        self.ws = None
        self.loop = asyncio.get_event_loop() if loop is None else loop

        self.session = aiohttp.ClientSession(loop=self.loop)
        self.router = ConnectionRouter(self.session)
        self.dispatcher = Dispatcher(self.loop)
        self.headers = { 'content-type' : 'application/json', }
        self.max_polls = kwargs.get('max-msgs', 100)
        self.update_id = kwargs.get('uid', 0)

