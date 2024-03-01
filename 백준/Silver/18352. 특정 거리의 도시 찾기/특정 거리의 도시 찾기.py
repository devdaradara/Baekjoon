import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)



def bfs(start):
    que = deque()
    que.append((start, 0))
    visited[start] = True
    answer = []

    while que:
        now, dist = que.popleft()
        if dist == k:
            answer.append(now)
            continue
        for i in graph[now]:
            if not visited[i]:
                que.append((i, dist + 1))
                visited[i] = True
    return answer


answer = bfs(x)
answer.sort()
if answer:
    for a in answer:
        print(a)
else:
    print(-1)