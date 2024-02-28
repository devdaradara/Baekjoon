import sys
input = sys.stdin.readline
import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)

    total = 0
    while len(files) >= 2:
        new = heapq.heappop(files) + heapq.heappop(files)
        total += new
        heapq.heappush(files, new)

    print(total)
