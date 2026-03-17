import sys

def merge_sort(arr):
    # Базовий випадок рекурсії: масив з 1 або 0 елементів вже відсортований
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Зливаємо
        while i < len(L) and j < len(R):
            # використовуємо <=
            # Ми порівнюємо лише номери з індексом 0 в кортежах
            # Як вони рівні, то беремо елемент з Лівої половини, бо він був раніше в початковому списку
            if L[i][0] <= R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Дописуємо залишки лівої половини (якщо є)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Теж з права
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    robots = []

    # Робимо список з кортежів (основний номер, допоміжний номер)
    idx = 1
    for _ in range(n):
        robots.append((int(input_data[idx]), int(input_data[idx + 1])))
        idx += 2

    merge_sort(robots)

    # Швидке формування результату та вивід
    out = [f"{p} {s}" for p, s in robots]
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()