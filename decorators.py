from functools import wraps

def outer():
    number = 5

    def inner():
        print(number)

    inner()

def apply(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# print(apply(add, 5, 5))
# print(apply(sub, 2, 8))

def close():
    x = 5
    def inner():
        print(x)
    return inner

# closure = close()
# closure()

def add_to_five(num):
    def inner():
        print(num+5)
    return inner

# fifteen = add_to_five(10)
# fifteen()

def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner():
        logging.debug("Called {}".format(func.__name__))
        return func()
    return inner

def logme2(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)
    # inner.__doc__ = func.__doc__
    # inner.__name__ = func.__name__
    return inner


@logme
def sub2(x, y):
    """Returns the difference between two numbers"""
    return x - y 