INPUT = [line.strip() for line in open("input.txt")]


def part1():
    """
    1 2 3
    4 5 6
    7 8 9
    """

    D = {
        "1R": 2,
        "1D": 4,
        "2L": 1,
        "2R": 3,
        "2D": 5,
        "3D": 6,
        "3L": 2,
        "4U": 1,
        "4R": 5,
        "4D": 7,
        "5U": 2,
        "5D": 8,
        "5L": 4,
        "5R": 6,
        "6U": 3,
        "6D": 9,
        "6L": 5,
        "7U": 4,
        "7R": 8,
        "8L": 7,
        "8U": 5,
        "8R": 9,
        "9U": 6,
        "9L": 8,
    }

    at = 5
    answer = ""
    for line in INPUT:
        for c in line:
            v = D.get(f"{at}{c}")
            if v is not None:
                at = v
        answer += str(at)
    return answer


def part2():
    PAD = """
..1
.234
56789
.ABC
..D
""".split()

    INSTR = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

    posx, posy = 0, 2
    answer = ""
    for line in INPUT:
        for c in line:
            dx, dy = INSTR[c]
            npx = posx + dx
            npy = posy + dy
            if (
                npy >= 0
                and npy < len(PAD)
                and npx >= 0
                and npx < len(PAD[npy])
                and PAD[npy][npx] != "."
            ):
                posx, posy = npx, npy
        answer += PAD[posy][posx]
    return answer


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
