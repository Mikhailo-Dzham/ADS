def solve():
    n, k = map(int, input().split())

    # Список для зберігання поточної перестановки
    current_permutation = []

    # used[i] буде True, якщо число i вже є в current_permutation
    used = [False] * (n + 1)

    def backtrack(depth):
        # Базовий випадок: як довжина перестановки досягла k, виводимо її
        if depth == k:
            print(" ".join(map(str, current_permutation)))
            return

        for i in range(1, n + 1):
            if not used[i]:

                used[i] = True
                current_permutation.append(i)

                backtrack(depth + 1)

                current_permutation.pop()
                used[i] = False

    # Запускаємо рекурсію, починаючи з 0-ї глибини
    backtrack(0)


if __name__ == "__main__":
    solve()