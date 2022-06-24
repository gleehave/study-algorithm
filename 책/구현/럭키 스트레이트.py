# 현재 캐릭터의 점수 N
# 특정조건: 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다.

# 현재 점수: 123,402
# 왼쪽 부분 자릿수의 합은 1+2+3 | 오른쪽 부분 자릿수의 합은 4 + 0 + 2 -> 럭키스트레이트 사용가능

# 럭키 스트레이트를 사용할 수 있다면 "LUCKY" 출력 | 사용할 수 없다면 "READY" 출력
# 단, N의 자릿수는 항상 짝수형태로 주어진다.

'''
N = int(input())
data = list(str(N))

for _ in range(len(data)):
    middle = len(data)//2
    left = sum(int(data[:middle]))
    right = sum(int(data[middle:]))

    if left == right:
        print("LUCKY")
    else:
        print("READY")
'''

n = input()
length = len(n)
result = 0

for i in range(length//2):
    result += int(n[i])

for i in range(length//2, length):
    result -= int(n[i])

if result == 0:
    print("LUCKY")
else:
    print("READY")