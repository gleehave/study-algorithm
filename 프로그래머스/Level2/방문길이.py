# U: 위쪽 1칸
# D: 아래쪽 1칸
# R: 오른쪽 1칸
# L: 왼쪽 1칸

# 시작점 0,0
# 좌표평면은 (-5,5) (-5,-5) (5,5) (5,-5)

# 처음 걸어간 길이를 알고싶다.
# 경계를 넘어가면 무시한다.


def solution(dirs):
    route = []
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    start_x = 0
    start_y = 0

    for dir in dirs:
        if dir == 'U':
            move_x = start_x + dx[2]
            move_y = start_y + dy[2]
        if dir == 'D':
            move_x = start_x + dx[3]
            move_y = start_y + dy[3]
        if dir == 'R':
            move_x = start_x + dx[1]
            move_y = start_y + dy[1]
        if dir == 'L':
            move_x = start_x + dx[0]
            move_y = start_y + dy[0]
        if (move_x < -5 or move_x > 5) or (move_y > 5 or move_y < -5):
            continue
        if (start_x, start_y, move_x, move_y) not in route:
            route.append((start_x, start_y, move_x, move_y))
            route.append((move_x, move_y, start_x, start_y))
        start_x = move_x
        start_y = move_y
    return len(route)//2

# dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
print(solution(dirs))