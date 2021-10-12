N = int(input()) # N : 2, 4, 8, 16, 32, 64, 128 중 하나이다.
paper=[]

for _ in range(N):
    paper.append(list(map(int,input().split())))

one = 0
zero = 0

def solv(x,y,N):
    global one, zero

    start = paper[x][y]
    divide = False

    for i in range(x, x+N):
        for j in range(y, y+N):
            if start != paper[i][j]:
                divide = True
                break
    
    if divide is True:
        N = N//2
        solv(x, y, N) # 0, 0, 4
        solv(x, y+N, N) # 0, 4, 4
        solv(x+N, y, N) # 4, 0, 4
        solv(x+N, y+N, N) # 4, 4, 4
    
    if divide is False:
        if start == 1:
            one += 1
        elif start == 0:
            zero += 1

solv(0,0,N)
print(zero, one)
    
