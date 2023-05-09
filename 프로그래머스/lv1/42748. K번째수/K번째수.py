def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        command = commands[i]
        # i = command[0]
        newArr = array[command[0]-1:command[1]]
        newArr.sort()
        answer.append(newArr[command[2]-1])

    return answer
