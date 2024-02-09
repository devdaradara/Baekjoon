import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())

tips = []

for _ in range(n):
    heappush(tips, -int(input()))

answer = 0

for i in range(n):
    t = -heappop(tips) - i
    if t < 0: t = 0
    answer += t

print(answer)

