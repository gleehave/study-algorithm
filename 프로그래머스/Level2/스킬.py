def calculate_depth(graph, start, depth):
    for node in graph[start]:
        if len(graph[node]) == 0:
            continue
        else:
            depth += 1
            calculate_depth(graph, node, depth)
    return depth


def solution(total_sp, skills):
    graph = {i:[] for i in range(1, len(skills)+2)}
    for skill in skills:
        a, b = skill[0], skill[1]
        graph[a].append(b)

    # root 노드를 찾아야한다.
    root_list = [0] * (len(skills)+2)
    for i in graph:
        root_list[i] = calculate_depth(graph, i, 1)

    root = root_list.index(max(root_list))

    visited = [False] * (len(skills)+2)
    queue = [root]
    visited[root] = True

    multipe = [0] * (len(skills)+2)
    while queue:
        start = queue.pop(0)

        for node in graph[start]:
            if visited[node] == False:
                visited[node] = True
                if len(graph[node]) == 0:
                    a = 1
                    multipe[node] = a
                    continue
                else:
                    a = len(graph[node])
                    multipe[node] = a
                    queue.append(node)

    for sub_node in graph[root]:
        multipe[root] += multipe[sub_node]

    x = total_sp // sum(multipe)
    result = [multipe[i] * x for i in range(1, len(multipe))]
    return result


solution(121, [[1,2], [1,3], [3,6], [3, 4], [3,5]])