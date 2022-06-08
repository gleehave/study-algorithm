def solution(people, limit):
    people = sorted(people)
    kg = 0
    answer = 1

    for person in people:
        if kg + person <= limit:
            kg += person
        else:
            answer += 1
            kg = person
    return answer


people = [70, 80, 50]
limit = 100
print(solution(people, limit))