import sys
input = sys.stdin.readline

sound = list(input().rstrip())
duck = []
dept = False

for s in sound:
    if s == "q":
        one = True
        for i in range(len(duck)):
            if len(duck[i]) == 5:
                duck[i] = ["q"]
                one = False
                break
        if one:
            one = True
            duck.append(["q"])

    elif s == "u":
        for i in range(len(duck)):
            if len(duck[i]) == 1:
                duck[i].append("u")
                dept = False
                break
            else:
                dept = True

    elif s == "a":
        for i in range(len(duck)):
            if len(duck[i]) == 2:
                duck[i].append("a")
                dept = False
                break
            else:
                dept = True

    elif s == "c":
        for i in range(len(duck)):
            if len(duck[i]) == 3:
                duck[i].append("c")
                dept = False
                break
            else:
                dept = True

    elif s == "k":
        for i in range(len(duck)):
            if len(duck[i]) == 4:
                duck[i].append("k")
                dept = False
                break
            else:
                dept = True
    if dept:
        break

cnt = 0
for d in duck:
    if len(d) == 5:
        cnt += 1
    else:
        dept = True
        break
        
if sound[0] != "q":
    dept = True

if cnt == 0 or dept:
    print("-1")
else:
    print(cnt)