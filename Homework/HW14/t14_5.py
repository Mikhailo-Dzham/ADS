import sys


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
        self.__init__()  #просто переініціалізовуємо і у нас новенька черга
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command: str):
        method, *args = command.split()
        func = getattr(self, method)
        return func(*args)

if __name__ == '__main__':
    queue = Queue()

    for line in sys.stdin:
        command = line.strip()
        if not command:
            continue

        result = queue.execute(command)
        print(result)

        if result == "bye":
            break