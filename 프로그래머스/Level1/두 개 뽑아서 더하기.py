# 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해서
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아라.
from itertools import combinations

def solution1(numbers):
    answer = []
    for i in range(len(numbers)): # 0 ~ n-1
        for j in range(i+1, len(numbers)): # i ~ n-1
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))

    return sorted(answer)

def solution2(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)


numbers = [2,1,3,4,1]
print(solution2(numbers))