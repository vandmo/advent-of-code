from collections import Counter

lines = [line.strip() for line in open("input.txt")]
column_counters = [Counter(column).most_common() for column in zip(*lines)]


def part1():
    return "".join([col_counter[0][0] for col_counter in column_counters])


def part2():
    return "".join([col_counter[-1][0] for col_counter in column_counters])


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
