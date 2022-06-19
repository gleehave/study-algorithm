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