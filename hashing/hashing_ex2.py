n = [1, 4, 7, 5, 3, 7, 9, 10, 4, 6, 3, 7, 3] # between 0 to 10
m = [10, 111, 7, 30, 2, 4]

sol = dict()
for i in range(len(n)):
    if n[i] in sol:
        sol[n[i]] += 1
    else:
        sol[n[i]] = 1

# print(sol)
for nums in m:
    if nums in sol:
        print(f"Count of {nums} is {sol[nums]}")
    else:
        print(f"Count of {nums} is 0")
    
