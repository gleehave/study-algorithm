# N x M 크기의 미로에서 출발지, 목적지가 주어진다.
# 최소 몇개의 칸을 지나면 출발지->도착지에 다다를 수 있는가?
# 경로가 있다면 최소한의 칸 수를 출력
# 경로가 없다면 0을 출력

def IsSafe(y, x):
    return 0<=y<N and 0<=x<N and (Maze[y][x] == 0 or Maze[y][x] == 3)

def BFS(start_y, start_x):
    global D_result
    Q.append((start_y, start_x))
    visited.append((start_y, start_x))

    while Q:
        start_y, start_x = Q.pop(0)
        for dir in range(4):
            NewY = start_y + dy[dir]
            NewX = start_x + dx[dir]
            if IsSafe(NewY, NewX) and (NewY, NewX) not in visited:
                Q.append((NewY, NewX))
                visited.append((NewY, NewX))
                Distance[NewY][NewX] = Distance[start_y][start_x]+1
                if Maze[NewY][NewX] == 3:
                    D_result = Distance[NewY][NewX] - 1
                    return

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Maze = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    D_result = 0
    Q = []
    Distance = [[0]*N for _ in range(N)]
    BFS(start_y, start_x)
    print("#{} {}".format(test_case, D_result))