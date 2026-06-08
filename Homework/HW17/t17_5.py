import sys


class PathNode:
    def __init__(self, val, min_limit, max_limit):
        self.val = val
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.child = None

    def add_next(self, next_val):
        # Перевіряємо, чи може наступне значення бути правильним нащадком
        # і звужуємо допустимі межі (min_limit, max_limit) для наступних поколінь
        if next_val < self.val:
            if next_val <= self.min_limit:
                return False
            self.child = PathNode(next_val, self.min_limit, self.val)
            return True

        elif next_val > self.val:
            if next_val >= self.max_limit:
                return False
            self.child = PathNode(next_val, self.val, self.max_limit)
            return True

        return False


def solve_468():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    arr = [int(x) for x in input_data]

    # Спочатку дерево не має обмежень по значеннях
    root = PathNode(arr[0], -float('inf'), float('inf'))
    curr = root

    # Намагаємося ланцюжком додати кожен наступний елемент шляху
    for val in arr[1:]:
        if not curr.add_next(val):
            print("NO")
            return
        curr = curr.child

    print("YES")


if __name__ == '__main__':
    sys.setrecursionlimit(50005)
    solve_468()