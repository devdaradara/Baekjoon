import sys

number, count = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))

sumsList = [0]
sums = 0

for i in numList:
    sums += i
    sumsList.append(sums)

for _ in range(count):
    start, end = map(int, sys.stdin.readline().split())
    print(sumsList[end] - sumsList[start - 1])