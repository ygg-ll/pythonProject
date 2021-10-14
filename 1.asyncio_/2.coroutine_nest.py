# 协程取消原理
# run_until_complete
import asyncio

# loop = asyncio.get_event_loop()
# loop.run_until_complete()  # 运行到某个条件会停止
# loop.run_forever()  # 一直运行
# 1.loop会被放到future中
# 2.取消future(task)
import asyncio
import time


async def get_html(sleep_times):
    print("waitiuing")
    await asyncio.sleep(sleep_times)
    print(f"sleep {sleep_times}")


# 下面要在命令行中运行，按住啊crtl+c 取消线程查看效果
# if __name__ == '__main__':
#     task1 = get_html(1)
#     task2 = get_html(2)
#     task3 = get_html(3)
#     # tasks = [task1, task2, task3]
#     tasks = [task3, task2, task1]
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e:
#         all_tasks = asyncio.Task.all_tasks()  # 获取所有tasks
#         for tasks in all_tasks:
#             print("canacle task")
#             print(tasks.cancel())  # 成功打印True
#             loop.stop()  # 调用完成stop后必须调用forever
#             loop.run_forever()
#     finally:
#         loop.close()  # close 和stop是有区别的

## 协程中嵌套协程


async def compute(x, y):
    print(f"compute {x} {y}")
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    reslt = await compute(x, y)
    print(f"{x} + {y} = {reslt}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
