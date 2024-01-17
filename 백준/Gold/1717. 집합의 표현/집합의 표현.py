import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("yes")
        else:
            print("no")