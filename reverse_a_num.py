n = int(input("enter a num to reverse: "))

num = n     # never change a input
res = str()
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10     # 5873 -> 587 
    res += str(last_digit)
res = int(res)
print(res)