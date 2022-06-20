# N종의 제품을 N곳의 공장에서
# 1곳당 1가지씩 생산하려한다.

#     A    B    C
# 1   73   21   21
# 2   11   59   40
# 3   24   31   83

# 1-C, 2-A, 3-B로 생산하면 63으로 최소가 된다.

def dfs(product):
    global total, sum

    if product == N:
        if total > sum:
            total = sum
        return

    if total <= sum:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            sum += lst[product][i]
            dfs(product+1)
            visited[i] = 0
            sum -= lst[product][i]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sum = 0
    total = 987654321

    dfs(0)
    print("#{} {}".format(test_case, total))