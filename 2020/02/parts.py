def isvalid_part1(line):
    rule, password = line.split(":")
    maxmin, letter = rule.split(" ")
    lower, upper = [int(n) for n in maxmin.split("-")]
    password = password.strip()
    occurences = sum(1 for c in password if c == letter)
    return occurences >= lower and occurences <= upper


def isvalid_part2(line):
    rule, password = line.split(":")
    maxmin, letter = rule.split(" ")
    password = password.strip()
    assert len(letter) == 1
    pos1, pos2 = map(lambda x: int(x) - 1, maxmin.split("-"))
    if password[pos1] == letter:
        if password[pos2] == letter:
            return False
        else:
            return True
    else:
        return password[pos2] == letter


lines = [line.strip() for line in open("input.txt")]
print("ANSWER PART 1:", sum(isvalid_part1(line) for line in lines))
print("ANSWER PART 2:", sum(isvalid_part2(line) for line in lines))
