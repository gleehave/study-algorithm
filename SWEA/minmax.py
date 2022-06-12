# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력

# T (1<= T <= 50): 케이스의 개수
# N (5<= N <= 1000)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    case =  list(map(int, input().split()))
    print("#{} {}".format(test_case, max(case) - min(case)))
