import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
total = int(input())

nums.sort()
start = 0
end = max(nums)
result = 0

while start <= end:
    mid = (start + end) // 2

    now = 0
    for num in nums:
        if num >= mid:
            now += mid
        else:
            now += num

    if now <= total:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(end)