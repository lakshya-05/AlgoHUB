n = 1234321

num = n
res = 0
while num > 0:
    last_digit = num % 10
    res = res*10 + last_digit
    print(res)
    num = num // 10

if res == n:
    print(res, "is palindrome")
else:
    print("not palindrome")
