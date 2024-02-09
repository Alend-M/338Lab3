import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n=len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j]> arr[j+1]:
                #swapping
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
                swaps +=1
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps

def test_arrays(arr):
    sorted_arr, comparisons, swaps = bubble_sort(arr)
    return comparisons, swaps
    #print("Sorted array:", sorted_arr)
    #print("Number of comparisons:", comparisons)
    #print("Number of swaps:", swaps)

#increasing input lengths, don't go passed "small" number of inputs
# but wait for maryam to figure out what small is
size2 = [4, 3]
size4 = [4,10,1,6]
size6 = [20,54,9,7,12,23]
size10 = [5,15,20,24,32, 16,7,28,4,1]
size15 = [6,66,3,82,10, 20,11,5,34,2, 22,55,11,77,33]
size25 = [2,3,6,22,97, 10,4,15,13,81, 22,55,11,77,33, 43,55,50,31,32]


sizes = [size2, size4, size6, size10, size15, size25]
sizes_names = ["size2", "size4", "size6", "size10", "size15", "size25"]
comparisons_data = []
swaps_data = []

# Test the arrays and collect data
for arr in sizes:
    comparisons, swaps = test_arrays(arr)
    comparisons_data.append(comparisons)
    swaps_data.append(swaps)

print("Sizes Names:", sizes_names)
print("Comparisons Data:", comparisons_data)
# Plotting
"""fig, ax1 = plt.subplots(1, 2, figsize=(10, 6))

# Plotting comparisons
ax1.plot(sizes_names, comparisons_data, marker='o', label='Comparisons')
comp_poly = np.poly1d(np.polyfit(range(len(sizes)), comparisons_data, 3))
ax1.plot(sizes_names, comp_poly(range(len(sizes))), linestyle='dashed', label='Comparison Interpolation')
ax1.set_xlabel('Input Size')
ax1.set_ylabel('Count')
ax1.set_title('Bubble Sort: Comparisons by Input Size')
ax1.legend()
ax1.grid(True)

# Plotting swaps
ax2 = ax1.twinx()
ax2.plot(sizes_names, swaps_data, marker='x', label='Swaps')
swaps_poly = np.poly1d(np.polyfit(range(len(sizes)), swaps_data, 3))
ax2.plot(sizes_names, swaps_poly(range(len(sizes))), linestyle='dashed', label='Swaps Interpolation')
ax2.set_xlabel('Input Size')
ax2.set_ylabel('Count')
ax2.set_title('Bubble Sort: Swaps by Input Size')
ax2.legend()
ax2.grid(True)


fig.tight_layout()
plt.title('Bubble Sort: Comparisons and Swaps by Input Size')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()"""