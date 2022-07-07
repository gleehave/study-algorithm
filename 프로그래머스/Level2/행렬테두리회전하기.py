# 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해,
# 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다.
# 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):

    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1,x2-1):
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1-1,y2-1):
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1,x1-1,-1):
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1,y1-1,-1):
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            mini = min(mini, test)

        array[x1-1][y1] = tmp
        answer.append(mini)

    return answer




# def solution(rows, columns, queries):
#     board = [[0 for col in range(columns)] for row in range(rows)]
#     data = 1
#     for row in range(rows):
#         for col in range(columns):
#             board[row][col] = data
#             data += 1
#
#     for query in queries:
#         start_x, start_y = query[0], query[1]
#         last_x, last_y = query[2], query[3]
#
#         if last_x-start_x > 1: # 공백이 있다.
#             blank = last_y - start_y - 1
#         else:
#             blank = 0
#
#         print("blank:", blank)
#         buffer = []
#         result = []
#         if blank == 0:
#             print("here")
#             for row in range(start_x-1, last_x-1):
#                 for col in range(last_y-1, last_y-1):
#                     buffer.append(board[row][col])
#
#         elif blank != 0:
#             for row in range(start_x-1, last_x): # 1 ~ 5 , row = (1 2 3 4)
#                 if row == start_x-1:
#                     buffer.append(board[row][start_y-1:last_y])
#                     continue
#                 if row == last_x-1:
#                     buffer.append(board[row][start_y-1:last_y])
#                     continue
#                 buffer.append(board[row][start_y])
#                 buffer.append(board[row][last_y])
#             print(buffer)
#             result.append(min(buffer))
#
#     return result

print(solution(rows, columns, queries))
