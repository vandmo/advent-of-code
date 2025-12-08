from itertools import pairwise, product

reds = []
for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    x, y = [int(n) for n in line.split(",")]
    reds.append((x, y))


def part1():
    max_area = 0
    for (x0, y0), (x1, y1) in product(reds, reds):
        xmax = max(x0, x1)
        xmin = min(x0, x1)
        ymax = max(y0, y1)
        ymin = min(y0, y1)
        area = (xmax - xmin + 1) * (ymax - ymin + 1)
        max_area = max(max_area, area)
    return max_area


def part2():

    def check(x0, y0, x1, y1):
        xmax = max(x0, x1)
        xmin = min(x0, x1)
        ymax = max(y0, y1)
        ymin = min(y0, y1)
        for (lp0x, lp0y), (lp1x, lp1y) in pairwise(reds + [reds[0]]):
            if lp0y == lp1y:  # horizontal line
                if lp0y < ymax and lp0y > ymin:
                    lpxmin = min(lp0x, lp1x)
                    lpxmax = max(lp0x, lp1x)
                    if lpxmin < xmax and lpxmax > xmin:
                        return False
            elif lp0x == lp1x:  # vertical line
                if lp0x < xmax and lp0x > xmin:
                    lpymin = min(lp0y, lp1y)
                    lpymax = max(lp0y, lp1y)
                    if lpymin < ymax and lpymax > ymin:
                        return False
            else:
                assert False
        return True

    max_area = 0
    for (x0, y0), (x1, y1) in product(reds, reds):
        if check(x0, y0, x1, y1):
            area = (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1)
            max_area = max(max_area, area)
    return max_area


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
