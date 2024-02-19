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
    for idx in range(n):
        answer.append(nums[idx])
        check()
        answer.pop()


check()