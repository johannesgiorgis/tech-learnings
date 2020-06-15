"""
Example ABC

A simple example that shows how to use Abstract Base Class in Python
"""

from abc import ABCMeta, abstractmethod


class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Knight(AbstractGameUnit):
    def __init__(self):
        super().__init__()  # added by PyCharm

    def info(self):
        print("INFO: Knight")


if __name__ == "__main__":
    # Inherits from ABC
    k1 = Knight()
    k1.info()
