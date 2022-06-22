T = int(input())
A=[-1]*30

A[0] = 1
A[1] = 3
A[2] = 6

for t in range(1, T+1):
    N = int(input())
    for i in range(3, N):
        if A[i] == -1:
            A[i] = A[i-1] + 2*A[i-2] + A[i-3]
    print("#{} {}".format(t, A[N-1]))
