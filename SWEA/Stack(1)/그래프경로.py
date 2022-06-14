# # V: 정점의 수 / E: 간선의 수
# # S: 출발 정점 / G: 도착 정점
# # S - > G 의 경로가 있으면 1 없으면 0 출력
#
# def dfs(graph, S, G, V):
#     visit = [False] * V
#     stack = []
#     stack.append(S)
#
#     while stack:
#         current = stack.pop()
#         visit[current] = True
#
#         for next in range(1,V+1):
#             if not visit[next] and node[current][next]:
#                 stack.append(next)
#     if visit[G]:
#         return 1
#     else:
#         return 0
#
#
#
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     V, E = map(int, input().split())
#     graph = []
#
#     for _ in range(E):
#         a, b = map(int, input().split())
#         graph.append([a, b])
#
#     S, G = map(int, input().split())
#
#

# T = int(input())
#
# def dfs(start, end, node):
#     stack = []
#     visited = [False] * (V + 1)
#     stack.append(start)
#
#     while stack:
#         now = stack.pop()
#         visited[now] = True
#         for next in range(1, V+1):
#             if not visited[next] and node[now][next]:
#                 stack.append(next)
#     if visited[end]:
#         return 1
#     else:
#         return 0
#
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     node = [[0 for _ in range(V+1)]for _ in range(V+1)]
#     for _ in range(E):
#         start, end = map(int, input().split())
#         node[start][end] = 1
#     S, G = map(int, input().split())
#     print("#{} {}".format(tc, dfs(S, G, node)))

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[]for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        node[start].append(end)

    S, G = map(int, input().split())
    stack = [S]
    visited = [False for _ in range(V+1)]

    while stack:
        now = stack.pop()
        visited[now] = True
        for next in node[now]:
            if not visited[next]:
                stack.append(next)

    if visited[G]:
        result = 1
    else:
        result = 0

    print("#{} {}".format(tc, result))