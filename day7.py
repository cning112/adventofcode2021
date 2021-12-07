def get_data():
    with open("day7.txt") as fp:
        return list(map(int, fp.readline().strip().split(",")))


def part1(data):
    from collections import Counter

    cnt = Counter(data)

    def check(x):
        return sum(abs(x - v) * n for v, n in cnt.items())

    return min(check(x) for x in range(0, max(cnt.keys())))


def part2(data):
    from collections import Counter

    cnt = Counter(data)

    def check(x):
        ans = 0
        for v, n in cnt.items():
            if v != x:
                d = abs(x-v)
                ans += n * ((1 + d) * d // 2)
        return ans
    return min(check(x) for x in range(0, max(cnt.keys())))


if __name__ == "__main__":
    data = get_data()

    print("part1", part1(data))
    print("part2", part2(data))
