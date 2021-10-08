K = int(input())
res=[]
mid=[]

for _ in range(K):
    Data = int(input())
    mid.append(Data)

for i in mid:
    if i != 0:
        res.append(i)
    if i == 0:
        res.pop()

print(sum(res))