import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []


def check():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    prev = 0
    for idx in range(n):
        if prev != nums[idx]:
            answer.append(nums[idx])
            prev = nums[idx]
            check()
            answer.pop()


check()