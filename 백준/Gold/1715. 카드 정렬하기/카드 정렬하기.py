import sys
input = sys.stdin.readline
from queue import PriorityQueue

num = int(input())

bundle = PriorityQueue()
check = []

for _ in range(num):
    bundle.put(int(input()))

for i in range(num - 1):
    num1 = bundle.get()
    num2 = bundle.get()
    bundle.put(num1+num2)
    check.append(num1+num2)

print(sum(check))