import asyncio, sys


class FilterQueue(asyncio.Queue):
    def __init__(self, *args):
        super().__init__(*args)
        self.window = None

    async def put(self, val):
        if self.empty():
            self.window = val
        await super().put(val)

    def __contains__(self, filt):
        for i in self._queue:
            if filt(i):
                return True
        return False

    async def get(self, filt=lambda x: True):
        if filt in self:
            for i in range(self.qsize()):
                el = await super().get()
                if filt(el):
                    # print(i)
                    self.window = self._queue[0] if not self.empty() else None
                    return el
                await super().put(el)
        else:
            self.window = self._queue[0] if not self.empty() else None
            return await super().get()

    def later(self):
        if self.empty():
            raise asyncio.QueueEmpty
        else:
            self.put_nowait(self.get_nowait())
            self.window = self._queue[0] if not self.empty() else None


exec(sys.stdin.read())
# async def putter(n, queue):
#     for i in range(n):
#         await queue.put(i)
#
# async def getter(n, queue, filter):
#     res = 0
#     for i in range(n):
#         await asyncio.sleep(0)
#         res += (i % 7) * await queue.get(filter)
#     return res
#
# async def main():
#     queue = FilterQueue(200)
#     res = await asyncio.gather(putter(4000, queue), getter(4000, queue, lambda n: n % 2))
#     print(res[1])
#
# asyncio.run(main())