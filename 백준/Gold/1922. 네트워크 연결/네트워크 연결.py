import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
lines = []
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    lines.append((c, a, b))

lines.sort()


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total = 0
for line in lines:
    cost, a, b = line
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total += cost

print(total)