def solve():

    A = int(input().strip())
    P = int(input().strip())

    if A == 0:
        print(0)
        return

    stack = []

    # Заповнюємо стек остачами від ділення
    while A > 0:
        stack.append(A % P)
        A //= P

    result = []

    # Витягуємо елементи зі стеку, автоматично отримуючи правильний порядок
    while stack:
        digit = stack.pop()
        if digit > 9:
            result.append(f"[{digit}]")
        else:
            result.append(str(digit))

    print("".join(result))


if __name__ == '__main__':
    solve()