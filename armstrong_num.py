n = 1634

num = n
res = 0
count = 0

while num > 0:
    count +=1
    num = num // 10 

print(count)

num = n
while num > 0:
    last = num % 10
    res = res + last**count
    num = num // 10     # complexity is O(log(n))

if res == n:
    print(n, "is an armstrong number")
else:
    print(n, "is NOT an armstrong number")