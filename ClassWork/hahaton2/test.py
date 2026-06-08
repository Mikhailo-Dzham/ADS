from collections import deque
def main():
    n,m = map(int, input().split())
    M = [[0]*m for _ in range(n)]
    for i in range(n):
        els = list(input())
        for j in range(m):
            M[i][j] = els[j]
            if els[j] == 'S':
                M[i][j] = 'V'
                s = (i,j)
                continue
            if els[j] == 'F':
                f = (i,j)
                continue

    q = deque()
    q.append(s)
    counter = 0
    while(len(q) != 0):
        data.append(*q) #тут додаємо в дату
        c = q.popleft()
        counter += 1
        i,j = c
        if M[i][j] == 'P':
            continue
        if i != 0:
            i_ = i - 1
            if M[i_][j] == 'F':
                return counter
            if M[i_][j] == 'V' or M[i_][j] == 'P':
                pass
            else:
                M[i_][j] = 'V'
                q.append((i_,j))
        if i != n-1:
            i_ = i+1
            if M[i_][j] == 'F':
                return counter
            if M[i_][j] == 'V' or M[i_][j] == 'P':
                pass
            else:
                M[i_][j] = 'V'
                q.append((i_,j))
        if j != 0:
            j_ = j-1
            if M[i][j_] == 'F':
                return counter
            if M[i][j_] == 'V' or M[i][j_] == 'P':
                pass
            else:
                M[i][j_] = 'V'
                q.append((i,j_))
        if j != m-1:
            j_ = j+1
            if M[i][j_] == 'F':
                return counter
            if M[i][j_] == 'V' or M[i][j_] == 'P':
                pass
            else:
                M[i][j_] = 'V'
                q.append((i,j_))
    return -1

def misha_fix(d):
    print(len(d))
    for line in d:
        for char in line:
            pass




if __name__ == "__main__":
    data = []
    main()


    misha_fix(data)
    # print(main())