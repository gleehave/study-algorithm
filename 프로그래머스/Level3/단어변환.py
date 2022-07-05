# 1. 한 번에 1개의 알파벳만 바꿀 수 있다.
# 2. words에 있는 단어로만 변환할 수 있다.

# begin: "hit"
# target: "cog"
# words:  ["hot","dot","dog","lot","log","cog"]
# hit -> hot -> dot -> dob -> cog 총 4번
# 변환할 수 없다면 0을 반환한다.

from collections import deque

begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

def solution(begin, target, words):
    answer = 0
    N = len(words)
    q = deque()
    q.append([begin, 0])
    visited = [False] * N

    while q:
        word, count = q.popleft()
        if word == target:
            answer = count
            break
        for index in range(N):
            temp = 0
            if visited[index] == False:
                for j in range(len(word)):
                    if word[j] != words[index][j]:
                        temp += 1
                if temp == 1:
                    q.append([words[index], count+1])
                    visited[index] = True
    return answer

print(solution(begin, target, words))