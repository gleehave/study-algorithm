# 사무실 출발 -> 관리구역 -> 사무실 복귀
# 각 구역을 1번씩만 방문하고 돌아올때, 최소 배터리 사용량을 구하자

# 0 18 34
# 48 0 55
# 18 7 0

T = int(input())

def dfs(current, tmp):
    global res
    if tmp < res:
        if 0 not in visited[1:]:
            res = min(res, tmp + a[current][0])
            return
        for next in range(1, N):
            if a[current][next] != 0 and visited[next] == 0:
                visited[next] = 1
                dfs(next, tmp+a[current][next])
                visited[next] = 0

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    res = 10000
    for i in range(1,N):
        visited = [0] * N
        visited[i] = 1
        dfs(i, a[0][i])
    print("#{} {}".format(tc, res))