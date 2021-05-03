import aiohttp
import asyncio
from rich import print

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://51.15.17.205:9000/tick/') as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            html = await response.text()
            json = await response.json()

            # print("Body:", html[:15], "...")
            print(json)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())