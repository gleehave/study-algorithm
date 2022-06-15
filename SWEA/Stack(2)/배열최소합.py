# NxN 배열에 숫자가 있다.
# 한줄에 1개씩 N개의 숫자를 골라 합이 최소가 되도록한다.
# 단, 세로로 같은 줄에서 2개 이상의 숫자를 고를 수 없다.

# 가자치기 기법을 활용
# 백트래킹 적용 필요

def backtracking(i, N, s, visited):
    global sumV
    if i == N:
        if s < sumV:
            sumV = s
    elif s > sumV:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                backtracking(i+1, N, s+num_list[i][j], visited)
                visited[j] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    sumV = 100
    visited = [0] * N

    backtracking(0, N, 0, visited)
    print(f"#{tc+1} {sumV}")