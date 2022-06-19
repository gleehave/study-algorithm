# l, m, r
# A는 정렬되어있고, B는 정수가 담긴 리스트이다.
# B에 속한 어떤 수가 A에 들어있으면서,
# 동시에 탐색과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수를 알고싶다.

# A: [1,2,3,4,5,6,7,8,9,10]
# 6은 번갈아 가면서 탐색한다.
# 5는 조건에 부합한다.
# 10은 오른쪽 - 오른쪽을 탐색하므로 조건에 맞지않는다.

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    N1 = sorted(list(map(int, input().split())))
    M1 = list(map(int, input().split()))

    count = 0
    for num in M1:
        start = 0
        end = N-1

        signal = 0
        while start <= end:
            mid = (start + end) // 2

            if num >= N1[mid]:
                if num == N1[mid]:
                    count += 1
                    break
                start = mid + 1
                if signal == 1:
                    break
                signal = 1
            elif num < N1[mid]:
                end = mid - 1
                if signal == -1:
                    break
                signal = -1

    print("#{} {}".format(test_case, count))