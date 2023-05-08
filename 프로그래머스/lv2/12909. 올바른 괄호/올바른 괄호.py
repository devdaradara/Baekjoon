
def solution(s):
    answer = True
    bracket = []

    for i in s:
        if i == "(":
            bracket.append("(")
        else: # i == ")"
            length = len(bracket)
            if length == 0 or bracket[length - 1] == ")":
                return False
            else:
                bracket.pop()
    if len(bracket) != 0: answer = False
    return answer

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
