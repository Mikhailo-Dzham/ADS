import sys

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  #колишня голова стає новим хвостом

        while current is not None:
            next_node = current.next  #запам'ятовуємо наступний вузол
            current.next = prev  #розвертаємо вказівник поточного вузла
            prev = current  #зсуваєм prev на поточний вузол
            current = next_node  #переходимо до наступного вузла

        self.head = prev

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        print()


def main():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])
    elements = input_data[1:n + 1]

    linked_list = LinkedList()

    for item in elements:
        linked_list.append(int(item))

    linked_list.print_list()

    linked_list.reverse()
    linked_list.print_list()


if __name__ == '__main__':
    main()