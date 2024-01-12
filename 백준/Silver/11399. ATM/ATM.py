import sys
input = sys.stdin.readline

people = int(input())
times = list(map(int, input().split()))

times.sort()

total = [0]

for i in range(people):
    total.append(total[i] + times[i])

print(sum(total))
