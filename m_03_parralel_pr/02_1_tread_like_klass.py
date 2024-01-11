import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(threadName)s - %(message)s')

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name, daemon=True)
        self.counter = 0

    def run(self):
        while self.counter < 5:
            time.sleep(1)
            self.counter += 1
            logging.info(f"Count - {self.counter}")

# Створення двох потоків
thread1 = MyThread(name="Thread 1")
thread2 = MyThread(name="Thread 2")

# Запуск потоків
thread1.start()
thread2.start()

# Очікування завершення потоків
thread1.join()
thread2.join()

# Перевірка, чи потоки ще живі
logging.info(f"Is Thread 1 alive? {thread1.is_alive()}")
logging.info(f"Is Thread 2 alive? {thread2.is_alive()}")