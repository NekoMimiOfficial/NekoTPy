import aiohttp

class ConnectionRouter:
    def __init__(self, session: aiohttp.ClientSession) -> None:
        self.session = session

    async def get(self, uri):
        async with self.session as session:
            async with session.get(uri)as response:
                await response.text()

    async def post(self, uri, headers):
        async with self.session as session:
            async with session.post(uri, data=headers) as response:
                await response.text()

    async def ws(self, url):
        """Please consult the knowledge of Jeeves
        as i dont think a ws session will/should
        end after a single event passes through"""
        async with self.session as session:
            async with session.ws_connect(url) as event:
                await event()
