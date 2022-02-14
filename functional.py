#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sequential_map(*args):
    box = args[-1]
    for func in args[:- 1]:
        transformed_box = list(map(func, box))
        box = transformed_box
    return box


def consensus_filter(*args):
    box = args[-1]
    for func in args[:len(args) - 1]:
        transformed_box = list(filter(func, box))
        box = transformed_box
    return box


def conditional_reduce(func1, func2, box):
    transformed_box = list(filter(func1, box))
    item = [func2(transformed_box[0], transformed_box[1])]
    for i in range(2, len(transformed_box)):
        item.append(func2(transformed_box[i], item[-1]))
    return item[-1]


def func_chain(*args):
    def chain(mega_func):
        for i in args:
            mega_func = i(mega_func)
        return mega_func
    return chain
