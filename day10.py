def get_data():
    with open("day10.txt") as fp:
        return fp.read().splitlines()


opens = {"(", "{", "<", "["}
ends = {"}": "{", ")": "(", ">": "<", "]": "["}


def part1(data):
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    ans = 0
    for l in data:
        stack = []
        for c in l:
            if c in opens:
                stack.append(c)
            else:
                if not stack or stack[-1] != ends[c]:
                    ans += points[c]
                    break
                else:
                    stack.pop()
    return ans


def part2(data):
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    scores = []
    for line in data:
        stack = []
        for c in line:
            if c in opens:
                stack.append(c)
            else:
                if not stack or stack[-1] != ends[c]:
                    break
                else:
                    stack.pop()
        else:
            s = 0
            while stack:
                s = 5 * s + points[stack.pop()]
            # or
            # s = int(''.join(map(lambda c: str(points[c]), stack[::-1])), 5)

            scores.append(s)

    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    data = get_data()
    print("part1", part1(data))
    print("part2", part2(data))
