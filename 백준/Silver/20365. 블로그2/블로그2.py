import sys

N = int(sys.stdin.readline())
datas = sys.stdin.readline().rstrip()

def solution(datas):
    rDatas = [v for v in datas.split("B") if v]
    bDatas = [v for v in datas.split("R") if v]

    answer = min(len(rDatas) + 1, len(bDatas) + 1)

    return answer


print(solution(datas))