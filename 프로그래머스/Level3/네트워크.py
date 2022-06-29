# N개의 컴퓨터 개수
# 연결에 대한 정보가 담긴 2차연 배열의 computers

# 네트워크의 개수를 return 하라.
# 각 컴퓨터는 0~N-1 정수료 표기한다.
# i 컴퓨터와 j 컴퓨터가 연결되어 있다면 computers[i][j]를 1로 표기한다.
# computers[i][i]는 항상 1이다.

n=3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# result 2

from collections import deque

# node는 index / visited는 방문한 node를 표기 한다.
# def bfs(n, computers, node, visited):
#     q = deque()
#     q.append(node)
#     visited[node] = True
#
#     while q:
#         start = q.popleft()
#         for move in range(n):
#             if move != start and computers[start][move] == 1:
#                 if visited[move] == False:
#                     q.append(move)
#
# def solution(n, computers):
#     answer = 0
#     visited = [False] * n
#     for node in range(n):
#         if visited[node] == False:
#             bfs(n, computers, node, visited)
#             answer += 1
#     return answer

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for node in range(n):
        if visited[node] == False:
            bfs(n, computers, node, visited)
            answer += 1
    return answer

def bfs(n, computers, node, visited):
    visited[node] = True
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        visited[node] = True
        for connect in range(n):
            if connect != node and computers[node][connect] == 1:
                if visited[connect] == False:
                    q.append(connect)


print(solution(n, computers))