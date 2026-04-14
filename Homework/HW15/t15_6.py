import sys

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 #зберігаємо довжину для швидкого обчислення остачі

    def AddToTail(self, val: int) -> None:
        new_node = Node(val)
        self.length += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        # Базові випадки
        if self.length <= 1 or k == 0:
            return

        #відкидаємо зайві повні оберти
        k = k % self.length
        if k == 0:
            return

        # Знаходимо новий хвіст списку.
        # При зсуві на k позицій вправо, новий хвіст буде на (length - k - 1)
        steps_to_new_tail = self.length - k - 1
        new_tail = self.head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next

        # З"єднуємо старий хвіст з старою головою
        self.tail.next = self.head

        # Оновлюємо посилання
        self.head = new_head
        self.tail = new_tail
        self.tail.next = None  # Розриваємо кільце на новому хвості

    def Print(self) -> None:
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


def main():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    elements = input_data[1:n + 1]

    my_list = List()

    for item in elements:
        my_list.AddToTail(int(item))

    #Всі наступні числа у вводі то запити k на обертання
    k_queries = input_data[n + 1:]

    # Виконуємо обертання та виводимо результат для кожного k
    for k_str in k_queries:
        k = int(k_str)
        my_list.RotateRight(k)
        my_list.Print()


if __name__ == '__main__':
    main()