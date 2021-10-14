import aiomysql
import asyncio


async def select(loop, sql, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)
            r = await cur.fetchone()
            print(r)


async def insert(loop, sql, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)
            await conn.commit()


async def main(loop):
    pool = await aiomysql.create_pool(
        host='192.168.122.205',
        port=3306,
        user='root',
        password='fengxiaoxiaoxi',
        db='aiomysqltest',
        loop=loop)
    # c1 = select(loop=loop, sql='select * from minifw limit 1', pool=pool)
    c1 = insert(loop=loop, sql="insert into artitle_test(title) values ('hello')", pool=pool)
    c2 = insert(loop=loop, sql="insert into artitle_test(title) values ('heloko')", pool=pool)

    tasks = [asyncio.ensure_future(c1), asyncio.ensure_future(c2)]
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    cur_loop = asyncio.get_event_loop()
    cur_loop.run_until_complete(main(cur_loop))
