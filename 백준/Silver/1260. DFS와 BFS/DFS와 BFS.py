import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

stack = []


def dfs(node):
    visited[node] = True
    print(node, end=" ")
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


def bfs(node):
    que = deque()
    que.append(node)
    visited[node] = True
    while que:
        now = que.popleft()
        print(now, end=" ")
        for new in graph[now]:
            if not visited[new]:
                que.append(new)
                visited[new] = True




dfs(v)
print()
visited = [False] * (n+1)
bfs(v)