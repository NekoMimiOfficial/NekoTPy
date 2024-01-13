import asyncio

class Dispatcher:
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop = loop
    
    async def _run_task(self, job, *args, **kwargs):
        await getattr(self, job)(*args, **kwargs)

    async def screen(self, job, *args, **kwargs):
        event = "on_" + job
        handle = "handle_" + job

        if hasattr(self, handle):
            getattr(self, handle)(*args, **kwargs)

        if hasattr(self, event):
            try:
                asyncio.ensure_future(self._run_task(event, *args, **kwargs), loop=self.loop)
            except:
                self.loop.create_task(self._run_task(event, *args, **kwargs))
