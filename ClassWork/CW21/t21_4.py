n = int(input())
AI = [[] for _ in range(n + 1)]
k = int(input())
for _ in range(k):
    arr = list(map(int, input().split()))
    q, a = arr[0], arr[1]
    if q == 1:
        b = arr[2]
        AI[a].append(b)
        AI[b].append(a)
    if q == 2:
        print(*AI[a])