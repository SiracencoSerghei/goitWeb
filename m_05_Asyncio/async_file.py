import asyncio
from aiofile import async_open, AIOFile, LineReader


async def main():
    async with async_open("hello.txt", 'w+') as afp:
        await afp.write("Hello ")
        await afp.write("world\n")
        await afp.write("Hello from - async world!")

    async with async_open("hello.txt", 'r') as afp:
        async for line in afp:
            print("async_open: ",line)

    async with AIOFile("hello.txt", 'r') as afp:
        async for line in LineReader(afp):
            print('AIOFile: ', line)


if __name__ == '__main__':
    asyncio.run(main())
