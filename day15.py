from collections import deque
from typing import List


def get_data() -> List[List[int]]:
    with open("day15.txt") as fp:
        lines = fp.read().splitlines()
    return [[int(x) for x in line] for line in lines]


def part1(risk: List[List[int]]):
    M, N = len(risk), len(risk[0])

    acc = [[float("inf")] * N for _ in range(M)]
    acc[0][0] = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dq = deque()
    dq.append((0, 0))

    while dq:
        i, j = dq.popleft()
        curr = acc[i][j]
        for di, dj in directions:
            ii = i + di
            jj = j + dj
            if 0 <= ii < M and 0 <= jj < N:
                new_acc = risk[ii][jj] + curr
                if acc[ii][jj] > new_acc:
                    acc[ii][jj] = new_acc
                    dq.append((ii, jj))

    return acc[-1][-1]


def part2(risk: List[List[int]]):
    M, N = len(risk), len(risk[0])
    MM, NN = M * 5, N * 5

    def risk_val(x, y):
        dx, mx = divmod(x, M)
        dy, my = divmod(y, N)
        v = risk[mx][my] + dx + dy
        if v >= 10:
            v -= 9
        return v

    acc = [[float("inf")] * NN for _ in range(MM)]
    acc[0][0] = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dq = deque()
    dq.append((0, 0))

    while dq:
        i, j = dq.popleft()
        curr = acc[i][j]
        for di, dj in directions:
            ii = i + di
            jj = j + dj
            if 0 <= ii < MM and 0 <= jj < NN:
                new_acc = risk_val(ii, jj) + curr
                if acc[ii][jj] > new_acc:
                    acc[ii][jj] = new_acc
                    dq.append((ii, jj))

    return acc[-1][-1]


if __name__ == "__main__":
    data = get_data()
    print("part1", part1(data))
    print("part2", part2(data))
