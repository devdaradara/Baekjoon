import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [sys.maxsize] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

que = PriorityQueue()
que.put((0, K))
distance[K] = 0

while not que.empty():
    current = que.get()
    new = current[1]
    if visited[new]:
        continue
    visited[new] = True
    for i in graph[new]:
        node = i[0]
        dist = i[1]
        if distance[node] > dist + distance[new]:
            distance[node] = dist + distance[new]
            que.put((distance[node], node))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")