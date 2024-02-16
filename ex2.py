# ex2.py

import matplotlib.pyplot as plt
import numpy as np
import random
import time
import sys 

sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    if (n <= 1):
        return arr
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def plot(input_sizes, quick_times, bubble_times, type):
    plt.figure(figsize = (10, 8))
    plt.plot(input_sizes, bubble_times, label = "Bubble Sort", marker = 'o')
    plt.plot(input_sizes, quick_times, label = "Quick Sort", marker = 'o')
    plt.xlabel("Size of Input Array")
    plt.ylabel("Time Taken")
    plt.title(f'Bubble Sort vs. Quick Sort {type} Timing Comparison')
    plt.legend()
    plt.show()

def test_arrays(size):
    test_array = []
    for size in size:
        values = [random.randint(0, 500) for i in range(size)]
        test_array.append(values)
    return test_array

def test(type, cases):
    runtimes = []
    for case in cases:
        start = time.time()
        type(case)
        end = time.time()
        runtimes.append(end - start)
    return runtimes

array_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 10000]

best = [list(range(0, size, 1)) for size in array_sizes]
worst = [list(range(size, 0, -1)) for size in array_sizes]
avg = test_arrays(array_sizes)

bubble_best = test(bubble_sort, best)
bubble_worst = test(bubble_sort, worst)
bubble_average = test(bubble_sort, avg)

quick_best = test(quick_sort, best)
quick_worst = test(quick_sort, worst)
quick_average = test(quick_sort, avg)

plot(array_sizes, bubble_best, quick_best, "Best")
plot(array_sizes, bubble_average, quick_average, "Average")
plot(array_sizes, bubble_worst, quick_worst, "Worst")