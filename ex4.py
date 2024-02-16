# ex4.py

import timeit
import numpy as np
import matplotlib.pyplot as plt
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

plt.scatter(test_input_sizes, times)
plt.xlabel("Size of Array")
plt.ylabel("Time")
plt.title("Worst Case Complexity for Quick Sort")
plt.show()