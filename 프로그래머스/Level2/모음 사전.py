# 'A', 'E', 'I', 'O', 'U' 만들 수 있는 길이 5 이하의 모든 단어가 있다.
# 'A', 'AA', ...... 'UUUUU' 이다.

# 단어 하나 word가 매개변수로 주어질 때,
# 이 단어가 사전에서 몇번째 단어인지 return 하라.

from itertools import product

def solution(word):
    words = []
    for i in range(1,6):
        for c in product(['A','E','I','O','U'], repeat=i):
            words.append(''.join(list(c)))
    words.sort()

    return words.index(word) + 1

print(solution('AAAAE'))