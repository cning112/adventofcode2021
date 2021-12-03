if __name__ == "__main__":
    cnt = []
    N = 0
    with open("day3.txt") as fp:
        for line in fp.readlines():
            if not cnt:
                for x in line.strip():
                    cnt.append(int(x))
            else:
                for i, x in enumerate(line.strip()):
                    cnt[i] += int(x)
            N += 1

    gamma = [str(int(x * 2 > N)) for x in cnt]
    gamma = int("".join(gamma), 2)

    epsilon = [str(int(x * 2 < N)) for x in cnt]
    epsilon = int("".join(epsilon), 2)

    ans = gamma * epsilon
    print("part one", ans)


    with open("day3.txt") as fp:
        readings = fp.read().splitlines()

    r1 = readings.copy()
    a, b = [], []
    idx = 0
    while len(r1) > 1:
        cnt = 0
        for l in r1:
            if l[idx] == "0":
                a.append(l)
                cnt -= 1
            else:
                b.append(l)
                cnt += 1

        if cnt >= 0:
            r1 = b
        else:
            r1 = a
        a, b  = [], []
        idx += 1

    o2 = int(r1[0], 2)

    a, b = [], []
    idx = 0
    r2 = readings.copy()
    while len(r2) > 1:
        cnt = 0
        for l in r2:
            if l[idx] == "0":
                a.append(l)
                cnt -= 1
            else:
                b.append(l)
                cnt += 1

        if cnt >= 0:
            r2 = a
        else:
            r2 = b

        a, b  = [], []
        idx += 1
    co2 = int(r2[0], 2)

    print('part two', o2 * co2)