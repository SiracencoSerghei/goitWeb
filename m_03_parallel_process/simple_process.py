from multiprocessing import Process, cpu_count
import os
import psutil

def print_word(word):
    process_id = os.getpid()
    process_name = psutil.Process(process_id).name()
    core_number = psutil.Process(process_id).cpu_num()

    print(f"Process ID: {process_id}, Process Name: {process_name}, Core Number: {core_number}, Word: hello, {word}")

def get_cpu_core_count():
    try:
        core_count = cpu_count()
        print(f"Number of CPU cores: {core_count}")
    except Exception as e:
        print("Failed to determine the number of CPU cores.")
        print(f"Error: {e}")
        return None
    
if __name__ == '__main__':
    
    p = Process(target=get_cpu_core_count)
    
    p1 = Process(target=print_word, args=('bob', ), daemon=True)
    p2 = Process(target=print_word, args=('alice', ), daemon=True)
    
    p.start()
    p1.start()
    p2.start()
    
    p.join()
    p1.join()
    p2.join()
    