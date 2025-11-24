def parts():
    part1 = 0
    part2 = 0
    for line in open("input.txt"):
        line = line.strip()
        part1 += len(line) - len(eval(line))
        part2 += 2 + line.count('"') + line.count("\\")
    return part1, part2


part1, part2 = parts()
print("ANSWER PART 1:", part1)
print("ANSWER PART 2:", part2)
