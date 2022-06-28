# 중앙은 노란색, 테두리는 갈색인 카펫이 있다.
# 전체 크기를 모른다.(n x m)

# 갈색의 개수: brown
# 노란색의 개수: yellow
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하라.

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for b in range(1, total+1):
        if (total / b) % 1 == 0:
            a = total / b
            if a >= b:
                if 2*a + 2*b == brown + 4:
                    return [a, b]
    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))