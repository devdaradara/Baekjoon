def solution(clothes):
    answer = 1
    clothes_type = {}

    for i in clothes:
        if i[1] in clothes_type.keys():
            clothes_type[i[1]] = int(clothes_type.get(i[1])) + 1
        else:
            clothes_type[i[1]] = "1"

    for j in clothes_type.keys():
        answer *= int(clothes_type.get(j)) + 1

    answer -= 1

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
