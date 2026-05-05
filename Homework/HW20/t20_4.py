from math import log2, ceil, gcd, lcm


class SegmentTree:

    def __init__(self, array):

        k = len(array)
        n = 1 << ceil(log2(k))

        # (gcd, lcm) Будемо зберігати одночасно НСД та НСК
        self.items = [(0, 1)] * n + [(x, x) for x in array] + [(0, 1)] * (n - k)

        for i in range(n - 1, 0, -1):
            left = self.items[2 * i]
            right = self.items[2 * i + 1]

            g = gcd(left[0], right[0])
            l = lcm(left[1], right[1])

            self.items[i] = (g, l)

        self.size = n

    def update(self, pos, new_value):

        pos += self.size
        self.items[pos] = (new_value, new_value)

        while pos > 1:
            pos //= 2

            left = self.items[2 * pos]
            right = self.items[2 * pos + 1]

            g = gcd(left[0], right[0])
            l = lcm(left[1], right[1])

            self.items[pos] = (g, l)

    def query_gcd(self, from_idx, to_idx):

        left = from_idx + self.size
        right = to_idx + self.size
        res = 0

        while left <= right:
            if left % 2 == 1:
                res = gcd(res, self.items[left][0])
                left += 1
            if right % 2 == 0:
                res = gcd(res, self.items[right][0])
                right -= 1

            left //= 2
            right //= 2

        return res

    def query_lcm(self, from_idx, to_idx):

        left = from_idx + self.size
        right = to_idx + self.size
        res = 1

        while left <= right:
            if left % 2 == 1:
                res = lcm(res, self.items[left][1])
                left += 1
            if right % 2 == 0:
                res = lcm(res, self.items[right][1])
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
                lc, gc = tree.query_lcm(x - 1, y - 1), tree.query_gcd(x - 1, y - 1)
                if lc < gc:
                    print("wins")
                else:
                    print("draw")





