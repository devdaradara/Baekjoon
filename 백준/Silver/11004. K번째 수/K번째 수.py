import sys

cnt, ord = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
print(num[ord-1])