n, m = map(int, input().split())

edges = set()

for _ in range(m):
    u, v = map(int, input().split())

    edges.add((min(u, v), max(u, v)))

# complite graph's edges  = n * (n - 1) // 2
print("YES" if len(edges) == n * (n - 1) // 2 else "NO")