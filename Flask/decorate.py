#!/usr/bin/python3


# Decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


# same functionality with line 18
@decorator_function
def display():
    print("display function ran")


@decorator_function
def display_info(name, age):
    print("display info ran with arguments ({}, {})".format(name, age))


display_info("emeka", 34)

# decorated_display = decorator_function(display)

# decorated_display()
# display()
