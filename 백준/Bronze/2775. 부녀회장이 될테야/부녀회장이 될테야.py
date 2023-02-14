testCase = int(input())

peoples = []

firstFloor = list(i for i in range(1, 15))
peoples.append(firstFloor)

for i in range(14):
    tmp = []
    for j in range(15):
        tmp.append(sum(peoples[i][0:j + 1]))
    peoples.append(tmp)

for _ in range(testCase):
    floor = int(input())
    room = int(input())

    print(peoples[floor][room - 1])
