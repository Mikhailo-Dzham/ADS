import sys

def dfs(graph, v):
    for vertex in graph[v]:
        if vertex not in path:
            path.append(vertex)

            tree.append((v, vertex))

            dfs(graph, vertex)

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()

    n, m = map(int, data[0].split())

    graph = [[] for _ in range(n)]

    for edge in data[1:]:
        u, v = map(int, edge.split())
        u -= 1
        v -= 1

        graph[u].append(v)
        graph[v].append(u)

    path = [0]
    tree = []

    dfs(graph, 0)

    for u, v in tree:
        print(u + 1, v + 1)