import sys
input = sys.stdin.readline

type, price = map(int, input().split())
coinPrice = []

for _ in range(type):
    coinPrice.append(int(input()))

cnt = 0

for i in range(type):
    money = coinPrice[type - i - 1]
    if price % money >= 0:
        cnt += price // money
        price %= money

print(cnt)