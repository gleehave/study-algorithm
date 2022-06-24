# 0~9 까지 이루어진 문자열 S가 주어진다.
# 왼쪽부터 오른쪽으로 1개씩 모든 숫자를 확인한다.
# 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구한다.
# 단, +연산 보다 x를 먼저 계산하는 일반 방식이 아니라, 모두 왼쪽부터 순서대로 이뤄진다.

# 02984
# (0+2)x9x8x4 = 576

# 567
# 5x6x7 = 210

S = input()
result = int(S[0])

for index in range(1, len(S)):
    temp = int(S[index])
    if temp <= 1 or result <= 1:
        result = result + temp
    else:
        result = result * temp

print(result)
