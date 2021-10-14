# 在协程序中使用多线程
# 在协成中集成阻塞io

import asyncio
import socket
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import time

# def get_url(url):
# 通过socket请求html
# url = urlparse(url)
# host = url.netloc
# path = url.path
# if path == "":
#     path = "/"
#
# # 建立socket连接
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # client.setblocking(False)
# client.connect((host, 80))  # 阻塞不会消耗cpu
# # 不停的询问连接是不是建立好，需要while循环不停地检查状态
# # 做计算任务或者再次发起其他的连接请求
# client.send(f"Get {url} HTTP:/1/1\r\nHost:{host}\r\nConnetcion:close\r\n\r")
#
# data = b""
# while True:
#     d = client.recv(1024)
#     if d:
#         data += d
#     else:
#         break
# data = data.decode("utf8")
# html_data = data.split("\r\n\r\n")[1]
# print(html_data)
# client.close()

import random


def get_url(url):
    url = url-1
    x = random.random()
    print(f"start url {x}")
    print(f"{x} {url}")



if __name__ == '__main__':
    s = time.time()
    loop = asyncio.get_event_loop()
    excutor = ThreadPoolExecutor(3)  # 这表示一个线程池 如果调用阻塞方式，那就放到线程池里运行
    tasks = []
    for i in range(20):
        url = 100
        task = loop.run_in_executor(excutor, get_url, url)  # 将某个阻塞io的函数放到这里面执行
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - s)
