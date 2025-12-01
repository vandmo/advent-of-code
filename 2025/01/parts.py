def parse(line):
    line = line.strip()
    direction = 1 if line[0] == "R" else -1
    clicks = int(line[1:])
    return direction, clicks


rotations = [parse(line) for line in open("input.txt")]


def part1():
    password = 0
    dial = 50
    for direction, clicks in rotations:
        dial = (dial + (direction * clicks)) % 100
        if dial == 0:
            password += 1
    return password


def part2():
    password = 0
    dial = 50
    for direction, clicks in rotations:
        wholes, rest = divmod(clicks, 100)
        password += wholes
        if dial == 0:
            dial = (dial + (direction * clicks)) % 100
        else:
            dial += rest * direction
            if dial <= 0 or dial > 99:
                password += 1
                dial %= 100
    return password


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
