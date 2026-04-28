class SimpleHeap:

    def __init__(self):
        self._items = []

    def leftChild(self, idx: int) -> int:
        return 2 * idx + 1

    def rightChild(self, idx: int) -> int:
        return 2 * idx + 2


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    heap = SimpleHeap()
    heap._items = arr

    is_heap = True

    for i in range(n // 2):
        left = heap.leftChild(i)
        right = heap.rightChild(i)

        if left < n and heap._items[i] > heap._items[left]:
            is_heap = False
            break

        if right < n and heap._items[i] > heap._items[right]:
            is_heap = False
            break

    print("YES" if is_heap else "NO")