import sys
input = sys.stdin.readline

n = int(input())
items = list(map(int, input().split()))
items.sort()

total = items.pop()

for i in range(n-1):
    n = items.pop() / 2
    total += n

print(total)