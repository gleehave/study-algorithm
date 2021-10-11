N = int(input())
Triangle = []

for _ in range(N):
    temp = list(map(int, input().split()))
    Triangle.append(temp)

Row = 2
for i in range(N):  # i = 1,2,3,4/ i = 2
    if i == 0:
        continue    
    for j in range(Row): # j = 0,1 / j= 0, 1, 2
        if j == 0:
            Triangle[i][j] = Triangle[i][j] + Triangle[i-1][j]
        elif i == j:
            Triangle[i][j] = Triangle[i][j] + Triangle[i-1][j-1]
        else:
            Triangle[i][j] = max(Triangle[i-1][j-1], Triangle[i-1][j]) + Triangle[i][j]
    Row += 1

print(max(Triangle[-1]))