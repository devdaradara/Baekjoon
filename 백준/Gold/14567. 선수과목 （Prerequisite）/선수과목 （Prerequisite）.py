import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology():
    answer = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i, 1))

    while q:
        now, time = q.popleft()
        answer[now] = time
        for new in graph[now]:
            indegree[new] -= 1
            if indegree[new] == 0:
                q.append((new, time+1))
    return answer


answer = topology()
for a in answer[1:]:
    print(a, end = " ")