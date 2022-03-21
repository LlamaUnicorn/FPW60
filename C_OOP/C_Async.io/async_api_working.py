import aiohttp
import asyncio
import time
import json

t_0 = time.time()


async def day_rate(session, day):
    async with session.get(f"f'https://api.exchangerate.host/2020-01-{day}?base=USD&symbols=RUB&places=2") as resp:
        r = await resp.json()
        print(r)
        total_base = json.loads(r.content)['rates']
        print(total_base)
        return r["rates"]["RUB"]

        # https: // api.exchangerate.host / 2020 - 02 - 01?base = USD & symbols = RUB & places = 2
        # r = requests.get(f'https://api.exchangerate.host/2020-01-{day}?base=USD&symbols=RUB&places=2')
        # # total_base = json.loads(r.content)[currency[base]]
        # # total_base = r.json()
        # total_base = json.loads(r.content)['rates']
        # message = f"Цена USD в RUB : {total_base}"
        # return message


async def main():
    async with aiohttp.ClientSession() as session:
        resps = [day_rate(session, day) for day in range(1, 31)]
        rates = await asyncio.gather(*resps)

    dt = time.time() - t_0
    print(f"Затрачено {dt:.2f} секунды")
    print(rates)


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())
