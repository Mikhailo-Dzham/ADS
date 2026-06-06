import sys
import heapq  # для купи


def solve():
    input_data = sys.stdin.read().split()

    t = int(input_data[0])
    idx = 1

    out = []
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        p = int(input_data[idx + 2])
        q = int(input_data[idx + 3])
        idx += 4

        # список суміжності для графа
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx + 1])
            w = int(input_data[idx + 2])
            idx += 3
            adj[u].append((w, v))
            adj[v].append((w, u))

        # Алгоритм Прима
        visited = [False] * (n + 1)
        pq = []  # мін-купа для ребра з найменшою вагою

        visited[1] = True
        for w, v in adj[1]:
            # Кидаєм в купу: (вага ребра, звідки, куди)
            heapq.heappush(pq, (w, 1, v))

        edge_in_mst = False
        edges_added = 0

        while pq and edges_added < n - 1:
            w, u, v = heapq.heappop(pq)

            if visited[v]:
                continue

            visited[v] = True
            edges_added += 1

            # Дивимся, чи є це ребро цільовим маршрутом
            if (u == p and v == q) or (u == q and v == p):
                edge_in_mst = True

            for next_w, next_v in adj[v]:
                if not visited[next_v]:
                    heapq.heappush(pq, (next_w, v, next_v))

        if edge_in_mst:
            out.append("YES")
        else:
            out.append("NO")

    print('\n'.join(out))


if __name__ == '__main__':
    solve()