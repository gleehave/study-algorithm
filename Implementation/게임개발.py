# N X M 크기의 직사각형,
# 육지, 바다, 캐릭터
# 맵의 각 칸은 (A, B)로 표현
# A는 북쪽으로부터 떨어진 칸의 개수
# B는 서쪽으로부터 떨어진 칸의 개수

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
# 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약, 4방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한채로 한칸 뒤로 가고 1단계로 돌아간다.
# 단, 이때, 바다인 칸이라 뒤로 갈 수 없는 경우에는 움짐임을 멈춘다.

# 0, 1, 2, 3 : 북, 동, 남, 서
# 0: 육지, 1: 바다

n, m = map(int, input().split())
d = [[0] * m for _ in range(n)] # 방문한 위치 저장
x, y, direction = map(int, input().split()) # 현재 캐릭터 x, y좌표
d[x][y] = 1 # 캐릭터 처음 위치 방문처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
