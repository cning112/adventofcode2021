import numpy as np


def get_data():
    with open("day4.txt") as fp:
        lines = fp.read().splitlines()

    numbers = [int(x) for x in lines[0].split(",")]

    boards = []
    tmp = []
    for line in lines[1:]:
        if line:
            tmp.append([int(x) for x in line.split()])
        if len(tmp) == 5:
            boards.append(np.asarray(tmp))
            tmp = []
    return numbers, boards


def part_1():
    numbers, boards = get_data()

    for num in numbers:
        for i in range(len(boards)):
            b = boards[i]
            b = np.where(b == num, -1, b)

            # any row
            test = b == -1
            if (
                np.any(np.all(test, axis=0))
                or np.any(np.all(test, axis=1))
                or np.all(np.diagonal(test))
                or np.all(np.diagonal(np.fliplr(test)))
            ):
                sum_ = np.sum(np.where(b == -1, 0, b))
                return sum_ * num

            boards[i] = b


def part_2():
    numbers, boards = get_data()

    for num in numbers:
        new_boards = []
        for i in range(len(boards)):
            b = boards[i]
            b = np.where(b == num, -1, b)

            # any row
            test = b == -1
            if (
                np.any(np.all(test, axis=0))
                or np.any(np.all(test, axis=1))
                or np.all(np.diagonal(test))
                or np.all(np.diagonal(np.fliplr(test)))
            ):
                if len(boards) == 1:
                    sum_ = np.sum(np.where(b == -1, 0, b))
                    return sum_ * num
            else:
                new_boards.append(b)
        boards = new_boards


if __name__ == "__main__":
    print("part 1", part_1())
    print("part 2", part_2())
