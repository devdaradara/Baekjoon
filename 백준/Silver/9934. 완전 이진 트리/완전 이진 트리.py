import sys
input = sys.stdin.readline

k = int(input())
cities = list(map(int, input().split()))
building = [[] for _ in range(k)]

def check(depth, array):
    if depth + 1 == k:
        building[depth].append(array[0])
        return
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid+1:]
    check(depth+1, left)
    building[depth].append(array[mid])
    check(depth+1, right)

check(0, cities)
for b in building:
    for bb in b:
        print(bb, end=" ")
    print()
