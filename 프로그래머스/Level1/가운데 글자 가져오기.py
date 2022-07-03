# 단어 s의 가운데 글자를 반환하는 함수
# 단어의 길이가 짝수라면 가운데 2글자를 반환

def solution(s):
    if len(s) % 2 != 0:
        center = len(s) // 2
        return s[center]
    else:
        center = len(s)//2
        return s[center-1:center+1]

s = 'qwer'
print(solution(s))