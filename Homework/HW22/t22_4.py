n, k, a, b, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# Читаєм переходи
for _ in range(k):
    u, v = map(int, input().split())
    graph[u].append(v)

count_routes = 0

def dfs(v, depth, visited):
    global count_routes

    # ліміт днів
    if depth > d:
        return

    # Дістались бази
    if v == b:
        count_routes += 1

    for to in graph[v]:
        if not visited[to]:
            visited[to] = True
            dfs(to, depth + 1, visited)
            visited[to] = False

visited = [False] * (n + 1)
visited[a] = True

dfs(a, 0, visited)

print(count_routes)