# 协程脱离不了 1.事件循环 2.回调（驱动生成器或或者驱动协程）3.epoll（io多路复用）

# asyncio是python用于解决异步id编程的一整套方案
# tornado、gevent、twisted(scrapy、django、channels)
# totando（实现web服务器），django+flask 传统阻塞io模型  web系统开发框架 本身不完成socket编码（uwsgi，gunicorn+nginx）
# totando 本身实现了web服务器（实现了socket编码）可以直接部署，但是功能不如nginx强大，没有实现ip限制 log服务 静态文件代理，但是不能使用简单的数据库驱动

# 使用asyncio
# 协程必须搭配事件循环
import asyncio
import time


# async def get_html(url):
#     print("start get url")
#     # 模拟耗时操作，但是不能用time.sleep(2)，因为这是一个同步阻塞的接口，同步阻塞的接口不能使用在协程序里面的
#     # asyncio.sleep(2)  # 但是可以使用这个 ，但是这样会直接报错
#     await asyncio.sleep(2)  # 但是可以使用这个，await加上的意思是等待这个操作完成  这样会返回一个future
#     # await time.sleep(2)  # await 后面必须接的是awaitable对象 所以这样会报错
#     # time.sleep(2)
#     print("end get url")


# 先运行这个main
# if __name__ == '__main__':
#     s = time.time()
#     loop = asyncio.get_event_loop()  # 完成select操作
#     loop.run_until_complete(get_html("http:imooc.com"))  # run_until_complete暂时可以理解为多线程中的join方法，在这种时候可以把asyncio理解为线程池
#     print(time.time() - s)


# 2. 运行10次 看看time.sleep 和 asyncio.sleep 的区别
# if __name__ == '__main__':
#     s = time.time()
#     loop = asyncio.get_event_loop()  # 完成select操作
#     tasks = [get_html("aaa.com") for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))  # asyncio.wait可以接受一个可迭代对象
#     print(time.time() - s)

# 3.获取返回值
from functools import partial


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return "bobby"


def callback(url, future):
    print(url)
    # 这里的默认传参为future
    print("send maill to bobby")


# 3.1使用ensure_future 获取单个返回值
# if __name__ == '__main__':
    # s = time.time()
    # loop = asyncio.get_event_loop()  # 完成select操作
    # get_future = asyncio.ensure_future(get_html("aaa.com"))
    # # tasks = [get_html("aaa.com") for i in range(10)]
    # loop.run_until_complete(get_future)  # run_until_complete 可以接受future类型 可以接受协成类型
    # print(get_future.result())
    # print(time.time() - s)


# 3.2 使用task 获取返回值
# if __name__ == '__main__':
#     s = time.time()
#     loop = asyncio.get_event_loop()  # 完成select操作
#     # tasks = [get_html("aaa.com") for i in range(10)]
#     task = loop.create_task(get_html("aa.com"))  # task是future的子类
#     # task.add_done_callback(callback)  # 这里只能接受函数名
#     task.add_done_callback(partial(callback, "sssss.com"))  # partial是一个偏函数partial可以把callback包装成一个不接收参数的函数
#     loop.run_until_complete(task)  # run_until_complete 可以接受future类型 可以接受协成类型
#     print(task.result())
#     print(time.time() - s)

# wait和gather
# gather 更加高层


# 4.获取多个任务返回值
if __name__ == '__main__':
    s = time.time()
    loop = asyncio.get_event_loop()  # 完成select操作
    tasks = [get_html("aaa.com") for i in range(10)]
    loop.run_until_complete(asyncio.gather(*tasks))  # gather添加*表示参数
    # print(time.time() - s)

    # tasks1 = [get_html("aaa.com") for i in range(2)]
    # tasks2 = [get_html("aaa.cn") for i in range(2)]
    # loop.run_until_complete(asyncio.gather(*tasks1, *tasks2))

    # tasks1_2 = asyncio.gather(*tasks1)
    # tasks2_2 = asyncio.gather(*tasks2)
    # tasks1_2.cancel()
    # loop.run_until_complete(asyncio.gather(tasks1_2, tasks2_2))
