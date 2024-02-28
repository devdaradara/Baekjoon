import sys
input = sys.stdin.readline

n = input().rstrip()
first = n[:len(n) // 2]
second = n[len(n) // 2:]


left = 0
right = 0
for i in range(len(n) // 2):
    left += int(first[i])
    right += int(second[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
