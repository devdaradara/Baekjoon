import sys
input = sys.stdin.readline

s = int(input())
switches = list(map(int, input().split()))

def boys(n, switches):
    idx = n - 1
    while idx <= s - 1:
        if switches[idx]:
            switches[idx] = 0
        else:
            switches[idx] = 1
        idx += n

def girls(n, switches):
    if switches[n - 1]:
        switches[n - 1] = 0
    else:
        switches[n - 1] = 1
    left = n - 1 - 1
    right = n - 1 + 1
    while left >= 0 and right <= s - 1:
        if switches[left] == switches[right]:
            if switches[left]:
                switches[left] = 0
                switches[right] = 0
            else:
                switches[left] = 1
                switches[right] = 1
        else:
            break
        left -= 1
        right += 1

student = int(input())
for _ in range(student):
    sex, num = map(int, input().split())
    if sex == 1:
        boys(num, switches)
    else:
        girls(num, switches)

for i in range(s):
    if i % 20 == 0 and i != 0:
        print()
    print(switches[i], end=" ")
