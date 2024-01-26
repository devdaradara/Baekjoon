import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    impt = deque()
    done = [False] * n

    for i in range(n):
        impt.append((i, tmp[i]))

    tmp.sort(reverse=True)

    cnt = 0

    while not done[m]:
        new = impt.popleft()
        if new[1] < tmp[0]:
            impt.append(new)
        else:
            done[new[0]] = True
            cnt += 1
            tmp.pop(0)

    print(cnt)