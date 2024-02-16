import timeit as ti
import random 
import matplotlib.pyplot as plt

#6.1
def linear_search(arr = [], target = 0):
    #6.2 for linear
    if len(arr) == 0:
        size = 10
        arr = [random.randint(0,10000) for n in range(size)]
        target = random.choice(arr)
    random.shuffle(arr)
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

def quicksort(arr):
    random.shuffle(arr)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

def binary_quicksort(arr=[], target = 0):
    #6.2 for binary search
    if len(arr) == 0:
        size = 10
        arr = [random.randint(0,10000) for n in range(size)]
        target = random.choice(arr)
    return binary_search(arr=quicksort(arr),target=target)


ans1 = ti.timeit(lambda:linear_search(), number=100)
ans2 = ti.timeit(lambda:binary_quicksort(), number=100)
print(f"linear:{ans1:.8f}\nBinary:{ans2:.8f}")

#6.3
sizeArray = [10, 20, 50, 100, 200,500, 1000, 2000, 5000, 10000]  #Different array sized to test
xArray = []                                                      #where to hold size of array to plot
linearArray = []                                                 #where to hold linear array time to plot 
binaryArray = []                                                 #where to hold bineary array time to plot 

for i in sizeArray:                                                     #loops through size array to test all sizes
    size = i

    arr = [random.randint(0,10000) for n in range(size)]                #makes a array holding random int
    target = random.choice(arr)                                         #selects a random target

    ans1 = ti.timeit(lambda:linear_search(arr,target), number=100)
    ans2 = ti.timeit(lambda:binary_quicksort(arr,target), number=100)
    xArray.append(size)
    linearArray.append(ans1)
    binaryArray.append(ans2)

#6.4
plt.figure(figsize=(10, 5))
plt.plot(xArray, linearArray, label='Linear Search')
plt.plot(xArray, binaryArray, label='Binary Search')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Linear Search vs Binary Search')
plt.legend()
plt.grid(True)
plt.show()
#6.4 discussion: Based on the results linear search is far faster

#6.5
arr = [1,2,3,4,5,6,7,8,9,10]    #Worse case for quicksort is a already sorted array
target = 3
ans1 = ti.timeit(lambda:linear_search(arr,target), number=100)
ans2 = ti.timeit(lambda:binary_quicksort(arr,target), number=100)
print(f"linear:{ans1:.8f}\nBinary:{ans2:.8f}")