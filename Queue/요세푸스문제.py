# K는 index다.
N, K = map(int, input().split())

res = []
Circle = [_ for _ in range(1,N+1)]
print('Circle: ',Circle)


for _ in range(N):
    print('res: ',res)
    for i in range(K):  # i = 0, 1, 2

        if i+1 == K:
            temp = Circle[0]
            res.append(temp)
            Circle.pop(0)
            break

        temp = Circle[0]
        print("temp: ", temp)
        Circle.append(temp)
        Circle.pop(0)

print("<")
for _ in res:
    print(_,sep=',')
print(">")
