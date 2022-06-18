# 0 보다 크고, 1 미만인 십진수 N을 이진수로 바꾸려 한다.
# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
# 13 자리 이상이 필요한 경우에는 'overflow'를 출력한다.

# -1 ~ -13 까지 반복
# N을 2^power로 나눈 몫을 result에 추가
# 나머지를 N으로 갱신
# N == 0이면 변환 완료

for tc in range(1, int(input())+1):
    N = float(input())
    result = ''

    for power in range(-1, -14, -1):
        result += str(int(N//(2**power)))
        N %= (2**power)
        if N == 0:
            break
    else: # 반복문이 강제 종료 되지 않았다면, 13자리 이상 이진변환이 필요함.
        result = 'overflow'

    print("#{} {}".format(tc, result))