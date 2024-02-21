import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0

for i in range(n):
    start = 0
    end = n - 1
    goal = nums[i]
    while start < end:
        if nums[start] + nums[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif nums[start] + nums[end] < goal:
            start += 1
        elif nums[start] + nums[end] > goal:
            end -= 1

print(cnt)