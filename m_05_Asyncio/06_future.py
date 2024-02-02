#  Awaitable -> Coroutine
#  Awaitable -> Future -> Task

import asyncio
from time import sleep, time

async def send_metrics(url):
    print(f"Send to {url}: {time()}")
    
async def worker():
    while True:
        await asyncio.sleep(1)
        await send_metrics('')

if __name__ == '__main__':
    start = time()
    
    print(time() - start)
    print('---------------')
   
    # asyncio.run(worker())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(worker())
    loop.run_forever()
    