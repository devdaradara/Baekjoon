import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input().rstrip())

nums = PriorityQueue()
minus = 0
zero = 0
one = 0
plus = 0
sumMul = 0

for _ in range(n):
    new = int(input().rstrip())
    if new < 0:
        minus += 1
    elif new == 0:
        zero += 1
    elif new == 1:
        one += 1
    else:
        plus += 1
    nums.put(new)

# minus
if minus > 0:
    div = minus // 2 

    for _ in range(div):
        num1 = nums.get()
        num2 = nums.get()
        sumMul += num1*num2

# zero
if zero > 0:
    if minus % 2 == 1:
        zero += 1
    for _ in range(zero):
        nums.get()
else:
    if minus % 2 == 1:
        sumMul += nums.get()

# one
if one > 0:
    for _ in range(one):
        sumMul += nums.get()

# plus
if plus > 0:
    if plus % 2:
        sumMul += nums.get()

    div = plus // 2

    for _ in range(div):
        num1 = nums.get()
        num2 = nums.get()
        sumMul += num1*num2

print(sumMul)