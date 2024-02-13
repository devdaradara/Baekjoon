import sys
input = sys.stdin.readline

n = int(input())
stocks = list(map(int, input().split()))

# stock = 0, money = n
def BNP(money):
    stock = 0
    for s in stocks:
        if money // s >= 0:
            stock += money // s
            now = money // s
            money -= now * s
    return stock, money

def TIMING(money):
    stock = 0
    up = 0
    down = 0
    prev = 0
    for s in stocks:
        if s > prev:
            up += 1
            down = 0
        elif s < prev:
            down += 1
            up = 0
        if down >= 3:
            stock += money // s
            now = money // s
            money -= now * s
        elif up >= 3:
            money += stock * s
            stock = 0
        prev = s
    return stock, money

joon_s, joon_m = BNP(n)
joon_total = joon_s * stocks[-1] + joon_m
sung_s, sung_m = TIMING(n)
sung_total = sung_s * stocks[-1] + sung_m

if joon_total > sung_total:
    print("BNP")
elif joon_total < sung_total:
    print("TIMING")
else:
    print("SAMESAME")