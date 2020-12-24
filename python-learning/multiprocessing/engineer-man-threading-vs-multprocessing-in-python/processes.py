from multiprocessing import Process
import os
import math


def calc():
    # increased as 4 M program run too fast to see python processes
    for i in range(0, 40000000):
        math.sqrt(i)


def multi_processing():
    processes = []

    for i in range(os.cpu_count()):
        print(f"registering process {i}...")
        processes.append(Process(target=calc))

    for process in processes:
        process.start()

    for process in processes:
        process.join()


# https://stackoverflow.com/a/24374798
# Needed to add the below to avoid freeze_support omitted error message
if __name__ == "__main__":
    multi_processing()

"""
Full Error Message:
RuntimeError: 
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.
"""
