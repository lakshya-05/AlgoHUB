# for printing n to 1 (forward - 1 2 3 4 5)

def head(i,n):
    if i>n:
        return
    print(i)
    head(i+1, n)

head(1,5)
