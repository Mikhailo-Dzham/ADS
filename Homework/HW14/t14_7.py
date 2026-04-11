import sys

#Берем нашу готову чергу
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def empty(self):
        return self._size == 0

    def push(self, item):
        node = Node(item)
        if self.empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self._head.item
        self._head = self._head.next
        self._size -= 1

        # Якщо після видалення черга стала порожньою,
        # хвіст теж треба занулити
        if self.empty():
            self._tail = None

        return item

    def front(self):
        if self.empty():
            return "error"
        return self._head.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command: str):
        method, *args = command.split()
        func = getattr(self, method)
        return func(*args)


def main():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])

    q1 = Queue()
    q2 = Queue()

    # Заповнюємо чергу першого гравця
    for i in range(1, n // 2 + 1):
        q1.push(int(input_data[i]))

    # Заповнюємо чергу другого гравця
    for i in range(n // 2 + 1, n + 1):
        q2.push(int(input_data[i]))

    moves = 0
    MAX_MOVES = 200000

    # Моделюємо гру
    while not q1.empty() and not q2.empty() and moves < MAX_MOVES:
        moves += 1
        c1 = q1.pop()
        c2 = q2.pop()

        # Спец правило 0 перемагає найбільшу карту (n - 1)
        if c1 == 0 and c2 == n - 1:
            q1.push(c1)
            q1.push(c2)
        elif c1 == n - 1 and c2 == 0:
            q2.push(c1)
            q2.push(c2)
        # В інших випадках перемагає більша карта
        elif c1 > c2:
            q1.push(c1)  # Спочатку завжди кладеться карта першого гравця
            q1.push(c2)  # Потім - карта другого гравця
        else:
            q2.push(c1)
            q2.push(c2)

    # Визначаємо переможця або нічию
    if q1.empty():
        print(f"second {moves}")
    elif q2.empty():
        print(f"first {moves}")
    else:
        print("draw")


if __name__ == '__main__':
    main()