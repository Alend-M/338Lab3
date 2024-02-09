import sys 
sys.setrecursionlimit(20000)



def merge(arr:list, low, mid, high):
    arr1Size = (mid +1) - low
    arr2Size = high - (mid) 

    #Case 1: Arrays are of 1 element
    if arr1Size == 1 and arr2Size == 1:
        if arr[0] > arr[mid + 1]:         #if left element greater then right swap
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
    else:
        for i in range(arr1Size):       #itterates through left array
           for k in range (mid+1, high+1):      #itterates through right array
               print(f"Arr: {arr} index: {arr[i]} vs {arr[k]}")
               if arr[i] > arr[k]:         #if left is bigger then right
                   print("SWAP")
                   temp = arr[k]           #save value so we have it after removing
                   arr.pop(k)               #remove value from right
                   arr.insert(i,temp)       #put right value in left array
        for l in range(mid+2, high+1):
            for m in range(mid + 3, high):
                print(f"Arr!!!!!: {arr} index: {arr[l]} vs {arr[m]}")
                if arr[l]> arr[m]:
                    print("SAWP")
                    arr[l], arr[m] = arr[m], arr[l]

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr,low, mid, high)
        

arr = [8,42,25,3,3,2,27,3]


merge_sort(arr, 0, len(arr)-1)
print(arr)

