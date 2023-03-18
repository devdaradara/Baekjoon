import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [(i+1) for i in range(n)]

for i in range(m):
    first, end = map(int, input().split())
    tmp = basket[first-1]
    basket[first-1] = basket[end-1]
    basket[end-1] = tmp

for ball in basket:
    print(ball, end=" ")