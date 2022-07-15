# 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면, h의 최댓값이 h-index이다.

citations = [3, 0, 6, 1, 5]
# return 3

def solution(citations):
    papers = len(citations)
    citations = sorted(citations, reverse=True)

    # 6, 5, 3, 1, 0
    for index, citation in enumerate(citations):
        if index >= citation:
            return index
    return len(citations)

print(solution(citations))