
from datetime import datetime
import yaml
import aiohttp
import asyncio

async def _tick_(request):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://51.15.17.205:9000/tick/') as response:

                # print("Status:", response.status)
                # print("Content-type:", response.headers['content-type'])

                html = await response.text()
                json = await response.json()

                # print("Body:", html[:15], "...")
                print(json)

            return aiohttp.web.json_response(dict(json=json))

    # $>
    except Exception as exp:
    # <!
        # !0 return what's wrong in string and the type of the exception should be enough to understand where you're wrong noobs
        return aiohttp.web.json_response({'err':{'str':str(exp),'typ':str(type(exp))}}, status=500)
#`< - - - - - - - - - - - -
async def tick_all(request):
    try:

        async with aiohttp.ClientSession() as session:
            async with session.get('http://51.15.17.205:9000/tick/Mohamed') as resp:

                info = await resp.json()
                info['timestamp'] = datetime.timestamp(datetime.now())
                data = yaml.dump(info)
                filename = f"./tick/data/{datetime.now().isoformat()}.yaml"
                with open(filename, "w") as f:
                    f.write(data)

        return aiohttp.web.json_response(info)
    except Exception as e:
        print(e)
        raise e

loop = asyncio.get_event_loop()
