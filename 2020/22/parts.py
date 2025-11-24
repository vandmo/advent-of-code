p1 = []
p2 = []
current = None

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    if line.startswith("Player 1"):
        current = p1
    elif line.startswith("Player 2"):
        current = p2
    else:
        assert current is not None
        current.append(int(line))

p1 = tuple(p1)
p2 = tuple(p2)


def part1(p1, p2):
    def play(p1, p2):
        while p1 and p2:
            v1, *p1 = p1
            v2, *p2 = p2
            p1 = tuple(p1)
            p2 = tuple(p2)
            if v1 > v2:
                p1 += tuple([v1, v2])
            else:
                assert v2 > v1
                p2 += tuple([v2, v1])
        return p1, p2

    p1, p2 = play(p1, p2)
    winner = p1 if p1 else p2
    return sum((i + 1) * v for i, v in enumerate(reversed(winner)))


def part2(p1, p2):
    def play(p1, p2):
        prevs = set()
        while p1 and p2:
            if (p1, p2) in prevs:
                return p1, []
            prevs.add((p1, p2))
            v1, *p1 = p1
            v2, *p2 = p2
            p1 = tuple(p1)
            p2 = tuple(p2)
            if len(p1) >= v1 and len(p2) >= v2:
                r1, r2 = play(p1[:v1], p2[:v2])
                if r1:
                    p1 += tuple([v1, v2])
                else:
                    assert r2
                    p2 += tuple([v2, v1])
            else:
                if v1 > v2:
                    p1 += tuple([v1, v2])
                else:
                    assert v2 > v1
                    p2 += tuple([v2, v1])
        return p1, p2

    p1, p2 = play(p1, p2)
    winner = p1 if p1 else p2
    return sum((i + 1) * v for i, v in enumerate(reversed(winner)))


print("ANSWER PART 1:", part1(p1, p2))
print("ANSWER PART 2:", part2(p1, p2))
