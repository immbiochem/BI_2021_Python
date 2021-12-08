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
        return np.dot(a, b)
    else:
        print('Parameters are not suitable for multiplication')
        return None


# Create multiplication_check
def multiplication_check(matrix_list):
    n = len(matrix_list)
    for i in range(n - 1):
        if matrix_list[i].shape[1] != matrix_list[i].shape[0]:
            return False
    return True


# Create multiply_matrices
def multiply_matrices(matrix_list):
    if multiplication_check(matrix_list):
        x = matrix_list[0]
        for i in matrix_list[1:]:
            x = np.dot(x, i)
        return x
    else:
        return None


# Create compute_2d_distance
def compute_2d_distance(a, b):
    return np.sqrt(sum((a-b)**2))


# Create compute_multidimensional_distance
def compute_multidimensional_distance(a, b):
    n = len(a)
    sum_dist_sqr = 0
    for i in range(n):
        sum_dist_sqr += (a[i] - b[i]) ** 2
    return sum_dist_sqr ** 0.5


# Create compute_pair_distances
def compute_pair_distances(a):
    n = len(a)
    pair_matrix = np.zeros((n, n))
    for i in range(a.shape[0]):
        for j in range(a.shape[0]):
            pair_matrix[i][j] = compute_multidimensional_distance(a[i], a[j])
    return pair_matrix
