def solve():
    n = int(input().strip())

    bin_str = bin(n)[2:]
    length = len(bin_str)

    shifts = []
    for i in range(length):
        shifted_str = bin_str[i:] + bin_str[:i]
        shifts.append(int(shifted_str, 2))

    # БІНАРНИЙ ПОШУК ПО ВІДПОВІДІ
    # low та high - межі нашого простору пошуку відповідей
    low = 0
    high = (1 << length) - 1

    best_ans = 0

    while low <= high:
        mid = (low + high) // 2

        # логіка бінарного пошуку:
        # Перевіряємо чи досяжне значення mid (чи є хоч один зсув >= mid)
        if any(shift >= mid for shift in shifts):
            best_ans = mid
            low = mid + 1 # Підходе? йдемо вгору
        else:
            high = mid - 1 # Ні -- шукаємо в меншій половині простору

    print(best_ans)


if __name__ == '__main__':
    solve()