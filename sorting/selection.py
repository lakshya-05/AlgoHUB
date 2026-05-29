# Selection Sort

def selection_sort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [4,1,7,2,9,3,5,8,6,0]
print(arr)
print(selection_sort(arr))

