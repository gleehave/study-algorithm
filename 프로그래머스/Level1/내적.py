# 길이가 같은 두 1차원 정수 배열 a, b가 주어진다.
# a와 b의 내적을 return 해라.

# n은 a, b의 길이
# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다.

a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]
# return 3

def solution(a, b):
    N = len(a)

    result = 0
    for index in range(N):
        result += a[index] * b[index]

    return result

print(solution(a,b))