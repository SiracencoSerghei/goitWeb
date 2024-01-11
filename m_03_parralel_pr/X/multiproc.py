import timeit
from multiprocessing import Manager, Process


def factorize_single_process():
    numbers = list(range(100, 1000))
    nums_divided_by = []
    for num in numbers:
        divisors = list(filter(lambda x: num % x == 0, range(1, num + 1)))
        nums_divided_by.append(divisors)    
    return nums_divided_by


def factorize_multi_process(num, result):
    divisors = list(filter(lambda x: num % x == 0, range(1, num + 1)))
    result.append(divisors)
    

def multi_processing():
    with Manager() as manager:
        numbers = manager.list(range(100, 1000))
        results = manager.list()        
        processes = []
        for _ in range(6):
            num = numbers.pop()
            pr = Process(target=factorize_multi_process, args=(num, results))
            pr.start()
            processes.append(pr)
        [pr.join() for pr in processes]
        return results

if __name__ == "__main__":
    
    setup_code = "from __main__ import multi_processing"
    times = timeit.repeat(stmt="multi_processing()", setup=setup_code, repeat=20, number=1)
    average =  sum(times)/len(times)
    print(f"Середній час multiprocessing: ",average)
    
    setup_code = "from __main__ import factorize_single_process"
    times = timeit.repeat(stmt="factorize_single_process()",setup=setup_code, repeat=20, number=1)
    average =  sum(times)/len(times)
    print(f"Середній час singleprocessing: ",average)