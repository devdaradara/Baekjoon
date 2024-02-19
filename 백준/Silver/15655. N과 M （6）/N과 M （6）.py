import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []


def check(start):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for idx in range(start, n):
        if nums[idx] not in answer:
            answer.append(nums[idx])
            check(idx+1)
            answer.pop()


check(0)