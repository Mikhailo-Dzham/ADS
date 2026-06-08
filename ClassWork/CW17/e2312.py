import sys
sys.setrecursionlimit(2000)

class BinaryTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self,key):
        if key < self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def print(self):

        print(self.key, end=" ")
        if self.left is not None:
            self.left.print()

        if self.right is not None:
            self.right.print()

    def height(self):
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()
        return max(left_height,right_height) + 1

    def find_max(self):
        if self.right is None:            return self.left.kay
        perv = curr = self

        while curr is not None:
            if curr.left is None:
                return perv.key
            return curr.left.key
        perv = curr
        curr = curr.right



if __name__ == "__main__":
    with open("input.txt") as f:
        lst = list(map(int,f.readline().split()))
        if lst[0] != 0:
            tree = BinaryTree(lst[0])

            for i in range(len(lst)):
                if lst[i] == 0:
                    break
                tree.insert(lst[i])

            print(tree.find_max())

        else:
            print(0)