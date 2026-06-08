import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    s = int(input_data[1]) - 1 # Переходимо до 0-індексації
    f = int(input_data[2]) - 1

    adj_matrix = []
    idx = 3
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(int(input_data[idx]))
            idx += 1
        adj_matrix.append(row)

    INF = float('inf')
    dist = [INF] * n
    dist[s] = 0

    # зберігає кортежі (поточна_відстань, вершина)
    pq = [(0, s)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Якщо ми вже витягували цю вершину з меншою відстанню, пропускаємо
        if current_dist > dist[u]:
            continue

        # якщо дійшли до фінішу, можемо зупинити пошук
        if u == f:
            break

        for v in range(n):
            weight = adj_matrix[u][v]
            # Якщо ребро існує (-1 означає відсутність) і це не та сама вершина
            if weight != -1 and u != v:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))


    if dist[f] == INF: # шляху немає
        print("-1")
    else:
        print(dist[f])


if __name__ == '__main__':
    solve()