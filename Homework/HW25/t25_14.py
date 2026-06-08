import sys


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])

    dist = []
    idx = 1
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(input_data[idx]))
            idx += 1
        dist.append(row)

    # Алгоритм Флойда-Воршелла: перевіряємо, чи шлях через вершину k
    # коротший за прямий шлях між вершинами i та j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Виводимо матрицю найкоротших шляхів
    for row in dist:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    solve()