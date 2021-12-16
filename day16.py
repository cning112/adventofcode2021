import operator
from functools import reduce
from io import BytesIO


def get_data() -> str:
    with open("day16.txt") as fp:
        return fp.readline()


class Packet:
    def __init__(self, f):
        self._f = f
        self.children = []
        self.version = int(self._read(3), 2)
        self.type_id = int(self._read(3), 2)
        if self.type_id == 4:  # literal
            self.value = 0
            while True:
                n = self._read(5).decode()
                self.value = (self.value << 4) + int(n[1:], 2)
                if n[0] == "0":
                    break
        else:  # operator
            length_type_id = self._read(1)
            if length_type_id == b"0":  # 15 bits
                length = int(self._read(15), 2)
                init_pos = self._f.tell()
                while self._f.tell() < init_pos + length:
                    self.children.append(Packet(self._f))
            else:
                length = int(self._read(11), 2)
                while length:
                    self.children.append(Packet(self._f))
                    length -= 1

    def _read(self, n):
        c = self._f.read(n)
        # print('read: ', c)
        return c

    @property
    def result(self):
        if self.type_id == 4:
            return self.value

        op = {
            0: operator.add,
            1: operator.mul,
            2: min,
            3: max,
            5: operator.gt,
            6: operator.lt,
            7: operator.eq,
        }[self.type_id]
        return int(reduce(op, (c.result for c in self.children)))


def parse(data):
    bytes_data = "".join(bin(int(c, 16))[2:].zfill(4) for c in data)
    bio = BytesIO(bytes_data.encode())
    packet = Packet(bio)
    return packet


def part1(data):
    packet = parse(data)

    ans = 0
    ps = [packet]
    while ps:
        next_ps = []
        for p in ps:
            ans += p.version
            next_ps.extend(p.children)
        ps = next_ps
    return ans


def part2(data):
    packet = parse(data)
    return packet.result


if __name__ == "__main__":
    data = get_data()
    print("part1", part1(data))
    print("part2", part2(data))
