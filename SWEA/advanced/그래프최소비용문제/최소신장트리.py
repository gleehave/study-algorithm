# 그래프에서 사이클 제거
# 모든 노드를 포함하는 트리를 구성한다.
# 가중치의 합이 최소가 되고자한다.

# 0 ~ V 번까지의 노드
# E 개의 간선을 가진 그래프 주어진다.

# V E       : 2 3
# n1, n2, w : 0 1 1
# n1, n2, w : 0 2 1
# n1, n2, w : 1 2 6

from heapq import heappop, heappush

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        a, b = b, a
    parents[b] = a

for test in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    parents = {i: i for i in range(V+1)}
    edges = []
    for _ in range(E):
        a, b, w = map(int, input().split())
        heappush(edges, (w, a, b))

    answer = 0
    while edges:
        w, a, b = heappop(edges)
        if find(a) != find(b):
            union(a, b)
            answer += w
    print("#{} {}".format(test, answer))