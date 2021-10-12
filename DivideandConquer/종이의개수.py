# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, 
# # -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

'''
N = int(input()) # N = 3, 9, 27, 81 ... 3^K 의 형태
Divide = int(N/3)

paper = []
for _ in range(N):
    paper.append(list(map(int,input().split())))

minus_count = []
zero_count = []
one_count = []
Start = 0

def segmentation(paper, Start, Divide):
    for i in range(Start, Divide-1): # i: 0,1,2
        for j in range(Start, Divide-1): # j: 0,1,2
            if paper[Start][Start] == paper[i][j]:
                continue

            if paper[Start][Start] != paper[i][j]:
                Divide = int(Divide/3)
                segmentation(paper, Start, Divide)
    if paper[Start][Start] == -1:
        minus_count.append(1)
    elif paper[Start][Start] == 0:
        zero_count.append(1)
    else:
        one_count.append(1)
    print('return: ',paper[Start][Start])
    return paper[Start][Start]

count = 3
while count > 0:
    count -= 1
    print('START: ',Start, "Divide: ",Divide)
    segmentation(paper, Start, Divide)
    Start = Start + Divide
    Divide = Divide + Divide
'''

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

one_count = 0
zero_count = 0
minus_count = 0

def dnc(x,y,n):
    global one_count, zero_count, minus_count

    check = graph[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != graph[i][j]:
                check = -2
                break
    
    if check == -2:
        n = n // 3
        dnc(x, y, n)                # 0, 0, 3
        dnc(x, y + n, n)            # 0, 3, 3
        dnc(x, y + 2 * n, n)        # 0, 6, 3
        dnc(x + n, y, n)            # 3, 0, 3
        dnc(x + n, y + n, n)        # 3, 3, 3
        dnc(x + n, y + 2 * n, n)    # 3, 6, 3
        dnc(x + 2 * n, y, n)        # 6, 0, 3
        dnc(x + 2 * n, y + n, n)    # 6, 3, 3
        dnc(x + 2 * n, y + 2 * n, n) # 6, 6, 3
    elif check == 1:
        one_count += 1
    elif check == 0:
        zero_count += 1
    else: minus_count += 1

dnc(0,0,n)
print( minus_count, zero_count, one_count)