# 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래 이다.
# 각 칸에서는 상하좌우 칸이 나타내는 인접지역으로만 이동할 수 있다.

# 인접지역으로 이동시에는 기본적으로 1만큼의 연료가 들고,
# 더 높은 곳으로 이동하는 경우, 높이 차이만큼 추가로 연료 소비된다.

from collections import deque
move = [(1,0), (0,1), (-1,0), (0,-1)]

for t in range(int(input())):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')

    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0
    queue = deque()
    queue.append((0,0))

    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            my, mx = dy+y, dx+x

            if 0 <= my < N and 0 <= mx < N:
                temp = 1
                if map_list[my][mx] > map_list[y][x]:
                    temp += map_list[my][mx] - map_list[y][x]
                if distance[my][mx] > distance[y][x] + temp:
                    distance[my][mx] = distance[y][x] + temp
                    queue.append((my, mx))
    print("#{} {}".format(t+1, distance[N-1][N-1]))