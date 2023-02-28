import sys
input = sys.stdin.readline

size, count = map(int, input().split())
numList = [list(map(int, input().split())) for _ in range(size)]
sumList = [[0] * (size+1) for _ in range(size+1)]

for i in range(1, size + 1):
    for j in range(1, size + 1):
        sumList[i][j] = sumList[i][j-1] + sumList[i-1][j] - sumList[i-1][j-1] + numList[i-1][j-1]


for _ in range(count):
    x1, y1, x2, y2 = map(int, input().split())
    print(sumList[x2][y2] - sumList[x1-1][y2] - sumList[x2][y1-1] + sumList[x1-1][y1-1])