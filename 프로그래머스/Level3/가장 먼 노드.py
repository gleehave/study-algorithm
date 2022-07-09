# n개의 노드가 있는 그래프가 있다.
# 1~n 까지 노드번호가 적혀있음.
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 알고 싶다.
# 최단경로로 이동했을 때, 간선의 개수가 가장 많은 노드를 의미한다.

# 다익스트라?

from collections import deque
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, vertex):
    graph = {i:[] for i in range(1, n+1)} # 무방향 그래프
    for data in vertex:
        start, end = data[0], data[1]
        graph[start].append(end)
        graph[end].append(start)

    # 초기 세팅
    INF = 1e9
    distance = [INF]*(n+1) # 노드 번호 시작이 1번 (0번 인덱스 제외)
    visited = [False] * (n+1) # 노드 번호 시작이 1번 (0번 인덱스 제외)
    distance[1] = 0 # 1번 노드

    queue = [1]
    visited[1] = True

    while queue:
        start = queue.pop(0)

        for node in graph[start]:
            if visited[node] == False:
                distance[node] = distance[start] + 1
                visited[node] = True
                queue.append(node)

    result = distance[1:]
    return result.count(max(result))





# def solution(n, edge):
#     graph = {i:[] for i in range(1, n+1)} # 무방향 그래프
#     for data in edge:
#         start, end = data[0], data[1]
#         graph[start].append(end)
#         graph[end].append(start)
#
#     # 초기 세팅
#     INF = 1e9
#     distance = [INF]*(n+1) # 노드 번호 시작이 1번 (0번 인덱스 제외)
#     visited = [False] * (n+1) # 노드 번호 시작이 1번 (0번 인덱스 제외)
#     distance[1] = 0 # 1번 노드
#
#     # print("graph:", graph)
#     # print("distance:", distance)
#     # print("visited:", visited)
#
#     for _ in range(n):
#         minIndex = 1
#         min_value = INF
#
#         for i in range(n):
#             if not visited[i] and distance[i] < min_value:
#                 min_value = distance[i]
#                 minIndex = i
#
#         visited[minIndex] = True
#         for node in graph[minIndex]: # 1: [2, 3]
#             if not visited[node] and distance[minIndex]+1 < distance[node]:
#                 distance[node] = distance[minIndex]+1
#
#     result = distance[1:]
#     return result.count(max(result))

solution(n, edge)