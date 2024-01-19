import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

student = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    student[a].append(b)
    inDegree[b] += 1

que = deque()

for i in range(1, n+1):
    if inDegree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    print(now, end=" ")
    for new in student[now]:
        inDegree[new] -= 1
        if inDegree[new] == 0:
            que.append(new)
