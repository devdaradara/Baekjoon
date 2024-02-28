import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())
answer = []


def find_exp(pl, mi, mu, di, idx, num):
    if idx == n:
        answer.append(num)
    if pl > 0:
        find_exp(pl-1, mi, mu, di, idx+1, num+nums[idx])

    if mi > 0:
        find_exp(pl, mi-1, mu, di, idx + 1, num-nums[idx])

    if mu > 0:
        find_exp(pl, mi, mu-1, di, idx + 1, num*nums[idx])

    if di > 0:
        find_exp(pl, mi, mu, di-1, idx + 1, int(num/nums[idx]))


find_exp(plus, minus, multiple, divide, 1, nums[0])
print(max(answer))
print(min(answer))