# 자연수 n을 이진법으로 변환한다. (format(, 'b'))? bin(n)?
# 1의 개수는 k 이다.
# n보다 작은 자연수 중 이진법으로 변환하여 1의 개수가 k인 수가 몇개인가?

# 만약 1111 로 모든 비트의 자리에 1이 들어올 경우, 같은 k의 값은 없다.
# 만약 1110 일때, k=3 -> 0111, 1011, 1101 3가지밖에 없다.
# 만약 1001 일때, k=2 -> 0011, 0101, 0110, 1100 4가지 있는데, 1100은 1001보다 크므로 제외


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

print(solution(44444444444444444))