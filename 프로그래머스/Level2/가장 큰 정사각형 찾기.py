# 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return

# 가장 작은 정사각형부터 확인하고, 하나하나 정사각형을 키워가면서 확인해야 한다.


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]


def solution(board):
    n = len(board) # row
    m = len(board[0]) # column

    dp = [[0]*m for _ in range(n)]
    # print("initalize DP: ", dp)
    dp[0] = board[0]
    # print("DP[0]:", dp)

    for i in range(1, n):
        dp[i][0] = board[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer**2

solution(board)