#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# Create three arrays
ar1 = np.array([1, 2, 3])
ar2 = np.arange(1, 4)
ar3 = np.zeros(3) + ar1


# Create matrix_multiplication
def matrix_multiplication(a, b):
    if a.shape[1] == b.shape[0]:
        a_col = a.shape[1]
        a_row = a.shape[0]
        b_col = b.shape[1]
        c = []
        for i in range(a_row):
            g = []
            for j in range(b_col):
                p = 0
                for n in range(a_col):
                    t = a[i][n] * b[n][j]
                    p += t
                g += [p]
            c += [g]
        return np.array(c)
    else:
        print('Parameters are not suitable for multiplication')
        return None


# Create multiplication_check
def multiplication_check(matrix_list):
    ret = True
    n = len(matrix_list)
    overlap = matrix_list[0].shape[1]
    for i in range(1, n - 1):
        if matrix_list[i].shape[0] == overlap:
            overlap = matrix_list[i].shape[1]
            continue
        else:
            ret = False
            break
    return ret


# Create multiply_matrices
def multiply_matrices(a):
    if multiplication_check(a):
        c = a[0]
        for i in a[1:]:
            c = matrix_multiplication(c, i)
            return c
    else:
        return None


# Create compute_2d_distance
def compute_2d_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


# Create compute_multidimensional_distance
def compute_multidimensional_distance(a, b):
    n = len(a)
    sum_dist_sqr = 0
    for i in range(n):
        sum_dist_sqr += (a[i] - b[i]) ** 2
    return sum_dist_sqr ** 0.5


# Create compute_pair_distances
def compute_pair_distances(a):
    d = []
    for i in range(a.shape[0]):
        for j in range(a.shape[0]):
            d += [((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2) ** 0.5]
    n = int((len(d)) ** 0.5)
    return np.array(d).reshape(n, n)
