from threading import Thread
from time import sleep
import logging


def example_work(delay, sec):
    sleep(delay)
    logging.debug(f'Wake up!-{sec}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    for i in range(5):
        thread = Thread(target=example_work, args=(i,i))
        thread.start()
    thread.join()
    logging.debug('Some stuff')
    