import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


def bfs(node):
    que = deque()
    que.append(node)
    visited[node] = True
    while que:
        now = que.popleft()
        for new in graph[now]:
            if not visited[new]:
                que.append(new)
                visited[new] = True


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        bfs(i)

print(cnt)