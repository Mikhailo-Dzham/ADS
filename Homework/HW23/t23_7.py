from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
components = []

for start in range(1, n + 1):

    if not visited[start]:

        # BFS
        q = deque([start])
        visited[start] = True

        comp = []

        while q:
            v = q.popleft()
            comp.append(v)

            for to in graph[v]:
                if not visited[to]:
                    visited[to] = True
                    q.append(to)

        components.append(comp)



print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)