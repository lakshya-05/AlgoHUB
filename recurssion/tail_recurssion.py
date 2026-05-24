# for printing n to 1 (backwards - 5 4 3 2 1)

def tail(i,n):
    if i>n:
        return
    tail(i+1, n)
    print(i)

tail(1,5)
