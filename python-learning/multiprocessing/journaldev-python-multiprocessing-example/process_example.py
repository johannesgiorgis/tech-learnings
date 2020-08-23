"""
Process Example
"""

from multiprocessing import Process


def print_func(continent="Asia"):
    print(f"The name of continent is : ", continent)


if __name__ == "__main__":
    names = ["America", "Europe", "Africa"]
    procs = []

    # instantiating without any argument
    print("instantiating process without any argument")
    proc = Process(target=print_func)
    procs.append(proc)
    proc.start()

    # instantiating processs with arguments
    print("instantiating process with arguments")
    for name in names:
        print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    print("complete the processes")
    for proc in procs:
        proc.join()
