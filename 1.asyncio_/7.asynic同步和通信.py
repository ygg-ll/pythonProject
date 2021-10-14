# asynic基于单线程 不用GIL
import asyncio

import aiohttp

total = 0

# async def add():
#     # 1.doingsomething
#     # 2.io 操作
#     global total
#     for i in range(1000000):
#         total += 1
#
#
# async def desc():
#     global total
#     for i in range(1000000):
#         total -= 1
#
#
# if __name__ == '__main__':
#     import asyncio
#
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)

#

# 什么时候同步？？？？？？？？？？？？？？？？？？？？？？？？？

from asyncio import Lock, Queue

queue = Queue
# await queue.get()  # 使用方式 queue一般用于限流，如果通信的话定义一个全局变量就好

# queue = []

cache = {}
lock = Lock


# async def get_stuff(url):
#     # 将下面代码保护起来
#     await lock.acquire()  # 因为需要等待这把锁，所以要加await
#     if url in cache:
#         return cache[url]
#     stuff = await aiohttp.request('GET', url)
#     cache[url] = stuff
#     return stuff

async def get_stuff(url):
    # 将下面代码保护起来
    # with await lock: # 或者下面写法
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request('GET', url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff()


async def use_stuff():
    stuff = await get_stuff()
    # use stuff to do something interesting
