class Stack:

    def __init__(self, a=100):
        self._items = [0 for _ in range(a)]
        self.cur = 0

    def push(self, item): #Додати
        self._items[self.cur] = item
        self.cur+=1
        return "ok"

    def pop(self): #Забрати
        self.cur -= 1
        return self._items[self.cur]

    def back(self): #Назаднутись
        return self._items[self.cur -1]

    def size(self):
        return self.cur

    def clear(self):
        self.cur = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command: str):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break