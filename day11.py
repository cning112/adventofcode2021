def get_data():
    with open("day11.txt") as fp:
        return [[int(x) for x in line] for line in fp.read().splitlines()]


def part1(arr, nsteps):
    M, N = len(arr), len(arr[0])

    def inc(i, j):
        if not (0 <= i < M and 0 <= j < N):
            return 0

        arr[i][j] += 1
        if arr[i][j] == 10:
            return (
                1
                + inc(i - 1, j)
                + inc(i + 1, j)
                + inc(i, j - 1)
                + inc(i, j + 1)
                + inc(i - 1, j - 1)
                + inc(i - 1, j + 1)
                + inc(i + 1, j - 1)
                + inc(i + 1, j + 1)
            )
        else:
            return 0

    ans = 0
    for _ in range(nsteps):
        for i in range(M):
            for j in range(N):
                ans += inc(i, j)
        for i in range(M):
            for j in range(N):
                if arr[i][j] > 9:
                    arr[i][j] = 0
    return ans


def part2(arr):
    M, N = len(arr), len(arr[0])

    def inc(i, j):
        if not (0 <= i < M and 0 <= j < N):
            return 0

        arr[i][j] += 1

        if arr[i][j] == 10:
            return (
                1
                + inc(i - 1, j)
                + inc(i + 1, j)
                + inc(i, j - 1)
                + inc(i, j + 1)
                + inc(i - 1, j - 1)
                + inc(i - 1, j + 1)
                + inc(i + 1, j - 1)
                + inc(i + 1, j + 1)
            )
        else:
            return 0

    nstep = 1
    while True:
        cnt = 0
        for i in range(M):
            for j in range(N):
                cnt += inc(i, j)

        if cnt == M * N:
            return nstep

        for i in range(M):
            for j in range(N):
                if arr[i][j] > 9:
                    arr[i][j] = 0

        nstep += 1


if __name__ == "__main__":
    data = get_data()
    print("part1", part1(data, nsteps=100))
    print("part2", part2(get_data()))
