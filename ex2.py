# ex2.py

import matplotlib.pyplot as plt
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

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

def quick_sort(arr, low, high):
    if (len(arr) <= 1):
        return arr
    if (low < high):
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

array = [1, 8, 3, 10, 4]
quick_sort(array, 0, len(array) - 1)
print(array)