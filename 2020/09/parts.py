data = [int(line) for line in open("input.txt")]

L = 25


def isvalid(i):
    v = data[i]
    for j in range(i - L, i):
        for k in range(j, i):
            if data[j] != data[k] and data[j] + data[k] == v:
                return True
    return False


def part1():
    for i in range(L, len(data)):
        if not isvalid(i):
            return data[i]
    assert False


p1 = part1()


def part2():
    for i in range(len(data)):
        s = data[i]
        numbers = set([s])
        for j in range(i + 1, len(data)):
            s += data[j]
            numbers.add(data[j])
            if s == p1:
                return min(numbers) + max(numbers)
            elif s > p1:
                break


print("ANSWER PART 1:", p1)
print("ANSWER PART 2:", part2())
