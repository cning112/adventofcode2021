from collections import defaultdict
from typing import List


def get_data():
    with open("day8.txt") as fp:
        return fp.read().splitlines()


def part1(data):
    ans = 0
    lengths = {2, 3, 4, 7}
    for line in data:
        digits = line.split('|')[1].split()
        ans += sum(len(d) in lengths for d in digits)
    return ans


def part2(data: List[List[str]]):

    def gen_mapping(ds):
        digits = set(tuple(sorted(d)) for d in ds)
        mapping = {}
        for d in digits:
            if len(d) == 2:
                mapping[d] = 1
                d1 = d
            elif len(d) == 3:
                mapping[d] = 7
                d7 = d
            elif len(d) == 4:
                mapping[d] = 4
                d4 = d
            elif len(d) == 7:
                mapping[d] = 8

        for d in sorted(digits):
            if len(d) == 6:
                if len(set(d) | set(d1)) == 7:
                    mapping[d] = 6
                    d6 = d
                elif len(set(d) | set(d4)) == 7:
                    mapping[d] = 0
                else:
                    mapping[d] = 9

        for d in sorted(digits):
            if len(d) == 5:
                if len(set(d) & set(d7)) == 3:
                    mapping[d] = 3
                elif len(set(d) | set(d6)) == 7:
                    mapping[d] = 2
                else:
                    mapping[d] = 5
        return mapping

    ans = 0
    for line in data:
        ds, digits = line.split('|')
        ds = ds.strip().split()
        digits = digits.strip().split()
        mapping = gen_mapping(ds)
        ans += int(''.join(str(mapping[tuple(sorted(d))]) for d in digits))
    return ans


if __name__ == "__main__":
    data = get_data()
    print("part1 ", part1(data))
    print("part2 ", part2(data))
