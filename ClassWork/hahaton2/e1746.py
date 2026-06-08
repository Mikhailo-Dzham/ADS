n, m = list(map(int, input().split()))

labyrinth = [list(input()) for _ in range(n)]

def where_f_s(): #Повертає два массива, координати старту та фінішу. Работає
    f = []
    s = []
    for line in range(n):
        for char in range(m):
            if labyrinth[line][char] == "F":
                f = [line, char]
            elif labyrinth[line][char] == "S":
                s = [line, char]

    return f, s

def straight_away(x, y):
    



print(where_f_s())

visited = [[0] * m for _ in range(n)]

def finder(x, y):
    if labyrinth[x][y] == 'P' or visited[x][y]:
        return 0

    visited[x][y] =1

    area = 1

    # Хвильовий алгоритм
    # area += finder(x + 1, y)
    # area += finder(x - 1, y)
    # area += finder(x, y + 1)
    # area += finder(x, y - 1)

    return area


f, s = where_f_s()
print(*s)
finder(*s)
print(visited)