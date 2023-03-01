import sys
input = sys.stdin.readline

num = int(input())
start, end = 1, 1
part_sum = 1
result = 1

while end != num:
    if part_sum == num:
        result += 1
        end += 1
        part_sum += end

    elif part_sum < num:
        end += 1
        part_sum += end

    else:
        part_sum -= start
        start += 1

print(result)