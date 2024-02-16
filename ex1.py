def merge(arr, low, mid, high):
    arrayLengthL = mid - low + 1    
    arrayLengthR = high - mid

    #
    left = [0] * arrayLengthL
    right = [0] * arrayLengthR

    for i in range(arrayLengthL):
        left[i] = arr[low + i]

    for j in range(arrayLengthR):
        right[j] = arr[(mid + 1) + j]

    i = 0     
    j = 0     
    k = low   
    
    while i < arrayLengthL and j < arrayLengthR:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < arrayLengthL:
        arr[k] = left[i]
        i += 1
        k += 1

    
    while j < arrayLengthR:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr,low, mid, high)
 
arr = [8,42,25,3,3,2,27,3]

merge_sort(arr, 0, len(arr)-1)
print(arr)
