import sys


def lower_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        # Основна відмінність від lower_bound:
        # ми йдемо вправо, навіть якщо arr[mid] == target
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    m = int(input_data[n + 1])
    queries = [int(x) for x in input_data[n + 2: n + 2 + m]]

    for q in queries:
        ans = upper_bound(arr, q) - lower_bound(arr, q)
        print(ans)


if __name__ == '__main__':
    solve()