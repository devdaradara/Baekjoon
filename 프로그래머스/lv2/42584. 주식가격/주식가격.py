def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]: cnt += 1
            else: break
        answer.append(cnt)

    return answer


# def solution(prices):
#     answer = []
    
#     for i in range(len(prices)):
#         cri = prices[i]
#         new_prices = prices[i:]
#         cnt = -1
        
#         for price in new_prices:
#             cnt += 1
#             if price < cri: break
            
#         answer.append(cnt)
        
#     return answer