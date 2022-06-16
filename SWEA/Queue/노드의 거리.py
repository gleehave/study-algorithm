from collections import deque

t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())

    queue = deque([s])
    visited = [0] * (v + 1)
    visited[s] = 1
    while (queue):
        n = queue.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[n] + 1

    if visited[g] != 0:
        print("#" + str(tc), visited[g] - 1)
    else:
        print("#" + str(tc), 0)