"""
Multiprocessing Pool Example
"""

from multiprocessing import Pool
import time

work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])


def work_log(work_data):
    print(f" Process {work_data[0]} waiting {work_data[1]} seconds")
    time.sleep(int(work_data[1]))
    print(f" Process {work_data[0]} Finished.")


def pool_handler():
    p = Pool(4)
    p.map(work_log, work)


if __name__ == "__main__":
    pool_handler()
