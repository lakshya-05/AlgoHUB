# sum of 1 to n

def add(sum, i, n):
    if i>n:
        print(f"Sum is {sum}")
        return
    add(sum+i, i+1, n)

add(0, 1, 7)

