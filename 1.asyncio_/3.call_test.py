# 可以直接给asyncio传递一些参数去执行

# call_soon  # 表示即刻执行，等到队列的下一循环的时刻 比call_later快
# call_later #
# call_cat  #指定时间运行
# call_soon_threadsafe  线程安全
import asyncio


# def callback(sleep_times):
#     print(f"sleep {sleep_times} success")
def callback(sleep_times, loop):
    print(f"sleep {sleep_times} success  {loop.time()}")


def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()
    # print(now)

    # loop.call_later(2, callback, 2)
    # loop.call_later(1, callback, 1)
    # loop.call_later(3, callback, 3)
    # loop.call_soon(callback, 4, loop)  # 表示即刻执行，等到队列的下一循环的时刻

    # loop.call_at(now + 2, callback, 2)
    # loop.call_at(now + 1, callback, 1)
    # loop.call_at(now + 3, callback, 3)
    # loop.call_soon(callback, 4, loop)  # 表示即刻执行，等到队列的下一循环的时刻

    # loop.call_at(now + 2, callback, 2, loop)
    # loop.call_at(now + 1, callback, 1, loop)
    # loop.call_at(now + 3, callback, 3, loop)
    # loop.call_soon(callback, 4, loop)  # 表示即刻执行，等到队列的下一循环的时刻

    loop.call_soon_threadsafe(callback, 2, loop)
    loop.call_soon_threadsafe(callback, 1, loop)
    loop.call_soon_threadsafe(callback, 3, loop)
    loop.call_soon(callback, 4, loop)  # 表示即刻执行，等到队列的下一循环的时刻

    # loop.call_soon(stoploop, loop)  # 停止方式:再写一个回调函数
    loop.stop()  #
    loop.run_forever()  # 启动      不能用loop.run_until_complete()，因为这个不是协程
