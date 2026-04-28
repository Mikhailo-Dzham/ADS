import sys

class Heap:

    def __init__(self):
        self._items = [] # (id, priority)
        self.pos = {} # id -> index

    def insert(self, id, priority):
        self._items.append((id, priority))
        idx = len(self._items) - 1
        self.pos[id] = idx
        self._sift_up(idx)

    def extract(self):
        self.swap(0, len(self._items) - 1)
        item = self._items.pop()
        del self.pos[item[0]]

        if self._items:
            self._sift_down(0)

        return item

    def change(self, id, new_priority):
        idx = self.pos[id]
        old_priority = self._items[idx][1]

        self._items[idx] = (id, new_priority)

        if new_priority > old_priority:
            self._sift_up(idx)
        else:
            self._sift_down(idx)

    def swap(self, i, j):
        self.pos[self._items[i][0]] = j
        self.pos[self._items[j][0]] = i
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self._items[p][1] >= self._items[i][1]:
                break
            self.swap(i, p)
            i = p

    def _sift_down(self, i):
        n = len(self._items)
        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2

            if right < n and self._items[right][1] > self._items[left][1]:
                max_child = right
            else:
                max_child = left

            if self._items[i][1] >= self._items[max_child][1]:
                break

            self.swap(i, max_child)
            i = max_child

if __name__ == '__main__':
    heap = Heap()

    for line in sys.stdin:
        cmd = line.split()

        if cmd[0] == "ADD":
            heap.insert(cmd[1], int(cmd[2]))

        elif cmd[0] == "POP":
            id, priority = heap.extract()
            print(id, priority)

        elif cmd[0] == "CHANGE":
            heap.change(cmd[1], int(cmd[2]))
