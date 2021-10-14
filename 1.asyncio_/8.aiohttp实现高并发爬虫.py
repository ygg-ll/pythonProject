# asyncio爬虫、去重（去除重复的url）、入库（因为是并发，所以pymysql不可用了）

import re
import aiohttp  # https://docs.aiohttp.org/en/stable/
import aiomysql  # https://aiomysql.readthedocs.io/en/latest/
from pyquery import PyQuery
import asyncio

start_url = "http://blog.jobbole.com/keji/qkl/170998.html"
waitting_urls = []  # 协成是单线程模式，使用list做通信就可以
seen_urls = set()  # 已经爬取的url去重 用set；上亿条用布隆过滤器
stopping = False

sem = asyncio.Semaphore(3)  # 设置并发，在fetch中设置就好


async def fetch(url, session):
    async with sem:
        try:
            async with session.get(url) as resp:
                # print(resp.status)
                # print(await resp.text())
                data = await resp.text()
                # print("Body:", data[:15], "...")
                return data
        except Exception as e:
            print(e)


def extract_urls(html):
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            waitting_urls.append(url)


async def init_urls(url, session):
    """解析等待爬取的下一个url"""
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def article_handler(url, session, pool):
    """获取文章详情，并且解析入库"""
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    print(title)

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            insert_sql = f"insert into artitle_test(title) values ('{title}')"
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waitting_urls.pop()
            print(f"start get url {url}")
            x = "http://.*?jobbole.com/.*/.*/\d+.html"
            rex = re.compile(x)
            if rex.match(url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session, pool))
                    # await asyncio.sleep(3)
                # else:
                #     if url not in seen_urls:
                #         asyncio.ensure_future(init_urls(url, session))


async def mainpro(loop):
    # 等待mysql连接建立好
    pool = await aiomysql.create_pool(host='192.168.122.205', port=3306,
                                      user='root', password='fengxiaoxiaoxi', db='aiomysqltest',
                                      loop=loop, charset='utf8', autocommit=True)

    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(mainpro(loop))
    loop.run_forever()
