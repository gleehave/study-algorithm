# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5,                     1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,            2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,      3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1, 2, 3번 학생 중 가장 많은 문제를 맞힌 사람을 return 하라.

answer = [1,2,3,4,5]
# result: [1]

def solution(answers):
    counts = []
    students = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for student in students:
        index = 0
        count = 0
        for correct in answers:
            if index > len(student)-1:
                index = 0
            if correct == student[index]:
                count += 1
            index += 1
        counts.append(count)

    result = []
    max_value = max(counts)
    if max_value == counts[0]:
        result.append(1)
    if max_value == counts[1]:
        result.append(2)
    if max_value == counts[2]:
        result.append(3)

    return result


print(solution(answer))