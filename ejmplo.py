def a_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(j)
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", arr)
print("Lista ordenada:", a_sort(arr))