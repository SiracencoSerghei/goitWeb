import asyncio

class Task:
    def __init__(self, idx: int) -> None:
        self.idx = idx

    async def run(self) -> None:
        print(f"Task {self.idx} in progress")
        await asyncio.sleep(1)
        print(f"Task {self.idx} finished")


async def main():
    tasks = []
    for i in range(1, 4):
        task = Task(i)
        print(type(task.run()))
        tasks.append(task.run())

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
