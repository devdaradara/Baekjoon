import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(i):
        power = max(dp[j], (i - j) * (1 + abs(nums[i] - nums[j])))
        dp[i] = min(dp[i], power)

if dp[-1] <= k:
    print("YES")
else:
    print("NO")
