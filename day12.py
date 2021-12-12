from collections import defaultdict


def get_data():
    with open("day12.txt") as fp:
        return [line.split("-") for line in fp.read().splitlines()]


class Node:
    def __init__(self, name):
        self.name = name
        self.nodes = []


def part1(data, *, max_visit=1):
    nodes = defaultdict(list)
    for a, b in data:
        nodes[a].append(b)
        nodes[b].append(a)

    visited = defaultdict(int)
    ans = 0

    def dfs(t):
        if t == "end":
            nonlocal ans
            ans += 1
            return

        for name in nodes[t]:
            if name == "start" or (name[0].islower() and visited[name] >= max_visit):
                continue

            visited[name] += 1
            dfs(name)
            visited[name] -= 1

    visited["start"] += 1
    dfs("start")
    return ans


def part2(data):
    nodes = defaultdict(list)
    for a, b in data:
        nodes[a].append(b)
        nodes[b].append(a)

    visited = defaultdict(int)
    visited_twice = False
    ans = 0

    def dfs(t):
        if t == "end":
            nonlocal ans
            ans += 1
            return

        nonlocal visited_twice
        twice = False

        for name in nodes[t]:
            if name == "start":
                continue

            if name[0].islower() and visited[name] > 0:
                if visited_twice:
                    continue
                else:
                    twice = True
                    visited_twice = True

            visited[name] += 1
            dfs(name)
            visited[name] -= 1
            if twice:
                visited_twice = False

    visited["start"] += 1
    dfs("start")
    return ans


if __name__ == "__main__":
    data = get_data()
    print("part1", part1(data, max_visit=1))
    print("part2", part2(data))
