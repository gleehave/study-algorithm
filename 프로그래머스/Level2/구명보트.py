from collections import deque


def solution(people, limit):
    boat = 0
    people.sort()

    q = deque(people)
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop() # 무거운 사람을 보트에 태움.
                q.popleft() # 가벼운 사람 보트에 태움.
                boat += 1
            elif q[0] + q[-1] > limit:
                q.pop() # 무거운 사람을 보트에 태움.
                boat += 1
        else:
            if q[0] <= limit:
                q.pop()
                boat += 1
    return boat


# 구명보트는 한 번에 최대 2명밖에 태울 수 없다. <- 제대로 요구사항 읽을것....
# 무게제한도 존재한다.

# 오름차순 정렬
# deque 자료구조로 양쪽에서 무게를 더함
#

people = [70, 80, 50]
limit = 100
print(solution(people, limit))