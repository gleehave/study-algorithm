# 10 x 10 격자에 색을 칠한다.
# 예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
# 2
# 2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
# 3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )


T = int(input())
for test_case in range(1, T + 1):
    # 데이터 입력 받기
    N = int(input())
    rectangle = [list(map(int, input().split())) for _ in range(N)]

    # 10 x 10이 고정이므로, 초기세팅
    canvas = [[0]*10 for _ in range(10)]
    count = 0

    # 입력받은 rectangle의 좌표를 가져와서
    for color in rectangle:
        # row, column 에다가 color의 값을 입력
        for row in range(color[0], color[2]+1):
            for column in range(color[1], color[3]+1):
                if canvas[row][column] == 0:
                    canvas[row][column] = color[-1]
                elif canvas[row][column] != 3 and canvas[row][column] != color[-1]:
                    canvas[row][column] = 3
                    count += 1

    print("#{} {}".format(test_case, count))