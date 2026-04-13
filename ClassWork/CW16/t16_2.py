from collections import deque


class Tree:

    def __init__(self,key,parent = None):
        self.key = key
        self.parent = parent
        self.children: list[Tree] = []
        self.search_method = self.dfs_stack

    def dfs(self, key):
        if self.key == key:
            return self
        for child in self.children:
            node = child.dfs(key)
            if node is not None:
                return node

    def dfs_stack(self,key):
        stack = [self]
        while stack:
            node = stack.pop()
            if node.key == key:
                return node

            for child in node.children:
                stack.append(child)

    def bfs(self, key):
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            if node.key == key:
                return node
            for child in node.children:
                queue.append(child)

    def add(self,parent_key,key):
        parent = self.search_method(parent_key)
        node = Tree(key, parent)
        parent.children.append(node)


    def get(self,a,b):
        node = self.search_method(a)
        came_from = None
        while node is not None:
            if node.key == b:
                return node.key
            for child in node.children:
                if child is not came_from and  child.search_method(b) is not None:
                    return node.key

            came_from = node
            node = node.parent

    def execute(self,command):
        method, *args = command.split()
        method = method.lower()
        args = map(int, args)
        return getattr(self,method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        tree = Tree(1)
        n = int(f.readline().strip())
        for _ in range(n):
            line = f.readline().strip()
            res = tree.execute(line)
            if res is not None:
                print(res)