import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = deque([(i+1) for i in range(n)])
pops = list(map(int, input().split()))

cnt = 0
for p in pops:
    while True:
        if arr[0] == p:
            arr.popleft()
            break
        else:
            if arr.index(p) <= len(arr) // 2:
                arr.rotate(-1)
                cnt += 1
            else:
                arr.rotate(1)
                cnt += 1

print(cnt)