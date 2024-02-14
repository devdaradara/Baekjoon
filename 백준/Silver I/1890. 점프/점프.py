import sys
input = sys.stdin.readline

n = int(input())
moves = [list(map(int, input().split())) for _ in range(n)]
ways = [[0] * n for _ in range(n)]
ways[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(ways[i][j])
            break
        if i + moves[i][j] < n:
            ways[i + moves[i][j]][j] += ways[i][j]
        if j + moves[i][j] < n:
            ways[i][j + moves[i][j]] += ways[i][j]
