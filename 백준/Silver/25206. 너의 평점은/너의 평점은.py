import sys
input = sys.stdin.readline

grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade_score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0

for _ in range(20) :
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade != "P":
        total += credit
        result += credit * grade_score[grades.index(grade)]

print('%.6f' % (result / total))