import sys


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    m = int(input_data[1])

    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1  # 0-індексація
        v = int(input_data[idx + 1]) - 1
        w = int(input_data[idx + 2])
        edges.append((u, v, w))
        idx += 3

    INF = float('inf')
    dist = [INF] * n
    dist[0] = 0

    # Алгоритм Беллмана-Форда
    for _ in range(n - 1):
        any_changed = False
        for u, v, w in edges:
            # Перевіряємо, чи досяжна вершина u, і чи покращує ребро шлях до v
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                any_changed = True

        if not any_changed:
            break

    result = []
    for d in dist:
        if d == INF:
            result.append("30000")
        else:
            result.append(str(d))

    print(" ".join(result))


if __name__ == '__main__':
    solve()