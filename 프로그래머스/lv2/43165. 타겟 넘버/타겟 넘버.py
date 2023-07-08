
def solution(numbers, target):
    leaves = [0]
    answer = 0 

    for num in numbers : 
        temp = []
	
        for leaf in leaves : 
            temp.append(leaf + num)
            temp.append(leaf - num)

        leaves = temp 

    for leaf in leaves : 
        if leaf == target : 
            answer += 1

    return answer


# import math

# def solution(numbers, target):
#     answer = 0

#     all_number = [numbers[0]]
#     all_cnt = len(numbers)

#     for i in range(all_cnt):
#         num = numbers[i]

#         for j in range(int(math.pow(2, i)) - 1, int(math.pow(2, i + 1)) - 2):
#             all_number.append(numbers[j] + num)
#             all_number.append(numbers[j] - num)

#     for k in range(int(math.pow(2, all_cnt)) - 1, len(all_number)):
#         if all_number[k] == target:
#             answer += 1

#     return answer
