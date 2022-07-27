# 양의 정수 x에 대한 함수가 있다.
    # x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        index = ''.join(bin_number).rfind('0')
        bin_number[index] = '1'

        if number % 2 == 1:
            bin_number[index+1] = '0'

        answer.append(int(''.join(bin_number), 2))

    return answer