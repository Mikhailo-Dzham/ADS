import sys
import math


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    px = [0.0] * n
    py = [0.0] * n

    idx = 1
    for i in range(n):
        px[i] = float(input_data[idx])
        py[i] = float(input_data[idx + 1])
        idx += 2

    unvisited = list(range(n))
    min_dist_sq = [float('inf')] * n
    min_dist_sq[0] = 0.0
    ans = 0.0

    sqrt = math.sqrt

    while unvisited:
        best_sq = float('inf')
        u = -1

        for v in unvisited:
            if min_dist_sq[v] < best_sq:
                best_sq = min_dist_sq[v]
                u = v

        unvisited.remove(u)
        ans += sqrt(best_sq)

        ux = px[u]
        uy = py[u]

        for v in unvisited:
            dx = ux - px[v]
            dy = uy - py[v]
            d_sq = dx * dx + dy * dy
            if d_sq < min_dist_sq[v]:
                min_dist_sq[v] = d_sq

    print(f"{ans:.10f}")


if __name__ == '__main__':
    solve()