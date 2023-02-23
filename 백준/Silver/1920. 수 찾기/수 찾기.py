haveNum = int(input())
haveNumbers = list(map(int, input().split()))
haveNumbers.sort()
isNum = int(input())
isNumbers = list(map(int, input().split()))

for number in isNumbers:
    leftPoint = 0
    rightPoint = len(haveNumbers) - 1
    while True:
        midPoint = (leftPoint + rightPoint) // 2

        if leftPoint > rightPoint:
            print(0)
            break

        elif number < haveNumbers[midPoint]:
            rightPoint = midPoint - 1

        elif number > haveNumbers[midPoint]:
            leftPoint = midPoint + 1

        elif number == haveNumbers[midPoint]:
            print(1)
            break
