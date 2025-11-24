lines = [line.strip() for line in open("input.txt")]


def part1():
    for line in open("input.txt"):
        for line2 in lines:
            if int(line) + int(line2) == 2020:
                return int(line) * int(line2)


def part2():
    for line in open("input.txt"):
        for line2 in lines:
            for line3 in lines:
                if int(line) + int(line2) + int(line3) == 2020:
                    return int(line) * int(line2) * int(line3)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
