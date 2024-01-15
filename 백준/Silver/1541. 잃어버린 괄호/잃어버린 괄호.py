import sys
input = sys.stdin.readline

mathEx = input().rstrip()

nums = []
exp = []

tmp = ""
for i in mathEx:
    if i == "+":
        nums.append(int(tmp))
        tmp = ""
        exp.append("+")
    elif i == "-":
        nums.append(int(tmp))
        tmp = ""
        exp.append("-")
    else:
        tmp += i
nums.append(int(tmp))

total = nums[0]
minusSum = 0
haveMinus = False

for i in range(len(exp)):
    if exp[i] == "-":
        if haveMinus:
            total -= minusSum
            minusSum = 0
            haveMinus = False
        else:
            haveMinus = True
        if minusSum == 0:
            haveMinus = True

    if haveMinus:
        minusSum += nums[i+1]
    else:
        if exp[i] == "-":
            total -= nums[i+1]
        else:
            total += nums[i+1]

if minusSum > 0:
    total -= minusSum

print(total)