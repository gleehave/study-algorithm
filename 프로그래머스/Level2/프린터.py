# 중요도가 높은 문서를 먼저 인쇄하는 프린터를 원한다.

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# (a, b, c, d) 가 있다.
# (2, 1, 3, 2) 의 중요도를 갖는다.
# ->  c, d, a, b 순서로 인쇄해야한다. (결과)

# 내가 인쇄를 요청한 문서가 몇번째로 인쇄되는가?

            # 0, 1, 2, 3
priorities = [2, 1, 3, 2]
location = 2

from collections import deque

def solution(priorities, location):
    answer = 0
    papers = deque([(data, index) for index, data in enumerate(priorities)])

    while papers:
        temp = papers.popleft()
        if papers and max(papers)[0] > temp[0]:
            papers.append(temp)
        else:
            answer += 1
            if temp[1] == location:
                break

    return answer

print(solution(priorities, location))