import sys
input = sys.stdin.readline

n, w = map(int, input().split())
tree = [[] for _ in range(n+1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

cnt = 0
for i in range(2, n + 1):
    if len(tree[i]) == 1:
        cnt += 1

print(w/cnt)