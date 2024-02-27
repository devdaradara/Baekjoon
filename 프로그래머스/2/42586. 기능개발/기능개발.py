def solution(progresses, speeds):
    have_to = []
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            have_to.append((100 - progresses[i]) // speeds[i])
        else:
            have_to.append((100 - progresses[i]) // speeds[i] + 1)
            
    answer = []
    
    tmp = 1
    for i in range(1, len(have_to)):
        if have_to[i] <= have_to[i-1]:
            tmp += 1
            have_to[i] = have_to[i-1]
        else:
            answer.append(tmp)
            tmp = 1
            
    answer.append(tmp)
    
    return answer