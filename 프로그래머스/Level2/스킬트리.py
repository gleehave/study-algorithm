def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        result = ""
        for value in tree:
            if value in skill:
                result += value

        if skill[:len(result)] == result:
            answer += 1
    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))