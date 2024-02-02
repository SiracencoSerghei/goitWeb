import threading
from threading import Thread
from time import sleep

def worker(msg):
    for i in range(0, 10):
        print(f"{msg}*", end="", flush=True)
        sleep(0.1)
        
        
# print('Starting\r')
# t1 = Thread(target=worker, args='A')
# t2 = Thread(target=worker, args='B')
# t3 = Thread(target=worker, args='C')
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print('\t\r')
# print('Done')
    
        
# class WorkerThread(Thread):
#     def __init__(self, daemon=None, target=None, name=None):
#         super().__init__(daemon=daemon, target=target,name=name)
#     def run(self):
#         print(f"the  {self.name} is running\n")
#         for i in range(0, 10):
#             print(f'. of {self.name}\n', flush=True)
#             sleep(1)
#         print(f"the  {self.name} has finished\n")
        
        

# def run_threads(quantity_of_threads):
#     threads = []

#     for _ in range(quantity_of_threads):
#         thread = WorkerThread()
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()
    
if __name__ == "__main__":

    # print('Starting')

    # run_threads(3)


    # print('\t\r')
    # print('\nDone')
    
    t1 = Thread(name='worker', target=worker, args='A')
    t2 = Thread(target=worker, args='B') # use default name e.g. Thread-1
    d = Thread(daemon = True, name='daemon', target=worker, args='C')
    t1.start()
    t2.start()
    d.start()
    print()
    for t in threading.enumerate():
        print(t.name)

