import sys

BRACKETS = {
    ")" : "(", "]" : "[", "}" : "{"
}

##########################################

def solve():
    data = sys.stdin.read().split("\n")

    for i in range(int(data[0])):

        d = data[i+1]

        stk = []

        for p in d:
            if not(stk and (p in BRACKETS)):
                stk.append(p)
                continue

            if stk[-1] != BRACKETS[p]:
                break
            stk.pop()
        if stk:
            print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    solve()
