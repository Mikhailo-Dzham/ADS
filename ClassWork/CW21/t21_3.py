n = int(input())
r = 0
for i in range(n):
    r += sum(list(map(int, input().split())))
print(r)
