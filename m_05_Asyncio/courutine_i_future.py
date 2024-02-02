import asyncio

async def async_task(name):
    print(f"Start {name}")
    await asyncio.sleep(2)
    print(f"End {name}")
    return f"Result from {name}"

async def main():
    
    # var 1=========================================
    
    task1 = async_task("Task 1")
    task2 = async_task("Task 2")

    # Отримуємо об'єкти Future для асинхронних задач, 
    # алє це буде підтипом Task
    future1 = asyncio.ensure_future(task1)
    future2 = asyncio.ensure_future(task2)
    print("future1: ", type(future1)) #  <class '_asyncio.Task'>
    # asyncio.ensure_future створює таску з фьючера... 
    # котра автоматом потрапляє у евент луп 
    # Отже, основна різниця полягає в тому, що Task - це 
    # конкретна реалізація Future, яка автоматично приєднується 
    # до циклу подій та призначена для представлення виконання 
    # конкретної асинхронної операції. 
    # Спрощено кажучи, Task - це свого роду розширений Future, 
    # спрощений для використання в контексті асинхронності.
    
    # Очікуємо на завершення обох фьючерсів
    await asyncio.gather(future1, future2)

    # Отримуємо результати
    result1 = future1.result()
    result2 = future2.result()
    
    print("Results:", result1, result2)
    
    # var 2 ================================================
    
    # Ви може створити Future за допомогою asyncio.Future().
    # Future не автоматично додається до циклу подій, і його 
    # треба ручно завершити або додати до циклу подій.

    my_future = asyncio.Future()
    print('my_future: ', type(my_future)) # <class '_asyncio.Future'>
    my_future.set_result(async_task("my_future"))
     
    result = await my_future.result()
    print("Custom Result: ", result)
    
    # ====================================

# Запускаємо цикл подій
asyncio.run(main())

