# 종이(1) 가로,세로 = 10 x 20
# 종이(2) 가로,세로 = 20 x 20

# 바닥의 공간은 N x 20 일때, 종이 2개로 바닥공간을 채울 수 있는 경우의 수

# 수식으로 풀어낸다!
# Dynamic Programming 으로 규칙성을 점화식으로 표현하고 계산해서 풀어낸다.

def function(N):
    if N % 10 == 0:
        if N==10:
            return 1
        elif N == 20:
            return 3
        else:
            return function(N-10)+(2*function(N-20))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    count = function(N)
    print("#{} {}".format(test_case, count))