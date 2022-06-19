# N개의 컨테이너를 M대의 트럭으로
# A에서 B 도시로 운반한다.
# 트럭당 1개의 컨테이너를 운반한다.
# 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# 최대 M대의 트럭이 편도로 1번만 운반한다.

# N, M이 주어진다.
# 화물 무게 w, 적재용량 t
# N,M = 3 2
# Ws =  1 5 3
# Ts =  8 3

# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     Ws = list(map(int, input().split()))
#     Ts = list(map(int, input().split()))
#     Ws = sorted(Ws, reverse=True)
#     Ts = sorted(Ts, reverse=True)
#
#     WTs = zip(Ws, Ts)
#     result = []
#     for wt in WTs:
#         if wt[0] > wt[1]:
#             continue
#         else:
#             result.append(wt)
#     sum = 0
#     for _ in range(len(result)):
#         sum += result[_][0]
#     print("#{} {}".format(test_case, sum))

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Ws = list(map(int, input().split()))
    Ts = list(map(int, input().split()))

    Ws = sorted(Ws, reverse=True)
    Ts = sorted(Ts, reverse=True)

    answer = 0
    left = 0
    for truck in Ts:
        while left < N and truck < Ws[left]:
            left += 1
        if left == N:
            break
        answer += Ws[left]
        left += 1

    print("#{} {}".format(test_case, answer))