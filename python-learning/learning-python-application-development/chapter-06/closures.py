"""
Closures Example
"""


def initial_number(x):
    print("1. Initial number " f"(orig environment during function creation): {x}")

    def modified_number(y):
        print(f" x: {x}, y: {y} , x+y: {x+y}")
        return x + y

    return modified_number


if __name__ == "__main__":
    foo = initial_number(100)
    print("2. Now calling this function with " "its original environment loaded:")
    # foo(1)
    # foo(5)
