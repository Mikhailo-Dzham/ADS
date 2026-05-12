from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

k = int(input())
starts = list(map(int, input().split()))

# BFS від багатьох джерел
dist = [-1] * (n + 1)
queue = deque()

for v in starts:
    dist[v] = 0
    queue.append(v)

while queue:
    v = queue.popleft()

    for to in graph[v]:
        if dist[to] == -1:
            dist[to] = dist[v] + 1
            queue.append(to)

max_dist = max(dist[1:])

answer_vertex = min(
    i for i in range(1, n + 1)
    if dist[i] == max_dist
)

print(max_dist)
print(answer_vertex)