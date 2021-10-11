# K는 index다.
N, K = map(int, input().split())

res = []
Circle = [_ for _ in range(1,N+1)]

for _ in range(N):
    for i in range(K):  # i = 0, 1, 2

        if i+1 == K:
            temp = Circle[0]
            res.append(temp)
            Circle.pop(0)
            break

        temp = Circle[0]
        Circle.append(temp)
        Circle.pop(0)

print("<",end='')
for i in range(N):
    if i == N-1:
        print(res[i], end='')
        break
    print(res[i], end='')
    print(', ', end='')
print(">")