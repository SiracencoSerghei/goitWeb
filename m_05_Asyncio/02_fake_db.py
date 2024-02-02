import asyncio
from time import sleep, time

from faker import Faker

fake = Faker()

def get_user_from_db(uuid: int)->dict:
    sleep(0.5)
    return {"id": uuid, 
            "name" : fake.name(), 
            "company": fake.company(),
            "email": fake.email()}
    
async def get_user_async_from_db(uuid: int)->dict:
    sleep(0.5)
    return {"id": uuid, 
            "name" : fake.name(), 
            "company": fake.company(),
            "email": fake.email()}
async def main():
    for uuid in [1,2,3]:
        user = await get_user_async_from_db(uuid)
        print(user)
        
if __name__ == "__main__":
    start = time()
    for uuid in  range(2):
        user = get_user_from_db(uuid)
        print(user)
    print("Sync version took {} seconds".format(time() - start))
    print('--------------------')
    start = time()
    asyncio.run(main())
    print(f"Async version took {time()-start}")

