# 자연수 n을 이진법으로 변환한다. (format(, 'b'))? bin(n)?
# 1의 개수는 k 이다.
# n보다 작은 자연수 중 이진법으로 변환하여 1의 개수가 k인 수가 몇개인가?

def solution(n):
    binary_n = bin(n)[2:]
    k = binary_n.count('1')

    binary_one = '1' * k

    minimum = int('0b'+binary_one,2)
    maximum = int('0b'+binary_one+'0',2)

    count = 0
    for i in range(minimum, maximum+1):
        binary_i = bin(i)[2:]
        temp_k = binary_i.count('1')
        if k == temp_k:
            count += 1
    return count

print(solution(9))