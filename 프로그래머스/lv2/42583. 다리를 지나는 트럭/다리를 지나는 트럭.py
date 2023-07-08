def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    weight_sum = 0

    while bridge:

        answer += 1
        weight_sum = weight_sum - bridge[0]
        bridge.pop(0)

        if truck_weights:

            # if sum(bridge) + truck_weights[0] <= weight:            
            if weight_sum + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                weight_sum = weight_sum + t
                bridge.append(t)

            else:
                bridge.append(0)

    return answer
