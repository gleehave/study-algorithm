# 자연수 n이 주어졌을 때,

# 1. 'n의 다음 큰 숫자'는 n보다 큰 자연수!!
# 2. 'n의 다음 큰 숫자'와 n은 2진수로 변환했을 때, 1의 개수가 같다.
# 3. 'n의 다음 큰 숫자'는 조건1과 조건2를 만족하는 가장 작은 수

n=78
# 78 = 1001110 -> 83 = 1010011
# result 83

def solution(n):
    answer = 0
    one_count = bin(n).count('1')

    for num in range(n+1,  100000000001):
        num_one_count = bin(num).count('1')

        if one_count == num_one_count:
            answer = num
            break

    return answer
