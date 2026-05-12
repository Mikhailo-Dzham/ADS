n = int(input())
r = 0
for i in range(n):
    if sum(list(map(int, input().split()))) == 1:
        r +=1
    
print(r)