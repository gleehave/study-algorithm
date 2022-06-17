# 16진수 1자리는 2진수 4자리로 표시된다.
# N자리 16진수가 주어지면,
# 각 자리 수를 4자리 2진수로 표시해라.
# 단, 2진수의 앞자리 0도 반드시 출력한다.

# 47FE
#0100 0111 1111 1110

T = int(input())
for test_case in range(1, T + 1):
    N, HEX = input().split()
    INT = int('0x'+HEX, 16)
    CONVERT = format(INT,'b')
    if len(CONVERT) < int(N)*4:
        CONVERT = '0'+CONVERT
    print("#{} {}".format(test_case, CONVERT))