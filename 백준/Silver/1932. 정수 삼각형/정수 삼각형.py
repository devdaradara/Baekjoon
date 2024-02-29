import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            left = 0
        else:
            left = triangle[i-1][j-1]

        if j == i:
            right = 0
        else:
            right = triangle[i-1][j]
        triangle[i][j] += max(left, right)

print(max(triangle[n-1]))