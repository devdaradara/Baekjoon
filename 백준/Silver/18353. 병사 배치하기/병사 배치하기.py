import sys
input = sys.stdin.readline

n = int(input())
fights = list(map(int, input().split()))
fights.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if fights[i] > fights[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))