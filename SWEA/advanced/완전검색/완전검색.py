# N x N
# 각 칸에서 오른쪽이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때,
# 지나는 칸에 써진 숫자의 합이 최소가 되도록 움직였다면
# 최소 합계가 얼마인가?

# 1 2 3
# 2 3 4
# 3 4 5

# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     sum = 0
#     start_x = 0
#     start_y = 0
#
#     dx = [1, 0] # 오른쪽
#     dy = [0, 1] # 아래
#
#     temp = []
#     while True:
#         sum += board[start_y][start_x]
#
#         for i in range(2):
#             move_y = start_y + dy[i]
#             move_x = start_x + dx[i]
#
#             temp.append([sum+board[move_y][move_x], i])

T = int(input())

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    global res, tmp
    if res < tmp:
        return
    if x == N-1 and y == N-1:
        res = tmp
        return
    for delta in range(2):
        move_x = x + dx[delta]
        move_y = y + dy[delta]
        if move_x < 0 or move_y >= N or move_y < 0 or move_y >= N:
            continue
        if (move_x, move_y) not in visited:
            visited.append((move_x, move_y))
            tmp += board[move_x][move_y]
            dfs(move_x, move_y)
            tmp -= board[move_x][move_y]
            visited.remove((move_x, move_y))

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    res = 10000000
    tmp = board[0][0]
    dfs(0, 0)
    print("#{} {}".format(tc, res))
