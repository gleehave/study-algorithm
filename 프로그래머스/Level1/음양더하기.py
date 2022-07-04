# 정수들의 절대값을 차례대로 담은 정수 배열 absolutes
# 이 정수들의 부호를 담은 boolean 배열의 signs가 있다.
# 실제 정수들의 합을 구하여 return 하라.


absolutes = [4, 7, 12]
signs = [True, False, True]

def solution(absolutes, signs):
    sign = {
        True: 1,
        False: -1
    }

    answer = 0
    for value in zip(absolutes, signs):
        answer += value[0]*sign[value[1]]

    return answer

print(solution(absolutes, signs))