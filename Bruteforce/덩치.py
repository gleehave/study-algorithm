N = int(input())
Data = []

for i in range(N):
    weight, height = map(int, input().split())
    Data.append((weight, height))

for i in Data:
    rank = 1
    for j in Data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank)
