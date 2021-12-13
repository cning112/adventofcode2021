from typing import Tuple, List, Iterable


def get_data() -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    with open("day13.txt") as fp:
        lines = fp.read().splitlines()

    marks = []
    instructions = []

    i = 0
    while lines[i]:
        x, y = lines[i].split(",")
        marks.append((int(x), int(y)))
        i += 1

    i += 1
    while i < len(lines):
        axis, idx = lines[i].rsplit(maxsplit=1)[-1].split("=")
        instructions.append((axis, int(idx)))
        i += 1

    return marks, instructions


def part1(marks: Iterable[Tuple[int, int]], instructions: Iterable[Tuple[str, int]]):
    for axis, idx in instructions:
        ans = set()

        def new_idx(i):
            return idx - abs(idx - i)

        if axis == "x":
            for x, y in marks:
                if x != idx:
                    ans.add((new_idx(x), y))
        elif axis == "y":
            for x, y in marks:
                if y != idx:
                    ans.add((x, new_idx(y)))
        marks = ans

    return marks


def part2(marks: Iterable[Tuple[int, int]], instructions: Iterable[Tuple[str, int]]):
    marks = part1(marks, instructions)
    M, N = max(m[0] for m in marks), max(m[1] for m in marks)

    arr = [["."] * (M + 1) for _ in range(N + 1)]

    for x, y in marks:
        arr[y][x] = "#"

    for line in arr:
        print("".join(line))


if __name__ == "__main__":
    marks, instructions = get_data()
    print("part1", len(part1(marks, instructions[:1])))
    print("part2:", part2(marks, instructions))
