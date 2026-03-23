import sys


def find_partitions(target):
    results = []

    def backtrack(remaining, min_val, path):
        if remaining == 0:
            if len(path) > 1:
                results.append("+".join(map(str, path)))
            return

        for i in range(min_val, remaining + 1):
            path.append(i)
            backtrack(remaining - i, i, path)
            path.pop()

    backtrack(target, 1, [])
    return results


try:
    line = sys.stdin.readline()
    if line:
        n = int(line.strip())
        partitions = find_partitions(n)
        for p in partitions:
            print(p)
except EOFError:
    pass