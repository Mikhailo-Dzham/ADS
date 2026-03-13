import sys
import random


def quick_sort(arr, low, high):
    if low < high:
        # Отримуємо індекс pivot
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    # Берем випадковий опорний елемент і ставимо його в кінець
    # Це захищає від найгіршого часу виконання O(N^2) на тестах із вже відсортованими даними
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def main():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    # Створюємо масив зчитаних чисел
    arr = [int(x) for x in input_data[1:n + 1]]

    # sys.setrecursionlimit(2000)

    if n > 1:
        quick_sort(arr, 0, n - 1)

    print(*arr)


if __name__ == '__main__':
    main()