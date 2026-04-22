n = 40

factors = list()
for i in range(1, (n//2)+1):     # time complexity O(n)
    if n % i == 0:
        factors.append(i)

print(factors)

# More Optimal solution
factors = list()
for i in range(1, int((n**0.5))+1):     # O(sqrt(n))
    if n % i == 0:
        factors.append(i)
        factors.append(int(n/i))

factors.sort()  # O(nlog(n))
print(factors)
