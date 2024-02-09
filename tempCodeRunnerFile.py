for l in range(mid, high+1):
            for m in range(mid + 1, high+1):
                print(arr)
                if arr[l]> arr[m]:
                    arr[l], arr[m] = arr[m], arr[l]