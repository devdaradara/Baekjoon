hasNumber = int(input())
hasCard = list(map(int, input().split()))
hasCard.sort()
isNumber = int(input())
isCard = list(map(int, input().split()))

for i in range(len(isCard)):
    startPoint = 0
    endPoint = len(hasCard) - 1
    isFind = False
    while (startPoint <= endPoint):
        midPoint = (startPoint + endPoint) // 2
        if (isCard[i] == hasCard[midPoint]):
            isFind = True
            break

        elif (isCard[i] < hasCard[midPoint]):
            endPoint = midPoint - 1

        elif (isCard[i] > hasCard[midPoint]):
            startPoint = midPoint + 1

    if (isFind): print("1", end=" ")
    else: print("0", end=" ")
