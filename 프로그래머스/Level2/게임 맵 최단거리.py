from collections import deque

def solution(maps):
    d = [[1,0], [-1,0], [0,1], [0,-1]]

    r = len(maps)
    c = len(maps[0])

    # 지나간 경로를 기억한다.
    table = [[-1 for _ in range(c)] for _ in range(r)]

    # 처음 시작점을 저장한다.
    queue = deque()
    queue.append([0, 0])

    # 처음 시작점을 다녀갔기 때문에, 1로 바꾼다.
    table[0][0] = 1

    while queue:
        # queue에서 꺼낸다.
        y, x = queue.popleft()

        for i in range(4):
            # 상, 하, 좌, 우 변화량 계산
            ny = y + d[i][0] # 좌표에서 더한다.
            nx = x + d[i][1] # 좌표에서 더한다.

            # 0부터 r-1 까지, 0부터 c-1 까지
            # 제한된 좌표계 안에 존재한다.
            if -1<ny<r and -1<nx<c:
                if maps[ny][nx] == 1: # 지나갈 수 있는 통로이면
                    if table[ny][nx] == -1: # 지나간 경로를 확인했을 때, 가능하다면
                        table[ny][nx] = table[y][x] + 1 # 최단경로값이 저장된다.
                        queue.append([ny, nx]) # queue에 좌표 저장

    answer = table[-1][-1]
    return answer