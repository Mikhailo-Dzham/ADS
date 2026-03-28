import sys

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def empty(self):
        return self._top is None

    def push(self,item):
        node  = Node(item)
        node.next = self._top
        self._top  = node
        self._size += 1
        return "ok"

    def pop(self):
        if self._top is None:
            return ("error")
        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

    def back(self):
        if self._top is None:
            return ("error")
        return self._top.item

    def size(self):
        return self._size


    def clear(self):
        self.__init__()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self,command: str):
        method, *args = command.split()
        func = getattr(self,method)
        return func(*args)

#######################################

testcase = sys.stdin.read().split("\n")

my_stack = Stack()

for case in testcase:
    func = case.split()
    result = my_stack.execute(case)
    print(result)
    if case == "exit":
        break

