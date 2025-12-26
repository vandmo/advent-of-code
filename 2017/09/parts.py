def score(data):
    score = 0
    garbage = 0
    level = 0
    state = "group"
    i = 0
    while i < len(data):
        if state == "garbage":
            match data[i]:
                case "!":
                    i += 1
                case ">":
                    state = "group"
                case _:
                    garbage += 1
        else:
            assert state == "group"
            match data[i]:
                case "{":
                    level += 1
                case "<":
                    state = "garbage"
                case "}":
                    score += level
                    level -= 1
        i += 1
    return score, garbage


part1, part2 = score(open("input.txt").read().strip())
print("ANSWER PART 1:", part1)
print("ANSWER PART 2:", part2)
