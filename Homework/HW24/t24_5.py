import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    grid = input_data[1:]

    # Черга для BFS; відвідувач може зайти через обидва входи
    q = deque([(0, 0), (n - 1, n - 1)])
    visited = {(0, 0), (n - 1, n - 1)}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Знаходимо всі доступні порожні клітинки
    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == '.' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))

    faces_count = 0

    # Обчислюємо кількість видимих граней стін
    for r, c in visited:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Якщо виходимо за межі сітки — це зовнішня стіна
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                # Ігноруємо відсутні стіни на місці входів
                if r == 0 and c == 0 and (dr == -1 or dc == -1):
                    continue
                if r == n - 1 and c == n - 1 and (dr == 1 or dc == 1):
                    continue
                faces_count += 1

            elif grid[nr][nc] == '#':
                faces_count += 1

    print(faces_count * 9)


if __name__ == '__main__':
    solve()