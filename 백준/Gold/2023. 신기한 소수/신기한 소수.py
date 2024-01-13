import sys
input = sys.stdin.readline

digit = int(input())
num = [[], [2, 3, 5, 7]]

def dfs(d):
    num.append([])
    for first in num[d]:
        for plus in range(1, 10, 2):
            new = first * 10 + plus
            if isPrime(new):
                num[d+1].append(new)


def isPrime(n):
    for i in range(2, int(n / 2 + 1)):
        if n % i == 0:
            return False
    return True



for d in range(1, digit+1):
    dfs(d)

for i in num[digit]:
    print(i)