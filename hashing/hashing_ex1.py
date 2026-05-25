n = [1, 4, 7, 5, 3, 7, 9, 10, 4, 6, 3, 7, 3] # between 0 to 10

hash_list = [0] * 11
for i in n:
    hash_list[i] += 1

# print(hash_list)

# Check number of frequencies of below in n
m = [10, 111, 7, 30, 2, 4]

for i in m:
    if i >= 0 and i <= 10:
        print(f"freq of {i} in n is {hash_list[i]}")
    else:
        print(f"freq of {i} in n is 0")
