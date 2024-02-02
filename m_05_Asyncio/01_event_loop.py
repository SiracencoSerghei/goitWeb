import asyncio

async def baz() -> str:
    print("Before SLEEP")
    await asyncio.sleep(3)
    print("After SLEEP")
    return "Hello World"

async def main():
    print("Hello I'm here...")
    r = baz()
    print(r)
    result = await r
    print(f"Got the result {result}")
    result = await asyncio.gather(baz(),baz(),baz())
    print(result)
    
if __name__ == "__main__":
    asyncio.run(main())