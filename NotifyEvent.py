import asyncio
import sys


class NotifyEvent(asyncio.Event):
    def __init__(self):
        super().__init__()
        # self.notify = asyncio.Event()
        # self.notify.set()

    def set(self, name=None):
        # self.notify.set()
        self.name = name
        super().set()

    async def wait(self):
        # await self.notify.wait()
        await super().wait()
        # self.notify.clear()
        super().clear()
        return self.name


async def task(name, event, d={}):
    while True:
        name1 = await event.wait()
        if name1:
            if name1 == name:
                d[name] = d.get(name, 0) +  1
                kol = sum(d.values())
                print(f'{name}: {d[name]} / {kol - d[name]}')
        else:
            break


exec(sys.stdin.read())



