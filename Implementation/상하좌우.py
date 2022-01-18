# 여행가는 n x n 크기의 공간위에 있다.
# 가장 왼쪽 좌표는 (1,1) 가장 오른쪽 좌표는 (n,n) 이다.
# LRUD 를 키워드로 움직인다.

# 입력을 받고, 초기 좌표인 (1,1)을 설정한다.
n = int(input())
x,y = 1,1

# LLRRUUDD 와 같은 이동 계획을 입력받는다.
plans = input().split()

# dx, dy가 합쳐져서 이동한다.
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    # 이동하고, 좌표를 nx, ny에 저장한다.
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나면? 무시.
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
