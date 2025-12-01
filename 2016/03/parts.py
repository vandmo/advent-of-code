from itertools import batched


rows = [tuple(int(n) for n in line.split()) for line in open("input.txt")]


def possible(a, b, c):
    return a + b > c and a + c > b and b + c > a


def part1():
    return sum(1 for row in rows if possible(*row))


def part2():
    number_of_possible_triangles = 0
    for three_rows in batched(rows, 3):
        for column in range(3):
            if possible(
                three_rows[0][column], three_rows[1][column], three_rows[2][column]
            ):
                number_of_possible_triangles += 1
    return number_of_possible_triangles


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
