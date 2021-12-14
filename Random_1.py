#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import timeit
import numpy as np
import matplotlib.pyplot as plt
import random

# TASK 1

# 1000 numbers
amount_of_num = np.arange(1, 1001)

# array generation
time_for_random = np.zeros(1000)
time_for_np_random = np.zeros(1000)
for i in range(1000):
    # for random
    start = timeit.default_timer()
    for j in range(i + 1):
        random.uniform(0, 1)
    stop = timeit.default_timer()
    time_for_random[i] = stop - start
    # for numpy
    start = timeit.default_timer()
    np.random.uniform(size=i + 1)
    stop = timeit.default_timer()
    time_for_np_random[i] = stop - start

# Common graph
fig_dims = (14, 8)
fig, axes = plt.subplots(figsize=fig_dims)
axes.plot(amount_of_num, time_for_random, color="r")
axes.plot(amount_of_num, time_for_np_random, color="g")
axes.set(xlabel='Amount of numeric', ylabel='Time, sec')
plt.legend(['Random', 'Numpy'])
plt.grid()


# TASK 2

# Merge sort
def merge(a, b):
    c = []
    ind_a = 0
    ind_b = 0
    while ind_a < len(a) and ind_b < len(b):
        if a[ind_a] < b[ind_b]:
            c.append(a[ind_a])
            ind_a += 1
        else:
            c.append(b[ind_b])
            ind_b += 1
    if ind_a == len(a):
        c += [i for i in b[ind_b:]]
    else:
        c += [i for i in a[ind_a:]]
    return (c)


def sort_merge(a):
    if len(a) <= 1:
        return (a)
    m = len(a) // 2
    left = a[:m]
    right = a[m:]
    left = sort_merge(left)
    right = sort_merge(right)
    return (merge(left, right))


# Monkey sort
def is_sorted(a):
    if len(a) <= 1:
        return True
    sort_list = [a[0] <= a[1]]
    for i in range(1, len(a) - 1):
        sort_list.append(a[i] <= a[i + 1])
    return all(sort_list)


def monkey_sort(a):
    while not is_sorted(a):
        np.random.shuffle(a)
    return a


# Arrays generation
lenght_of_list, time_for_monkey_sort = np.arange(1, 11), np.zeros(10)
time_for_merge_sort = np.zeros(10)
for i in range(10):
    a = np.arange(i)
    np.random.shuffle(a)
    # for Merge sort
    start = timeit.default_timer()
    sort_merge(a)
    stop = timeit.default_timer()
    time_for_merge_sort[i] = stop - start
    # for Monkey sort
    start = timeit.default_timer()
    monkey_sort(a)
    stop = timeit.default_timer()
    time_for_monkey_sort[i] = stop - start

# Common graph
fig_dims = (14, 8)
fig, axes = plt.subplots(figsize=fig_dims)
axes.plot(lenght_of_list, time_for_monkey_sort, color="r")
axes.plot(lenght_of_list, time_for_merge_sort, color="g")
axes.set(xlabel='Lenght of list', ylabel='Time')
plt.legend(['Monkey sort', 'Merge sort'])
plt.grid()

# TASK 3

n = 1000
x, y = np.zeros(n), np.zeros(n)
act = [1, -1]
for i in range(1, n):
    x[i], y[i] = x[i-1] + random.choice(act), y[i-1] + random.choice(act)
param = max([max(abs(x)), max(abs(y))]) + 5
fig_dims = (10, 8)
fig, axes = plt.subplots(figsize=fig_dims)
plt.plot(x, y, color="g")
axes.vlines(0, -param, param, color = 'r')
axes.hlines(0, -param, param, color = 'r')
plt.grid()

# TASK 4

x_ax = np.zeros(1000)
y_ax = np.zeros(1000)
d = {1: (10, 10), 2: (40, 40), 3: (80, 10)}
l = [1, 2, 3]
x_ax[0] = 40
y_ax[0] = 20
for i in range(1, 1000):
    sign = random.choice(l)
    x_ax[i] = d[sign][0] + x_ax[i - 1] / 2
    y_ax[i] = d[sign][1] + y_ax[i - 1] / 2

fig_dims = (10, 8)
fig, axes = plt.subplots(figsize=fig_dims)
plt.scatter(x_ax, y_ax, color="g")
plt.grid()


# TASK 5
# text = input()
def txet(text):
    text_list = list(map(lambda x: [x], text.split()))
    alpha = list(map(lambda x: list(x[0]), text_list))
    for i in range(len(alpha)):
        if len(alpha[i]) > 3:
            rand = alpha[i][1:len(alpha[i]) - 1]
            np.random.shuffle(rand)
            alpha[i] = [alpha[i][0]] + rand + [alpha[i][-1]]
    omega = list(map(lambda s: ''.join(s), alpha))
    return ' '.join(omega)
# print(txet(text))
