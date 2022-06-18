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
    if res < tmp:  # 현재 결과값 보다 크면 함수 끝나도록 -> 제한시간때문에 가지치기 해야함
        return
    if x == N-1 and y == N-1:
        res = tmp
        return
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if (nx, ny) not in visited:
            visited.append((nx, ny))  # 좌표 업로드
            tmp += a[nx][ny]
            print("dfs 전 tmp: ", tmp)
            dfs(nx, ny)
            tmp -= a[nx][ny]  # 원상복구
            print('dfs 후 tmp:', tmp)
            visited.remove((nx, ny))
            print("visited 제거: ", visited)


for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    visited = [] # stack 역할을 한다.
    res = 3000
    tmp = a[0][0]
    dfs(0, 0)  # 현재좌표
    print("#{} {}".format(tc, res))