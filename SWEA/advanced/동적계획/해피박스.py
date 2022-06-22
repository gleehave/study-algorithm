
def knapsack():
    global K,N,W, weight, value
    for i in range(N+1):
        K[i][0] = 0
    for w in range(W+1):
        K[0][w] = 0

    for i in range(1, N+1):
        for w in range(1, W+1):
            if weight[i] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w-weight[i]]+value[i], K[i-1][w])

T = int(input())
for t in range(1, T+1):
    W, N = map(int, input().split())
    K = [[0 for x in range(W+1)] for x in range(N+1)]
    weight = [0 for x in range(N+1)]
    value = [0 for x in range(N+1)]
    for n in range(1, N+1):
        weight[n], value[n] = map(int, input().split())
    knapsack()
    print("#{} {}".format(t, K[N][W]))