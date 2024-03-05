import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
money = [0]
money.extend(list(map(int, input().split())))
parent = [i for i in range(n+1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if money[a] < money[b]:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a, b)

answer = 0
done = set()
for i in range(1, n+1):
    if find_parent(i) not in done:
        answer += money[parent[i]]
        done.add(parent[i])

if answer <= k:
    print(answer)
else:
    print("Oh no")