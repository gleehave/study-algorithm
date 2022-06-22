T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = [[N, 0]] # 넣을 차례인 수, 합
    ans = 0
    while A:
        cur = A.pop()
        if cur[0] == 0:
            continue

        bound = cur[0] * (cur[0]+1)/2 + cur[1]
        if bound >= K:
            if cur[0] + cur[1] == K:
                ans += 1
            elif cur[0] + cur[1] < K:
                A.append(([cur[0]-1, cur[0] + cur[1]]))
            A.append([cur[0]-1, cur[1]])

    print("#{} {}".format(t, ans))
