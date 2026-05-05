from math import log2, ceil, gcd


class SegmentTree:
    def __init__(self, array):

        k = len(array)
        n = 1 << ceil(log2(k))

        self.items = [0]*n + array + [0]*(n - k)

        for i in range(n - 1,0 ,-1):
            self.items[i] = gcd(self.items[2 * i], self.items[2 * i + 1])

        self.size = n

    def update(self,pos, new_value):

        pos += self.size

        self.items[pos] = new_value
        while pos > 1:
            pos //= 2
            self.items[pos] = gcd(self.items[2 * pos], self.items[2 * pos + 1])

    def query_gcd(self, from_idx, to_idx):
        left = from_idx + self.size
        right = to_idx + self.size
        res = 0

        while left <= right:
            if left % 2 == 1:
                res = gcd(res, self.items[left])
                left += 1
            if right % 2 == 0:
                res = gcd(res, self.items[right])
                right -= 1

            left //= 2
            right //= 2

        return res


if __name__ == "__main__":

    with open("input.txt") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        q = int(f.readline())
        tree = SegmentTree(array)
        for _ in range(q):
            cmd,x,y = f.readline().split()

            x = int(x)
            y = int(y)

            if cmd == "2":
                tree.update(x - 1,y)
            elif cmd == "1":
                print(tree.query_gcd(x - 1, y - 1))
