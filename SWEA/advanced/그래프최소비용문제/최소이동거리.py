# A도시에 E개의 일방통행 구간이 있다.
# 각 구간이 만나는 연결지즘에는 0~N까지 번호가 있다.

# 시작, 끝, 연결지점 번호, 구간 길이가 주어질 때,
# 0~N 까지 최소 이동거

# N=2, E=3
# 0 1 1
# 0 2 6
# 1 2 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])

    INF = float('inf')
    dist = [INF] * (V+1)
    selected = [False] * (V+1)

    dist[0] = 0
    cnt = 0
    while cnt < V:
        min = INF
        u = -1
        for i in range(V+1):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i

        selected[u] = True
        cnt += 1
        for w, cost in adj[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost

    print("#{} {}".format(tc, dist[V]))