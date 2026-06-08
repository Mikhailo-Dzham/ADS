class Heap:

    def __init__(self):
        self._items = [0]

    def insert(self, item):
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

    def extract(self) -> int:
        self.swap(0, len(self._items) - 1)
        item = self._items.pop()
        self._sift_down(0)
        return item

    def swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def _sift_up(self, idx):
        i = idx
        while i > 0:
            parent = self.parent(i)

            if self._items[parent] >= self._items[i]:
                break

            self.swap(i, parent)
            i = parent

    def _sift_down(self, idx):
        i = idx
        while self.leftChild(i) < len(self._items):
            left = self.leftChild(i)
            right = self.rightChild(i)
            if right < len(self._items) and self._items[left] < self._items[right]:
                max_child = right
            else:
                max_child = left

            if self._items[max_child] <= self._items[i]:
                break

            self.swap(i, max_child)
            i = max_child

    def parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def leftChild(self, idx: int) -> int:
        return 2 * idx + 1

    def rightChild(self, idx: int) -> int:
        return 2 * idx + 2


if __name__ == '__main__':
    heap = Heap()
    f = open("input.txt")
    n = int(f.readline())
    for _ in range(n):
        cmd, *args = map(int, f.readline().split())
        if cmd == 0:
            heap.insert(*args)
        elif cmd == 1:
            print(heap.extract())
    f.close()
