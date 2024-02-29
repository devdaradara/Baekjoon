import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)
answer = 0

for i in range(n - 1, -1, -1):
    if table[i][0] + i <= n:
        dp[i] = max(table[i][1] + dp[table[i][0] + i], answer)
        answer = dp[i]
    else:
        dp[i] = answer

print(answer)