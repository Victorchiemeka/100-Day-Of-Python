#!/usr/bin/python3
from typing import Any


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwds):
        print(
            "Call method executed this before {}".format(
                self.original_function.__name__
            )
        )
        return self.original_function(*args, **kwds)


@decorator_class
def display():
    print("display function ran")


display()
