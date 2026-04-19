n = 511114

num = n     # never change a input

# method - 1
count = 0
while num > 0:
    num = num // 10     # 5873 -> 587 
    count += 1
print(count)

# method - 2
import numpy as np
res = int(np.log10(n)+1)
print(res)
