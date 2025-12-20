from itertools import permutations


def rotate(s, steps):
    if steps < 0:
        i = (len(s) - steps) % len(s)
        return f"{s[i:]}{s[:i]}"
    i = steps % len(s)
    return f"{s[-i:]}{s[:-i]}"


def scramble(password, operations: list[str]):
    for operation in operations:
        if operation.startswith("swap position "):
            operation = operation[len("swap position ") :]
            l, r = sorted([int(n) for n in operation.split(" with position ")])
            password = f"{password[0:l]}{password[r]}{password[l+1:r]}{password[l]}{password[r+1:]}"
        elif operation.startswith("swap letter "):
            operation = operation[len("swap letter ") :]
            l, r = operation.split(" with letter ")
            password = password.replace(l, "!")
            password = password.replace(r, l)
            password = password.replace("!", r)
        elif operation.startswith("reverse positions "):
            operation = operation[len("reverse positions ") :]
            l, r = sorted([int(n) for n in operation.split(" through ")])
            password = f"{password[:l]}{password[l:r+1][::-1]}{password[r+1:]}"
        elif operation.startswith("rotate left "):
            operation = operation[len("rotate left ") :]
            steps = int(operation[: -len(" step")])
            password = rotate(password, -steps)
        elif operation.startswith("rotate right "):
            operation = operation[len("rotate right ") :]
            steps = int(operation[: -len(" step")])
            password = rotate(password, steps)
        elif operation.startswith("move position "):
            operation = operation[len("move position ") :]
            l, r = [int(n) for n in operation.split(" to position ")]
            pl = list(password)
            c = pl[l]
            del pl[l]
            pl.insert(r, c)
            password = "".join(pl)
        elif operation.startswith("rotate based on position of letter "):
            letter = operation[len("rotate based on position of letter ") :]
            i = password.index(letter) + 1
            if i > 4:
                i += 1
            password = rotate(password, i)
    return password


operations = [line.strip() for line in open("input.txt")]


def part1():
    return scramble("abcdefgh", operations)


def part2():
    for s in permutations("fbgdceah"):
        s = "".join(s)
        if scramble(s, operations) == "fbgdceah":
            return s


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
