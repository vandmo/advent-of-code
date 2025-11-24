INPUT = "389125467"

input = [int(n) for n in INPUT]


def move(links, current_cup, MAX):
    a, b, c = (
        links[current_cup],
        links[links[current_cup]],
        links[links[links[current_cup]]],
    )
    links[current_cup] = links[c]
    destination = current_cup - 1
    while True:
        if destination < 1:
            destination = MAX
        if destination != a and destination != b and destination != c:
            break
        destination -= 1
    p = links[destination]
    links[destination] = a
    links[c] = p
    return links[current_cup]


def part1():
    links = dict()

    for i in range(len(input) - 1):
        links[input[i]] = input[i + 1]
    start = input[0]
    links[input[-1]] = start

    def cups():
        cups = list()
        c = 1
        while True:
            cups.append(c)
            c = links[c]
            if c == 1:
                break
        return cups

    current = start
    for _ in range(100):
        current = move(links, current, 9)
    return "".join(str(n) for n in cups()[1:])


def part2():
    links = dict()

    for i in range(len(input) - 1):
        links[input[i]] = input[i + 1]
    start = input[0]
    links[input[-1]] = 10
    for i in range(10, 1_000_000):
        links[i] = i + 1
    links[1_000_000] = start
    current = start
    for _ in range(10_000_000):
        current = move(links, current, 1_000_000)
    return links[1] * links[links[1]]


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
