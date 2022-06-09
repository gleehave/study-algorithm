# 대기실 5개, 1개의 대기실은 5x5 크기
# 맨해튼 거리가 2 이하로 앉으면 안됨 (즉, 3이상)
# 단, 응시자가 앉아있는 자리 사이가 파티션으로 막혀있을 경우는 허용.
# P는 자리, 0은 빈 테이블, X는 파티션
# 맨해튼 거리: (r1, c1), (r2,c2)일 때, |r1-r2| + |c1-c2|
from collections import deque


def bfs(p):
    start = []

    # P가 있는 좌표 저장
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    # P가 있는 좌표 1개씩 꺼내서 deque에 저장
    for s in start:
        queue = deque([s])

        visited = [[0]*5 for i in range(5)]
        distance = [[0]*5 for i in range(5)]

        # 시작 방문 좌표 1로 바꾸기
        visited[s[0]][s[1]] = 1

        # 시작하는 P위치에서 qeue에 들어있는 모든 P와의 거리를 확인
        while queue:
            y, x = queue.popleft()

            dx = [-1,1,0,0]
            dy = [0,0,-1,1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    if p[ny][nx]=='P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))

    return answer