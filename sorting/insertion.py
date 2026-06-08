# Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr



arr = [8,2,4,6,3,9,5,1,7,0]
print(insertion_sort(arr))

