import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
times = []
lecture = []

for _ in range(n):
    times.append(list(map(int, input().split())))
times.sort()

heappush(lecture, times[0][1])

for i in range(1, n):
    if times[i][0] < lecture[0]:
        heappush(lecture, times[i][1])
    else:
        heappop(lecture)
        heappush(lecture, times[i][1])

print(len(lecture))