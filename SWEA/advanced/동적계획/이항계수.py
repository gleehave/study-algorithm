T = int(input())
A = []
for a in range(71):
    nA = [-1] * 71
    A.append(nA)
    nA = []
for t in range(1, T+1):
    n, a, b = map(int, input().split())
    c = min(a, b)
    for i in range(n+1):
        for j in range(min(i+1, c+1)):
            if A[i][j] == -1:
                if j == 0 or j == i:
                    A[i][j] = 1
                else:
                    A[i][j] = A[i-1][j] + A[i-1][j-1]
    print("#{} {}".format(t, A[n][c]))