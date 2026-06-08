import sys


def dfs(v):
    visited[v] = True
    rec_stack[v] = True

    for to, edge in enumerate(graph[v]):
        if edge:
            if not visited[to]:
                if dfs(to):
                    return 1
            elif rec_stack[to]:
                return 1

    rec_stack[v] = False
    return 0


if __name__ == "__main__":
    data = sys.stdin.read().splitlines()

    n = int(data[0])

    graph = [list(map(int, row.split())) for row in data[1:]]

    visited = [False] * n
    rec_stack = [False] * n

    for v in range(n):
        if not visited[v]:
            if dfs(v):
                print(1)
                sys.exit()

    print(0)