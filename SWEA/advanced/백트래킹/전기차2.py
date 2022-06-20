# 충전지가 방전되기 전에 교체
# 최소한의 교체 횟수로 목적지에 도착한다.

# 정류장: 1 2 3 4 5
# 충전지: 2 3 1 1

# 1번에서 충전용량이 2 이므로, 3번 정류장까지 운행할 수 있다.
# 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.

def dfs(idx):
    global charge, result

    if idx >= len(lst):
        if result >= charge:
            result = charge
        return

    if result <= charge:
        return

    for i in range(idx + lst[idx], idx, -1):
        charge += 1
        dfs(i)
        charge -= 1

T = int(input())

for test_case in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    result = 987654321
    charge = 0
    dfs(1)

    print("#{} {}".format(test_case, result-1))