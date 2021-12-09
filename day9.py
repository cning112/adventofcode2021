from functools import reduce


def get_data():
    with open("day9.txt") as fp:
        lines = fp.read().splitlines()
        return [list(map(int, line)) for line in lines]


def part1(data):
    import numpy as np

    arr0 = np.array(data)
    arr = np.pad(arr0, ((1, 1), (1, 1)), "constant", constant_values=10)

    cond = arr[1:-1, 1:-1] < arr[2:, 1:-1]
    cond &= arr[1:-1, 1:-1] < arr[:-2, 1:-1]
    cond &= arr[1:-1, 1:-1] < arr[1:-1, 2:]
    cond &= arr[1:-1, 1:-1] < arr[1:-1, :-2]
    return sum(arr0[cond] + 1)


def part2(data):
    import numpy as np

    arr = np.array(data)

    M, N = arr.shape

    arr = np.where(arr == 9, -1, 0)

    def flip(i, j):
        if not (0 <= i < M and 0 <= j < N) or arr[i, j] != 0:
            return 0
        arr[i, j] = -1
        return 1 + flip(i - 1, j) + flip(i + 1, j) + flip(i, j - 1) + flip(i, j + 1)

    areas = []
    for i in range(M):
        for j in range(N):
            cnt = flip(i, j)
            if cnt:
                areas.append(cnt)

    areas.sort()
    return reduce(lambda a, b: a * b, areas[-3:])


if __name__ == "__main__":
    data = get_data()
    print("part1", part1(data))
    print("part2", part2(data))
