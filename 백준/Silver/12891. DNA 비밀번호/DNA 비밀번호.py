import sys

input = sys.stdin.readline

dnaLength, passLength = map(int, input().split())
dna = str(input())
aGoal, cGoal, gGoal, tGoal = map(int, input().split())

aCnt, cCnt, gCnt, tCnt = 0, 0, 0, 0
cnt = 0
firstLetter = dna[0]
lastLetter = dna[passLength - 1]

passWord = False

for i in range(passLength):

    if dna[i] == "A": aCnt += 1
    if dna[i] == "C": cCnt += 1
    if dna[i] == "G": gCnt += 1
    if dna[i] == "T": tCnt += 1

if aCnt >= aGoal and cCnt >= cGoal and gCnt >= gGoal and tCnt >= tGoal:
    passWord = True

if passWord:
    cnt += 1


for i in range(1, dnaLength - passLength + 1):
    passWord = False

    if firstLetter == "A": aCnt -= 1
    if firstLetter == "C": cCnt -= 1
    if firstLetter == "G": gCnt -= 1
    if firstLetter == "T": tCnt -= 1
    firstLetter = dna[i]

    lastLetter = dna[i + passLength - 1]
    if lastLetter == "A": aCnt += 1
    if lastLetter == "C": cCnt += 1
    if lastLetter == "G": gCnt += 1
    if lastLetter == "T": tCnt += 1

    if aCnt >= aGoal and cCnt >= cGoal and gCnt >= gGoal and tCnt >= tGoal:
        passWord = True

    if passWord: cnt += 1


print(cnt)
