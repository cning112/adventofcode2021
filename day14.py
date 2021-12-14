from collections import Counter, defaultdict
from typing import Tuple, Dict


def get_data() -> Tuple[str, Dict[str, str]]:
    with open("day14.txt") as fp:
        lines = fp.read().splitlines()

    def parse(l):
        a, b = l.split("->")
        return a.strip(), b.strip()

    mapping = dict(parse(line) for line in lines[2:])
    return lines[0], mapping


def count(template: str, mapping: Dict[str, str], steps: int) -> Dict[str, int]:
    pairs = Counter((a + b for a, b in zip(template, template[1:])))

    for _ in range(steps):
        new_pairs = defaultdict(int)
        for p, v in pairs.items():
            c = mapping[p]
            p0, p1 = p[0] + c, c + p[1]
            new_pairs[p0] += v
            new_pairs[p1] += v
        pairs = new_pairs

    cnt = defaultdict(int)
    for p, v in pairs.items():
        cnt[p[0]] += v
    cnt[template[-1]] += 1
    return cnt


def part1(template, mapping):
    cnt = count(template, mapping, 10)
    max_ = max(cnt.values())
    min_ = min(cnt.values())
    return max_ - min_


def part2(template, mapping):
    cnt = count(template, mapping, 40)
    max_ = max(cnt.values())
    min_ = min(cnt.values())
    return max_ - min_


if __name__ == "__main__":
    template, mapping = get_data()
    print("part1", part1(template, mapping))
    print("part2", part2(template, mapping))
