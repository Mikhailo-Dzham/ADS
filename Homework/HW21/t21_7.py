n, m = map(int, input().split())

degree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())

    degree[u] += 1
    degree[v] += 1

for i in range(1, n + 1):
    print(degree[i])