import sys
input = sys.stdin.readline

number = int(input())
goal = int(input())
material = list(map(int, input().split()))

material.sort()
start = 0
end = len(material) - 1
count = 0

while end > start:
    sum = material[start] + material[end]
    if sum < goal:
        start += 1

    elif sum > goal:
        end -= 1

    else:
        count += 1
        end -= 1
        start += 1

print(count)