import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [(i+1) for i in range(n)]

for i in range(m):
    start, end = map(int, input().split())
    basket = basket[:start-1] + basket[start-1:end][::-1] + basket[end:]

for basekt_num in basket:
    print(basekt_num, end=" ")