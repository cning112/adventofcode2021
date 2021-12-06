import functools

N = 7
M = 9


def get_data():
    with open("day6.txt") as fp:
        data = [int(x) for x in fp.read().strip().split(",")]
        return data


@functools.lru_cache()
def offspring_total(days):
    if days < N:
        return 0

    ans = days // N
    while days >= N:
        ans += offspring_total(days - M)
        days -= N
    return ans


def part1(data, days):
    return sum(offspring_total(days - x + (N - 1)) for x in data) + len(data)


if __name__ == "__main__":
    data = get_data()
    print("part1 ", part1(data, 80))
    print("part2 ", part1(data, 256))
