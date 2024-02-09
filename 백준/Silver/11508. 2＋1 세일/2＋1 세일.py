import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
items = []

for _ in range(n):
    heappush(items, -int(input()))

total = 0
for i in range(n):
    n = heappop(items)
    if (i+1) % 3 != 0:
        total += -n

print(total)