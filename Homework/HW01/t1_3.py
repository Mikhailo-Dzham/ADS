def t1(n, k):
    k += 1           # 4               (k, 1, +, =)
    i = n             # 2                  (n, =)
    while i > 0:   # 3  * (n+1)      (i, 0, >)
        i -= 1        # 4  * n       (i, 1, -, =)
        # 7n + 9

def t2(k, n):
    i = n  # 2
    while i > 1:  # 3 * (log2(n) + 1)
        k += 1  # 4 * log2(n)
        i //= 2  # 4 * log2(n)
    # 11log2(n) + 5

def t3(k, n):
    i = 0  # 2
    while i < n:  # 3 * (n/2 + 1)
        j = 0  # 2 * (n/2)
        while j < n:  # 3 * (n/2 * (n/2 + 1))
            k += 1  # 4 * (n/2 * n/2)
            j += 2  # 4 * (n/2 * n/2)
        i += 2  # 4 * (n/2)
        # 2 +  1.5n + 3 + n + 3(n**2/4 + n/2) + n**2 + n**2 + 2n
        # 5 + 1.5n + 3 n + 3n**2/4 + 1.5n + 2n**2
        # 5 + 6n + 2.75n**2

def t4(k, n):
    i = 0  # 2
    while i < n:  # 3 * (n+1)
        j = 0  # 2 * n
        while j < i * i:  # 5 * (iteration sum + n)  <- (j, i, i, *, <)
            k += 1  # 4 * (sum)
            j += 1  # 4 * (sum)
        i += 1  # 4 * n
        # За формулою суми квадратів (сума з n-1 по i=0 для і**2)
        # 14n + 5 + 13((2n**3 - 3n**2 + n)/6)

def t5(k, n):
    i = 1  # 2
    while i < n:  # 3 * (log2(n) + 1)
        j = 1  # 2 * log2(n)
        while j < n:  # 3 * (log2(n) * (log2(n) + 1))
            k += 1  # 4 * (log2(n)^2)
            j *= 2  # 4 * (log2(n)^2)
        i *= 2  # 4 * log2(n)
    # 2 + 3log2(n) + 3 + 4log2(n) + 2log2(n) + 11(log2(n))**2 + 3log2(n)
    # 11(log2(n))**2 + 12log2(n) + 5

def t6(k, n):
    i = 1  # 2
    while i < n:  # 3 * (log2(n) + 1)
        j = i  # 2 * log2(n)
        while j < n:  # 3 * (iteration sum) \
            k += 1  # 4 * (iteration sum)       }  11 * ((log2(n) * (log2(n) + 1))/2 + 3log2(n)
            j *= 2  # 4 * (iteration sum)     /
        i *= 2  # 4 * log2(n)

    # (7log2(n) + 5) + 2log2(n) + 5.5(log2(n))**2 + 5.5log2(n) + 3log2(n)
    # 5.5(log2(n))**2 + 17.5log2(n) + 5
