n = int(input())

labyrinth = [list(input()) for _ in range(n)]

r, c = map(int, input().split())

# Шоб массив з нуля починався
r -= 1
c -= 1

visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    if labyrinth[x][y] == '*' or visited[x][y]:
        return 0

    visited[x][y] = True

    area = 1

    # Хвильовий алгоритм
    area += dfs(x + 1, y)
    area += dfs(x - 1, y)
    area += dfs(x, y + 1)
    area += dfs(x, y - 1)

    return area


print(dfs(r, c))