def solution(nums):
    to_set = len(set(nums))  
    answer = min(to_set, len(nums) // 2)
    return answer