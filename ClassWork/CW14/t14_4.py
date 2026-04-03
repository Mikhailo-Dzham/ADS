class Queue():
    def __init__(self, capacity=100_000): # :)))))
        self.data = [0] * capacity
        self.capacity = capacity
        self.first = None
        self.last = None
        self.__size = 0

    def push(self, n):
        if self.first == None:
            self.first = 0
            self.last = 0
        else:
            self.last = (self.last + 1) % self.capacity
        self.data[self.last] = n
        self.__size += 1
        print("ok")

    def pop(self):
        if self.__size == 0:
            print("error")
            return
        val = self.data[self.first]
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = (self.first + 1) % self.capacity
        self.__size -= 1
        print(val)
        return val

    def front(self):
        if self.__size == 0:
            print("error")
            return
        val = self.data[self.first]
        print(val)
        return val

    def size(self):
        print(self.__size)
        return self.__size

    def clear(self):
        self.first = None
        self.last = None
        self.__size = 0
        print("ok")

    def _overflow_check(self):
        pass


def exit():
    print("bye")
    sys.exit(0)


if __name__ == "__main__":
    import sys

    q = Queue()
    DICT = {
        "push": q.push,
        "pop": q.pop,
        "front": q.front,
        "size": q.size,
        "clear": q.clear,
        "exit": exit
    }
    for line in sys.stdin:
        command = line.split()
        if len(command) == 2:
            DICT[command[0]](command[1])
        else:
            DICT[command[0]]()