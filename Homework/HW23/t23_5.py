from collections import deque

n, m = map(int, input().split())

edges = [None]  # щоб індексація ребер була з 1
graph = [[] for _ in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, input().split())
    edges.append((a, b))

    graph[a].append((b, i))
    graph[b].append((a, i))

k = int(input())

for _ in range(k):
    data = list(map(int, input().split()))

    c = data[0]
    removed = set(data[1:])

    visited = [False] * (n + 1)

    # BFS
    q = deque([1])
    visited[1] = True

    while q:
        v = q.popleft()

        for to, edge_id in graph[v]:

            if edge_id in removed:
                continue

            if not visited[to]:
                visited[to] = True
                q.append(to)

    if all(visited[1:]):
        print("Connected")
    else:
        print("Disconnected")