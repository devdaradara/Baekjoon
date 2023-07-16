def solution(citations):
    answer = min(citations)
    
    citations.sort()
    citations.insert(0, answer)
    candi = []
    
    index_h = 0
    
    for i in range(max(citations)):
        citations[index_h] += 1
        
        for j in citations[1:]:
            if citations[index_h] >= j: citations[index_h] += 1
            else: break
            
        if (len(citations) - index_h) >= citations[index_h]:    
            candi.append(citations[index_h])
        else:
            break
    
    answer = max(candi) - 1
    
    return answer

# 0, 1, 1, 3, 5, 6