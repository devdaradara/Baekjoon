def solution(s):
    answer = True
    
    stack = []
    
    for ss in s:
        if ss == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                answer = False        
                break
            if stack.pop() != "(":
                answer = False        
                break
                
    if stack:
        answer = False
        
    return answer