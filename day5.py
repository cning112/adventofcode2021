import numpy as np


def get_data():
    with open("day5.txt") as fp:
        lines = fp.read().splitlines()
    ans = []
    for line in lines:
        s = line.split(" ")
        x1, y1 = s[0].split(",")
        x2, y2 = s[-1].split(",")
        ans.append((int(x1), int(y1), int(x2), int(y2)))
    return ans


def part1(data):
    M = max(max(x[0], x[2]) for x in data) + 1
    N = max(max(x[1], x[3]) for x in data) + 1

    array = np.zeros((M, N))

    for x1, y1, x2, y2 in data:
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            array[x1, y1 : y2 + 1] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            array[x1 : x2 + 1, y1] += 1

    return np.count_nonzero(array >= 2)


def part2(data):
    M = max(max(x[0], x[2]) for x in data) + 1
    N = max(max(x[1], x[3]) for x in data) + 1

    array = np.zeros((M, N))

    for x1, y1, x2, y2 in data:
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            array[x1, y1 : y2 + 1] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            array[x1 : x2 + 1, y1] += 1
        else:
            if (x1 < x2) == (y1 < y2):
                x1, x2 = min(x1, x2), max(x1, x2)
                y1, y2 = min(y1, y2), max(y1, y2)
                for i in range(0, x2 - x1+1):
                    array[x1 + i, y1 + i] += 1
            else:
                x1, x2 = min(x1, x2), max(x1, x2)
                y1, y2 = min(y1, y2), max(y1, y2)
                for i in range(0, x2 - x1+1):
                    array[x1 + i, y2 - i] += 1

    return np.count_nonzero(array >= 2)


if __name__ == "__main__":
    data = get_data()
    print("part 1 ", part1(data))
    print("part 2 ", part2(data))
