import sys


def binary_search_exists(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    m = int(input_data[n + 1])
    queries = [int(x) for x in input_data[n + 2: n + 2 + m]]

    for q in queries:
        if binary_search_exists(arr, q):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    solve()