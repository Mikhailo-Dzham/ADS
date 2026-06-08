import sys
from collections import deque


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    m = int(input_data[1])

    grid = []
    idx = 2
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(input_data[idx])
            idx += 1
        grid.append(row)

    # Переводимо в 0-індексацію
    x1 = int(input_data[idx]) - 1
    y1 = int(input_data[idx + 1]) - 1
    x2 = int(input_data[idx + 2]) - 1
    y2 = int(input_data[idx + 3]) - 1

    start_r, start_c = y1, x1
    target_r, target_c = y2, x2

    if grid[start_r][start_c] == '1' or grid[target_r][target_c] == '1':
        print("-1")
        return

    if start_r == target_r and start_c == target_c:
        print("0")
        return

    # Черга для BFS: зберігає (рядок, стовпець, поточна дистанція)
    q = deque([(start_r, start_c, 0)])
    grid[start_r][start_c] = '1'

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        r, c, dist = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Перевірка меж лабіринту та чи є клітинка прохідною
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '0':
                if nr == target_r and nc == target_c:
                    print(dist + 1)
                    return

                grid[nr][nc] = '1'  # Одразу відмічаємо як відвідану, шоб уникнути дублювання в черзі
                q.append((nr, nc, dist + 1))

    print("-1")


if __name__ == '__main__':
    solve()