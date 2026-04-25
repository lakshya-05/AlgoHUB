# method 1
lst = [1, 1, 3, 5, 4, 2, 4, 5, 8, 1, 3, 1]
f = dict()
for i in range(0, len(lst)):    # O(n)
    if lst[i] in f:
        f[lst[i]] += 1
    else:
        f[lst[i]] = 1

print(f)

# method 2 (.get())
res = {}    # dict
for i in range(0, len(lst)):    # O(n)
    res[lst[i]] = res.get(lst[i], 0) + 1

print(res)
