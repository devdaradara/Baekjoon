from collections import deque

def solution(bridge_length, weight, truck_weights):
    que = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    answer = 0
    weights = 0
    
    while truck_weights:
        weights -= que.popleft()
        
        if weights + truck_weights[0] <= weight:
            que.append(truck_weights[0])
            weights += truck_weights[0]
            truck_weights.popleft()
        else: 
            que.append(0)
        answer += 1    
    
    return answer + bridge_length