# 1~N까지의 도시가 있다.
# M개의 단방향 도로가 있다. 모든 도로의 거리는 1이다.
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력해라

# N=4, K=2, X=1일때,
# 1번 도시에서 출발하여 도달할 수 있는 도시 중, 최단거리가 2인 도시는 4번도시 뿐이다.
# N, M, K, X = 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

N, M, K, X = map(int, input().split()); print("N, M, K, X: ", N, M, K, X)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

print("graph: ", graph)

distance = [-1]*(N+1)
distance[X] = 0

print("(시작점 세팅) distance: ", distance)

q = deque([X])
while q:
    now = q.popleft(); print("(노드번호) now: ", now)
    print("graph[now]: ", graph[now])
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

print("(final) distance: ",distance)
check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)