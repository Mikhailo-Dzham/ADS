import sys


class Tree:
    def __init__(self):
        self.fee = 0
        self.children = []

    def get_min_cost(self):
        if not self.children:
            return self.fee

        return self.fee + min(child.get_min_cost() for child in self.children)


def solve():
    input_data = sys.stdin.read().split()

    n = int(input_data[0])

    nodes = [Tree() for _ in range(n + 1)]

    idx = 1
    for i in range(1, n + 1):
        fee = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2

        nodes[i].fee = fee

        for _ in range(k):
            child_id = int(input_data[idx])
            nodes[i].children.append(nodes[child_id])
            idx += 1

    print(nodes[1].get_min_cost())


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    solve()