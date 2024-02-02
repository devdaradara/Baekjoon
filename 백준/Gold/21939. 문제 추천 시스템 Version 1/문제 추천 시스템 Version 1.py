import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
min_pro = []
max_pro = []
solved = {}

for _ in range(n):
    p, l = map(int, input().split())
    heappush(min_pro, (l, p))
    heappush(max_pro, (-l, -p))
    solved[p] = False

m = int(input())

for i in range(m):
    full = input().rstrip()
    if full[0] == "r":
        cmd, x = full.split()
        if x == "1":
            while solved[-max_pro[0][1]]:
                heappop(max_pro)
            print(-max_pro[0][1])
        else:
            while solved[min_pro[0][1]]:
                heappop(min_pro)
            print(min_pro[0][1])

    elif full[0] == "a":
        while solved[-max_pro[0][1]]:
            heappop(max_pro)
        while solved[min_pro[0][1]]:
            heappop(min_pro)
        cmd, p, l = full.split()
        heappush(min_pro, (int(l), int(p)))
        heappush(max_pro, (-int(l), -int(p)))
        solved[int(p)] = False

    elif full[0] == "s":
        cmd, p = full.split()
        solved[int(p)] = True