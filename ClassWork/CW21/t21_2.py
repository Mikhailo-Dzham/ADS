n = int(input())
AI = [[] for _ in range(n + 1)]

for i in range(n):
    I = list(map(int, input().split()))
    AI[i] = I[1:]
M = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j+1 in AI[i]:
            M[i][j] = 1
    print(*M[i])