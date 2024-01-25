import sys
input = sys.stdin.readline

n = int(input())
string = input().rstrip()

len = n // 5
signal = ["" for _ in range(len)]

for i in range(n):
    signal[i % len] += string[i]

answer = ""
width = [3, 1, 4, 3, 3, 4, 3, 3, 3, 3]
idx = 0

while idx < len:
    crt = signal[idx]

    if crt == ".....":
        idx += 1

    # 0, 1, 6, 8
    elif crt == "#####":
        if idx == len - 1 or signal[idx + 1] == ".....":
            answer += "1"
            idx += width[1]
        elif signal[idx + 1] == "#...#":
            answer += "0"
            idx += width[0]
        else:
            new = signal[idx + 2]
            if new == "#.###":
                answer += "6"
                idx += width[6]
            else:
                answer += "8"
                idx += width[8]
    # 2
    elif crt == "#.###":
        answer += "2"
        idx += width[2]

    # 3
    elif crt == "#.#.#":
        answer += "3"
        idx += width[3]

    # 4
    elif crt == "###..":
        answer += "4"
        idx += width[4]

    # 7
    elif crt == "#....":
        answer += "7"
        idx += width[7]

    # 5, 9
    else:
        new = signal[idx + 2]
        if new == "#.###":
            answer += "5"
            idx += width[5]
        else:
            answer += "9"
            idx += width[9]

print(answer)