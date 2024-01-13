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
