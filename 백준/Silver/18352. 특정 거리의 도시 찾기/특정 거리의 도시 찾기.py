from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

cityMap = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    start, end = map(int, input().split())
    cityMap[start].append(end)

def bfs(n):
    que = deque()
    que.append(n)
    visited[n] += 1

    while que:
        now = que.popleft()
        for new in cityMap[now]:
            if visited[new] == -1:
                que.append(new)
                visited[new] = visited[now] + 1

bfs(x)

have = False

for i in range(n+1):
    if visited[i] == k:
        print(i)
        have = True

if not have: print(-1)