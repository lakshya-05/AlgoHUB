# Bubble Sort

def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [4,1,7,2,9,3,5,8,6,0]
print(bubble_sort(arr))
        


# Optimized approach

def bubble_sort_optimized(arr):
    swap = False
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            return arr
    return arr

arr = [4,1,7,2,9,3,5,8,6,0]
print(bubble_sort_optimized(arr))
