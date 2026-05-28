# reverse an array using recursion

# method-1
def reverse(arr, rev=None):
    if rev is None:
        rev = []
    if len(arr)==0:
        return rev
    rev.append(arr.pop())
    return reverse(arr, rev)


# method-2
def reverse2(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverse2(arr, left+1, right-1)


arr = [3,5,7,7,3,1,6,3,9,6,0]
print(reverse(arr))

arr = [2,4,6,8,1,3,5,7]
print(reverse2(arr, left=0, right=len(arr)-1))
