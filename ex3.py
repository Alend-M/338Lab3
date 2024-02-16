import matplotlib.pyplot as plt
import numpy as np
import random




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
    return comparisons, swaps



#increasing input lengths, don't go passed "small" number of inputs
# but wait for maryam to figure out what small is
all_arrays = [
[random.randint(0, 1000) for _ in range(5)],
[random.randint(0, 1000) for _ in range(10)],
[random.randint(0, 1000) for _ in range(20)],
[random.randint(0, 1000) for _ in range(50)],
[random.randint(0, 1000) for _ in range(75)],
[random.randint(0, 1000) for _ in range(100)],
[random.randint(0, 1000) for _ in range(200)],
]



sizes = []
comparisons_data = []
swaps_data = []


# Test the arrays and collect data
for arr in all_arrays:
    size = len(arr)
    sizes.append(size)
    comparisons, swaps = bubble_sort(arr.copy())
    comparisons_data.append(comparisons)
    swaps_data.append(swaps)

# Interpolating data
x_new = np.linspace(min(sizes), max(sizes), 300)
p_comparisons = np.polyfit(sizes, comparisons_data, 3) #make the data fit to cubic polynomial
p_swaps = np.polyfit(sizes, swaps_data, 3)
comparisons_interp = np.polyval(p_comparisons, x_new)
swaps_interp = np.polyval(p_swaps, x_new)

# Plotting

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(sizes, comparisons_data, marker='o', label = "Actual Comparisons")
plt.plot(x_new, comparisons_interp, color= 'r',alpha = 0.75, linestyle = 'dashed', label="Interpolated Comparisons")
plt.xlabel('Size of Array')
plt.ylabel('Number of Comparisons')
plt.title('Comparisons by Input Size')
plt.legend()
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(sizes, swaps_data, marker='o', label = "Actual Swaps")
plt.plot(x_new, swaps_interp,color= 'r', alpha = 0.75, linestyle = 'dashed', label="Interpolated Swaps")
plt.xlabel('Size of Array')
plt.ylabel('Number of Swaps')
plt.title('Swaps by Input Size')
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.show()
