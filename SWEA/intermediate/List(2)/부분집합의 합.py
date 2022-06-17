# 1~12까지 숫자를 원소로 가진 집합 A
# N: 부분집합의 원소의 개수
# K: 원소의 합

from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    A = [i for i in range(1,13)]
    N, K = map(int, input().split())
    count = 0

    SUBSET = combinations(A, N)

    for SET in SUBSET:
        if sum(SET) == K:
            count += 1
        continue

    print("#{} {}".format(test_case, count))
