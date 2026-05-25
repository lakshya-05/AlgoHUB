s = "asseedmfdgsoaadejhfe"
q = ["a", "d", "e", "r"]

freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# print(freq)
for i in q:
    if i in freq:
        print(f"Count of {i} is {freq[i]}")
    else:
        print(f"Count of {i} is 0")
