# merge sort

# merging 2 sorted arrays

def merge_array(left, right):
    res = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < n:
        res.append(left[i])
        i += 1
    while j < m:
        res.append(right[j])
        j += 1
    return res



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left=left, right=right)



arr = [3,1,4,6,8,2,5,0,9,7]
print(merge_sort(arr))


