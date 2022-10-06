import random as r
import time

def solve(array):
    sum = 0
    for i in range(len(array)):
        s = array[i]
        if s > sum:
            sum = s
        for l in array[i+1:]:
            s = s+l
            if s > sum:
                sum = s
    return sum

print(0)
array = []
for i in range(10000):
    n = r.randint(-100,100)
    array.append(n)
a = time.time()
ss = solve(array)
print(ss)
b = time.time()
print(b-a)

