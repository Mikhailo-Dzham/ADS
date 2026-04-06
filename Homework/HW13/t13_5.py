BRACKETS = {
    ")" : "(", "]" : "[", "}" : "{"
}

def solve():
    d = input()

    stk = [] #Так, тут використаний список, але використовуємо його за принципом стенка

    for p in d:
        if not(stk and (p in BRACKETS)):
            stk.append(p)
            continue

        if stk[-1] != BRACKETS[p]:
            break
        stk.pop()
    if stk:
        print("no")
    else:
        print("yes")

if __name__ == "__main__":
    solve()
