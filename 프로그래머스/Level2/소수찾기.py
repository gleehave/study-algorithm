# 흩어진 종이 조각을 붙여 소수를 몇개를 만들 수 있는지 알고 싶다.
# 각 종이 조각에 적힌 문자열 numbers가 주어진다.
# 종이조각으로 만들 수 있는 소수가 몇개인가?

numbers = "17"
# [7, 17, 71] 총 3개

# 2, 4, 6, 8, 10, 12, 14, 16, 18
# 3, 6, 9, 12, 15, 18
# 5, 10, 15, 20
# 6, 12, 18, 24, 30

from itertools import permutations

def solution(numbers):
    answer = []
    per = []
    nums = [n for n in numbers]
    for i in range(1, len(numbers) + 1):
        per += list(permutations(nums, i))
    new_nums = [int(("").join(p)) for p in per]

    for n in new_nums:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                check = False
                break

        if check:
            answer.append(n)

    return len(set(answer))


print(solution(numbers))