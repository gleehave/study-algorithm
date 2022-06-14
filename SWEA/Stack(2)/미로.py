# # NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램
# # 도착할 수 있으면 1, 아니면 0을 출력한다.
# # 2에서 출발, 3에 도착, 0은 통로
#
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     maze = [list(input()) for _ in range(N)]
#
#     moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]
#
#     for i in range(N):
#         if 2 in maze[i]:
#             x = maze[i].index(2)
#             y = i
#             break
#
#     x = 0
#     y = 0
#
#     stack = [(y, x)]
#     result = 0
#     while stack:
#         y, x = stack.pop()
#         maze[y][x] = 1
#
#         for moveY, moveX in moves:
#             dy = y + moveY
#             dx = x + moveX
#
#             if dx < 0 or dy < 0 or y >= N or x >= N:
#                 result = True
#                 break
#
#
#             if maze[dy][dx] == 3:
#                 result += 1
#                 break
#
#             elif not maze[dy][dx]:
#                 stack.append((dy, dx))
#
def IsSafe(y, x):
    return 0<= y < N and 0 <= x < N and (maze[y][x]==0 or maze[y][x]==3)

def DFS(start_y, start_x):
    global result

    if maze[start_y][start_x] == 3:
        result = 1
        return

    visited.append((start_y, start_x))
    for dir in range(4):
        new_y = start_y + dy[dir]
        new_x = start_x + dx[dir]
        if IsSafe(new_y, new_x) and (new_y, new_x) not in visited:
            DFS(new_y, new_x)

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y,x

    #상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = []
    result = 0
    DFS(start_y, start_x)
    print('#%d %d'%(tc, result))