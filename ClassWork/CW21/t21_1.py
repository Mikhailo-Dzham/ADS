n = int(input())
M = []
m_l = [[] for _ in range(n + 1)]
for i in range(n):
    M.append(list(map(int, input().split())))


for i in range(n):
    for j in range(n):
        if M[i][j] == 1:
            if i < j:
                m_l[min(i, j)+1].append(max(i,j)+1)

for a in range(1, n+1):
    B = m_l[a]
    if B:
        for b in B:
            print(a, b)