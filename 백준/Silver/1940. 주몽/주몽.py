import sys
input = sys.stdin.readline

material = int(input())
armor = int(input())
nums = list(map(int, input().split()))

cnt = 0

nums.sort()
first = 0
last = len(nums)-1

while first < last:
    sumNum = nums[first] + nums[last]
    if sumNum > armor: last -= 1
    if sumNum < armor: first += 1
    if sumNum == armor:
        cnt += 1
        last -= 1
        first += 1


print(cnt)