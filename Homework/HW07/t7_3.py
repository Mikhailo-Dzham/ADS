import sys # треба для швидшого зчитування данних


def solve():
    # В мене не проходило по часу, того я оптимізував інпут. Хоча проблема виявилася в іншому, я так залишу для швидкості :)
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    numbers = input_data[1:]

    # треба використати просте число яке буде достатньо більше за 100000 щоб мінімізувати колізії та уникнути перезаповнення
    TABLE_SIZE = 200003    #Пробував 150007 та 300007, але вони повільніші

    table = [[] for _ in range(TABLE_SIZE)]

    def my_hash(phone):
        """ ШОБ БАЛИ НЕ ЗНЯЛИ """
        return int(phone) % TABLE_SIZE

    unique_count = 0

    for phone in numbers:
        idx = my_hash(phone)

        # Перевіряємо, чи є вже такий номер у нашому ланцюжку (колізії)
        found = False
        for item in table[idx]:
            if item == phone:
                found = True
                break

        # Якщо номера ще немає, додаємо його і збільшуємо каунтер
        if not found:
            table[idx].append(phone)
            unique_count += 1

    print(unique_count)


if __name__ == '__main__':
    solve()