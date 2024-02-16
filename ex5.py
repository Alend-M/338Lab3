import matplotlib.pyplot as plt
import numpy as np
import time
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

 
def binary_search(arr, val, start, end):
     
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid        

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr[j+1:i+1] = arr[j:i]
        arr[j] = val
    return arr

def tests(n):
    insertion_times = []
    binary_insertion_times = []
    for size in range(1, n+1):
        data = [random.randint(0, 1000) for _ in range(size)]
        
        start_time = time.time()
        insertion_sort(data.copy())
        end_time = time.time()
        insertion_times.append(end_time - start_time)
        
        start_time = time.time()
        binary_insertion_sort(data.copy())
        end_time = time.time()
        binary_insertion_times.append(end_time - start_time)
        
    return insertion_times, binary_insertion_times




n = 1000  # maximum input size 
sizes = list(range(1, n+1))
insertion_times, binary_insertion_times = tests(n)

# Interpolating data
x_new = np.linspace(min(sizes), max(sizes), 300)
p_insert = np.polyfit(sizes, insertion_times, 3) #make the data fit to cubic polynomial
p_binsert = np.polyfit(sizes, binary_insertion_times, 3)
insertion_interp = np.polyval(p_insert, x_new)
binary_insertion_interp = np.polyval(p_binsert, x_new)

#Plotting
plt.figure(figsize=(10, 5))
plt.plot(sizes, insertion_times,color='blue',label = "Insertion sort")
plt.plot(x_new, insertion_interp, color= 'r',alpha = 0.75, linestyle = 'dashed', label="Interpolated Insertion sort")
plt.plot(sizes, binary_insertion_times, color='cyan', label = "Binary Insertion sort")
plt.plot(x_new, binary_insertion_interp, color= 'g',alpha = 0.75, linestyle = 'dashed', label="Interpolated Binary Insertion sort")
plt.xlabel('Input Size')
plt.ylabel('Time (in seconds)')
plt.title('Insertion Sort and Binary Insertion Sort Times Vs Size')
plt.legend()
plt.grid(True)
plt.show()


#4.) Discuss the results: which algorithm is faster? Why?:
'''As seen in the plot, binary insertion sort is faster, this becomes particularily more evident
as the input size grows. This is because binary insertion sort uses binary search, while regular 
insertion sort uses linear search. Binary search has worst case time complexity of O(log n) while
linear search's is O(n) (log n is better). Both sorting methods have the same worst and average-case 
time complexity (O(n)^2), but using binary search reduces the number of comparisons needed.'''

