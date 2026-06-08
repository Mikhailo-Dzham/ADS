import sys


def get_all_diffs(weights):
    diffs = {0: {0}}
    for w in weights:
        new_diffs = {}
        for d, sums in diffs.items():
            new_diffs.setdefault(d, set()).update(sums)
            new_diffs.setdefault(d + w, set()).update({s + w for s in sums})
            new_diffs.setdefault(d - w, set()).update(sums)
        diffs = new_diffs
    return diffs


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    sh_weights = list(map(int, input_data[2:2 + n]))
    m_weights = list(map(int, input_data[2 + n:2 + n + m]))

    mid = m // 2
    left_part = get_all_diffs(m_weights[:mid])
    right_part = get_all_diffs(m_weights[mid:])

    possible_one_side_sums = set()
    for d1, sums1 in left_part.items():
        target_d2 = -d1
        if target_d2 in right_part:
            sums2 = right_part[target_d2]
            for s1 in sums1:
                for s2 in sums2:
                    possible_one_side_sums.add(s1 + s2)

    final_results = set()
    for sh in sh_weights:
        for m_sum in possible_one_side_sums:
            final_results.add(sh + 2 * m_sum)

    for val in sorted(final_results):
        sys.stdout.write(str(val) + '\n')


if __name__ == "__main__":
    solve()