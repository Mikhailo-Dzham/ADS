import sys


def solve():
    input_data = sys.stdin.read().split()


    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    #сортування вставкою
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        moved = False

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            moved = True  # Фіксуємо, що відбулося зміщення

        arr[j + 1] = key

        # Якщо елемент змінив свою позицію, виводимо поточний стан масиву
        if moved:
            print(" ".join(map(str, arr)))


if __name__ == '__main__':
    solve()