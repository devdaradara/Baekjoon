def solution(arr):
    answer = []
    answer.append(arr[0])
    point = 0
    
    for i in arr:
        if answer[point] != i:
            answer.append(i)
            point += 1
        
    return answer