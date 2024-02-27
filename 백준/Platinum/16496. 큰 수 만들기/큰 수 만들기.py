import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(str, input().split()))

nums.sort(key=lambda x: x * 10, reverse=True)

print(str(int("".join(nums))))