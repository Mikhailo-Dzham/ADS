import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    sh_weights = list(map(int, data[2:2 + n]))
    m_weights = list(map(int, data[2 + n:2 + n + m]))
    if sum(m_weights) > 1000_00:
        a = 1/0

    states = {0: {0}}
    for w in m_weights:
        new_states = {}
        for diff, side_sums in states.items():
            new_states.setdefault(diff, set()).update(side_sums)
            new_states.setdefault(diff + w, set()).update({s + w for s in side_sums})
            new_states.setdefault(diff - w, set()).update(side_sums)
        states = new_states

    possible_one_side = states.get(0, {0})
    final_results = set()
    for s in sh_weights:
        for m_sum in possible_one_side:
            final_results.add(s + 2 * m_sum)

    for val in sorted(final_results):
        print(val)


if __name__ == "__main__":
    solve()