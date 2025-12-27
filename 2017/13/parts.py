I = {}
for line in open("input.txt"):
    d, r = line.split(":")
    I[int(d)] = int(r)
M = max(I.keys())


def calc_severity(wait):
    severity = 0
    for depth in range(M + 1):
        r = I.get(depth)
        if r is not None:
            m = r * 2 - 2
            if (wait + depth) % m == 0:
                severity += depth * r
    return severity


def is_safe(wait):
    for depth in range(M + 1):
        r = I.get(depth)
        if r is not None:
            m = r * 2 - 2
            if (wait + depth) % m == 0:
                return False
    return True


def part2():
    wait = 0
    while True:
        if is_safe(wait):
            return wait
        wait += 1


print("ANSWER PART 1:", calc_severity(0))
print("ANSWER PART 2:", part2())
