import sys
input = sys.stdin.readline

number_cnt, sum_cnt = map(int, input().split())

numbers = list(map(int, input().split()))

sum_list = [0]
temp = 0

for i in numbers:
    temp += i
    sum_list.append(temp)

for _ in range(sum_cnt):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start-1])