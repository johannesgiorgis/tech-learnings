from threading import Thread
import os
import math


def calc():
    for i in range(0, 4000000):
        math.sqrt(i)


def threads():
    threads = []

    for i in range(os.cpu_count()):
        print(f"registering thread {i}...")
        threads.append(Thread(target=calc))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    threads()