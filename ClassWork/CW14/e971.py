n, k = [int(i) for i in input().split()]

n_massive = [i for i in range(1, n+1)]
print(n_massive)

def reduc(massive):
    del massive[::3]

while len(n_massive) != 0:
    reduc(n_massive)

print(n_massive[0])

