import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [(i+1) for i in range(n)]

for i in range(m):
    begin, end, mid = map(int, input().split())
    basket = basket[:begin-1] + basket[mid-1:end] + basket[begin-1:mid-1] + basket[end:]


for basekt_num in basket:
    print(basekt_num, end=" ")