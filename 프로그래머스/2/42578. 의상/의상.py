from collections import defaultdict

def solution(clothes):
    arr = defaultdict(int)
    
    for c in clothes:
        arr[c[1]] += 1
              
    answer = 1
    
    for i in list(arr.values()):
        answer *= (i + 1)
    
    return answer - 1