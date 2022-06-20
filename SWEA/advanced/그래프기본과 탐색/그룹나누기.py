def Find(x):
    if x == parent[x]:
        return x
    else:
        return Find(parent[x])

def Union(x,y):
    parent[Find(y)] = Find(x)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    parent = [0] * (N+1)

    for i in range(1, N+1):
        parent[i] = i

    init = list(map(int, input().split()))
    for i in range(M):
        start = init[2*i]
        end = init[2*i+1]
        Union(start, end)

    result = []
    for i in range(len(parent)):
        result.append(Find(i))

    print("#{} {}".format(tc, len(set(result))-1))
