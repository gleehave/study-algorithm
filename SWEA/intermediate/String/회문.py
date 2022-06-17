# # N x M 에 글자판이 있다.
# # 길이가 M인 회문을 찾는다.
#
# def horizontal(board, N, M):
#     for row in range(N):
#         for column in range(N-M+1):
#             if board[row][column:column+M] == board[row][column:column+M][::-1]:
#                     return board[row][column:column+M]
#
# def vertical(board, N, M):
#     for row in range(N-M+1):
#         for column in range(N):
#             column_list = []
#             for i in range(M):
#                 column_list.append(board[row+i][column])
#             if column_list == column_list[::-1]:
#                 return column_list
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     board = [list(map(str, input().split())) for _ in range(N)]
#
#     horizon = horizontal(board, N, M)
#     verti = vertical(board, N, M)
#     if horizon:
#         print("#{} {}".format(test_case, horizon))
#     if verti:
#         print("#{} {}".format(test_case, verti))

for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [0 for _ in range(n)]
    for i in range(n):
        arr[i] = list(input())
    count = 0
    print("#{} ".format(t + 1), end="")

    for i in range(n):
        for j in range(0, n - m + 1):
            for k in range(m // 2):
                if arr[i][j + k] == arr[i][j + m - 1 - k]:
                    count += 1
            if count == m // 2:
                for l in range(j, j + m):
                    print(arr[i][l], end="")
            count = 0
    # 세로축
    count = 0
    for j in range(n):
        for i in range(0, n - m + 1):
            for k in range(m // 2):
                if arr[i + k][j] == arr[i + m - 1 - k][j]:
                    count += 1
            if count == m // 2:
                for l in range(i, i + m):
                    print(arr[l][j], end="")
            count = 0
    print("")
