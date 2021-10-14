# python为了将语义更加明确在3.5后引用了async和await
import types


@types.coroutine
def downloader(url):
    yield url


# async def downloader(url):
#     return "bobby"


async def download_url(url):
    """doingsomething"""
    html = await downloader(url)  # awit 后面只能接Awaitable对象 from collections import Awaitable
    return html


if __name__ == '__main__':
    coro = download_url("sss.mopcc.com")
    # next(None)  # 使用关键词后不能这样用
    coro.send(None)
