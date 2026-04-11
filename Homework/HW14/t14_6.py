import sys


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def empty(self):
        return self._size == 0

    def push_front(self, item):
        node = Node(item)
        if self.empty():
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1
        return "ok"

    def push_back(self, item):
        node = Node(item)
        if self.empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self.empty():
            return "error"
        item = self._head.item
        self._head = self._head.next
        self._size -= 1

        if self.empty():
            self._tail = None
        else:
            self._head.prev = None  # Відв'язуємо старий елемент

        return item

    def pop_back(self):
        if self.empty():
            return "error"
        item = self._tail.item
        self._tail = self._tail.prev
        self._size -= 1

        if self.empty():
            self._head = None
        else:
            self._tail.next = None  # Відв'язуємо старий елемент

        return item

    def front(self):
        if self.empty():
            return "error"
        return self._head.item

    def back(self):
        if self.empty():
            return "error"
        return self._tail.item

    def size(self):
        return self._size

    def clear(self):
        self.__init__()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command: str):
        method, *args = command.split()
        # Шукаємо метод у класі та викликаємо його з переданими аргументами
        func = getattr(self, method) #Буде підбирати функції за їх текстовою назвою
        return func(*args)


if __name__ == '__main__':
    deque = Deque()

    for line in sys.stdin:
        command = line.strip()

        result = deque.execute(command)
        print(result)

        if result == "bye":
            break