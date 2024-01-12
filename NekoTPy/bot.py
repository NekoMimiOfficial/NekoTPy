"""
Bot wrapper
~~~~~~~~~~~

:license: (c) 2024 NekoMimiOfficial Apache2
"""

import asyncio
import aiohttp

class Bot:
    def __init__(self, *, loop=None, **kwargs) -> None:
        self.token = None
        self.ws = None
        self.loop = asyncio.get_event_loop() if loop is None else loop

        self.session = aiohttp.ClientSession(loop=self.loop)
        self.headers = { 'content-type' : 'application/json', }
        self._closed = False
        self._is_logged_in = False


        @property
        def is_logged_in(self):
            return self._is_logged_in
