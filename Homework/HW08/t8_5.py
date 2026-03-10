import sys


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    swaps = 0
    # бабл сорт
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    print(swaps)


if __name__ == '__main__':
    solve()