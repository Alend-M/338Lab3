# ex4.py

import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

sys.setrecursionlimit(20000)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less_equal_p = [i for i in arr[1:] if i <= pivot]
        greater_equal_p = [j for j in arr[1:] if j > pivot]
        return quick_sort(less_equal_p) + [pivot] + quick_sort(greater_equal_p)

test_input_sizes = range(50, 500, 50)
times = []

for size in test_input_sizes:
    array = list(range(0, size, 1))
    time = timeit.timeit(lambda: quick_sort(array), number = 1)
    times.append(time)

def quadratic_fit(x, a, b, c):
    return (a*(np.power(x, 2)) + b*x + c)

# Fit the curve to the data
quad_params, _ = curve_fit(quadratic_fit, test_input_sizes, times)

plt.scatter(test_input_sizes, times)
plt.plot(test_input_sizes, quadratic_fit(test_input_sizes, *quad_params), 'b--', label="Quadratic Fit")
plt.xlabel("Size of Array")
plt.ylabel("Time")
plt.title("Worst Case Complexity for Quick Sort")
plt.show()