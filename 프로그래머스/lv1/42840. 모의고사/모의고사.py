def solution(answers):
    answer = [0, 0, 0]
    humans = []

    first_answer = [1, 2, 3, 4, 5]
    second_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    third_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx in range(len(answers)):
        if answers[idx] == first_answer[idx % 5]:
            answer[0] += 1

        if answers[idx] == second_answer[idx % 8]:
            answer[1] += 1

        if answers[idx] == third_answer[idx % 10]:
            answer[2] += 1

    high_score = max(answer)
    add = 1

    for i in range(answer.count(high_score)):
        humans.append(answer.index(high_score)+add)
        answer.remove(high_score)
        add += 1

    return humans