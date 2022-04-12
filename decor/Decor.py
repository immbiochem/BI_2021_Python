#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import random
import requests


# Task 1
def time_this(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)  # wait for the function to complete
        end = time.time()
        return end - start

    return inner_function


# Demonstration 1
if __name__ == '__main__':
    @time_this
    def some_function(a, b, c, d, e=0, f=2, g='3'):
        time.sleep(a)
        time.sleep(b)
        time.sleep(c)
        time.sleep(d)
        time.sleep(e)
        time.sleep(f)
        return g

    some_function(1, 2, 3, 4, e=5, f=6, g='99999')


# Task 2
def function_logging(func):
    def inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return_type = str(type(result)).split("'")[1]
        if args and kwargs:
            print(f'Function {func.__name__} is called with position arguments: {args} and keyword arguments {kwargs}')
        elif args:
            print(f'Function {func.__name__} is called with position arguments: {args}')
        else:
            print(f'Function {func.__name__} is called with keyword arguments: {kwargs}')
        print(f'Function {func.__name__} returns output of type {return_type}')
        return result

    return inner_function


# Demonstration 2
if __name__ == '__main__':
    @function_logging
    def func3(a, b, c, d=4):
        return [a + b * c] * d

    print(func3(1, 2, c=3, d=2), end='\n\n')


# Task 3
def russian_roulette_decorator(probability=0.2, return_value="(/¯◡ ‿ ◡)/¯☆*"):
    def decorator(func):
        def inner_func(*args, **kwargs):
            if round(random.uniform(0, 1), 2) > probability:
                return func(*args, **kwargs)
            return return_value

        return inner_func

    return decorator


# Demonstration 3
if __name__ == '__main__':
    @russian_roulette_decorator(probability=0.2, return_value="Ooops, your output has been stolen!")
    def make_request(url):
        return requests.get(url)

    for _ in range(10):
        print(make_request('https://google.com'))
