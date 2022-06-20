# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만든다.
# +1, -1, *2, -10 -> 4가지 연산이 있을 때,
# 최소 몇번의 연산을 거쳐야 M을 만들 수 있는가?

# N =2, M=7
# (2+1)*2+1= 7  최소 3번의 연산 필요하다.

# 2 7     -> 3번
# 3 15    -> 4번
# 36 1007 -> 8번

from collections import deque

def operation():
    global result
    while Q:
        front, check = Q.popleft()
        if front == M:
            result = check
            return
        for i in range(4):
            if i == 0:
                if 1<= front + 1 <= 1000000 and visited[front+1] == False:
                    Q.append((front+1, check+1))
                    visited[front+1] = True
            elif i == 1:
                if 1<= front-1 <= 1000000 and visited[front-1] == False:
                    Q.append((front-1, check+1))
                    visited[front-1] = True
            elif i == 2:
                if 1 <= front * 2 <= 1000000 and visited[front*2] == False:
                    Q.append((front*2, check+1))
                    visited[front*2] = True
            elif i == 3:
                if i<= front-10 <=1000000 and visited[front-10] ==False:
                    Q.append((front-10, check+1))
                    visited[front-10] = True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    visited = [False] * 1000001
    Q = deque()
    Q.append((N, 0))
    operation()

    print("#{} {}".format(tc, result))