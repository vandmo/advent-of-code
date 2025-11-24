from collections import defaultdict

input = [line.strip() for line in open("input.txt")]


def coords(s):
    start, end = s.split(" through ")
    start = tuple(map(int, start.split(",")))
    end = tuple(map(int, end.split(",")))
    for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            yield x, y


def part1():
    lights = defaultdict(lambda: False)

    for line in input:
        if line.startswith("turn on "):
            for coord in coords(line[len("turn on ") :]):
                lights[coord] = True
        elif line.startswith("turn off "):
            for coord in coords(line[len("turn off ") :]):
                lights[coord] = False
        elif line.startswith("toggle "):
            for coord in coords(line[len("toggle ") :]):
                lights[coord] = not lights[coord]
        else:
            assert False

    return sum(1 for v in lights.values() if v)


def part2():
    lights = defaultdict(lambda: 0)
    for line in input:
        if line.startswith("turn on "):
            for coord in coords(line[len("turn on ") :]):
                lights[coord] += 1
        elif line.startswith("turn off "):
            for coord in coords(line[len("turn off ") :]):
                lights[coord] -= 1
                if lights[coord] < 0:
                    lights[coord] = 0
        elif line.startswith("toggle "):
            for coord in coords(line[len("toggle ") :]):
                lights[coord] += 2
        else:
            assert False

    return sum(v for v in lights.values())


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
