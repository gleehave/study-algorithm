# 일정액을 내면 크기가 정해진 박스가 가득 찰 때까지 마음대로 물건을 담을 수 있다.
# 물건의 가격의 합계가 최대가 되고자 한다.

# 상품 크기의 합이 박스 크기를 초과할 수 없다.
# 박스 크기 10 이고, 상품의 크기와 가격이 주어지면
# 최대로 담을 수 있는 가격 합계는 2번과 3번인 25일 때 최대가 된다.

# 상품    크기    가격
# 1      6      12
# 2      5      10
# 3      5      15
# 4      4      6

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