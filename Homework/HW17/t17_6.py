import sys


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        # Рекурсивно шукаємо місце для нового вузла
        if key < self.key:
            if self.left is None:
                self.left = BSTNode(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BSTNode(key)
            else:
                self.right.insert(key)

    def preorder(self, result):
        # Прямий обхід: спочатку корінь, потім ліве піддерево, потім праве
        result.append(self.key)
        if self.left:
            self.left.preorder(result)
        if self.right:
            self.right.preorder(result)


def solve_2242():
    input_data = sys.stdin.read().split()
    letters = []

    for token in input_data:
        if token == '*':
            break
        for char in token:
            letters.append(char)

    if not letters:
        return

    # Будуємо дерево з кінця, оскільки останній видалений елемент -- це корінь
    letters.reverse()

    root = BSTNode(letters[0])
    for char in letters[1:]:
        root.insert(char)

    result = []
    root.preorder(result)
    print("".join(result))


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    solve_2242()