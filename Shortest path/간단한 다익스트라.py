import sys

input = sys.stdin.readline
INF = int(1e9) # 무한값

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수
start = int(input())             # 시작노드를 입력
graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1)        # 방문기록 리스트
distance = [INF] * (n+1)         # 최단거리 테이블을 초기화

for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c이다.
    graph[a].append((b, c))             # graph에 입력

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환한다.
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작노드 초기화
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node() # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        visited[now] = True

        for j in graph[now]: # 현재 노드와 연결된 다른 노드를 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start)

