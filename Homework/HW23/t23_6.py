from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1

#вершини без вхідних ребер
q = deque()

for v in range(1, n + 1):
    if indegree[v] == 0:
        q.append(v)

top_sort = []

while q:
    v = q.popleft()
    top_sort.append(v)

    for to in graph[v]:
        indegree[to] -= 1

        if indegree[to] == 0:
            q.append(to)

# якщо не всі вершини попали у відповідь, то є цикли
if len(top_sort) != n:
    print(-1)
else:
    print(*top_sort)