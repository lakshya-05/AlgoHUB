# sum of n nums

def add(n):
    if n == 1:
        return 1
    return add(n-1) + n

add(7)
