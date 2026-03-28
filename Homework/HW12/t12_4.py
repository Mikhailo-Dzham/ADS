import sys

#Чесно, я цей код класса міг просто імпортувати з лабки...
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

##########################################

def solve():
    input_data = sys.stdin.read().split()

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1

        # Обробляємо блоки перестановок для поточного N
        while idx < len(input_data):
            first_val = int(input_data[idx])

            # Якщо рядок 0, блок завершено
            if first_val == 0:
                idx += 1
                print()  #Так як в умові просят чистий рядок після нуля
                break

            # Збираємо цільову послідовність вагонів
            target = [first_val]
            for _ in range(1, n):
                idx += 1
                target.append(int(input_data[idx]))
            idx += 1

            my_stack = Stack()
            current_car = 1
            possible = True

            for t in target:
                # Заганяємо вагони в тупік, поки зверху стека не буде потрібний
                while current_car <= n and (my_stack.empty() or my_stack.back() != t):
                    my_stack.push(current_car)
                    current_car += 1

                # Якщо в топі потрібний вагон - відправляєм його
                if not my_stack.empty() and my_stack.back() == t:
                    my_stack.pop()
                else:
                    # Якщо потрібного так і не знайшли - фейл
                    possible = False

            if possible:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    solve()