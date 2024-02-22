import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
building = [[] for _ in range(n+1)]

indegree = [0] * (n + 1)
cost = [0] * (n + 1)

for i in range(1, n+1):
    data = list(map(int, input().split()))[:-1]
    cost[i] = data[0]
    buildings = data[1:]

    for b in buildings:
        building[b].append(i)
        indegree[i] += 1
        

def topology_sort():
    que = deque()
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()
        result[now] += cost[now]
        for b in building[now]:
            indegree[b] -= 1
            result[b] = max(result[b], result[now])
            if indegree[b] == 0:
                que.append(b)
    return result


answer = topology_sort()
for i in range(1, n + 1):
    print(answer[i])