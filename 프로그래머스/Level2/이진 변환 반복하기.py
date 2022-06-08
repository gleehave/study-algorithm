# 0과 1로 이루어진 문자열 x
# x의 모든 0을 제거
# x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꾼다.

# x='0111010' 일때, '0111010' ->'1111' c=4 -> '100'
# '1'이 될 때까지의 이진변환 횟수 , 제거된 모든 0의 개수를 알고싶다.

def solution(s):
    # 이진변환 횟수, 제거된 0의 개수
    answer = [0, 0]

    cnt, zero = 0, 0
    while True:
        if s == '1':
            break
        else:
            zero += s.count('0')
            s = format(len(s.replace('0','')),'b')
            cnt += 1

    answer[0] = cnt
    answer[1] = zero

    return answer


