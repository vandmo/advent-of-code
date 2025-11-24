INPUT = "hijklmmn"
BASE = ord("z") - ord("a") + 1
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def tonum(passwd):
    n = 0
    mul = 1
    for c in reversed(passwd):
        n += mul * (ord(c) - ord("a"))
        mul *= BASE
    return n


def tostr(n):
    digits = []
    while True:
        n, r = divmod(n, BASE)
        digits.append(chr(ord("a") + r))
        if n == 0:
            break
    return "".join(reversed(digits))


def isvalid(passwd):
    if any(forbidden in passwd for forbidden in "iol"):
        return False
    for i in range(len(ALPHABET) - 2):
        straight = f"{ALPHABET[i]}{ALPHABET[i+1]}{ALPHABET[i+2]}"
        if straight in passwd:
            break
    else:
        return False
    return sum(1 for letter in ALPHABET if f"{letter}{letter}" in passwd) >= 2


assert tostr(tonum("ghjaabcc")) == "ghjaabcc"


assert not isvalid("hijklmmn")
assert not isvalid("abbceffg")
assert not isvalid("abbcegjk")
assert isvalid("abcdffaa")
assert isvalid("ghjaabcc")


MAXp1 = tonum("zzzzzzzz") + 1


def find_next(current):
    n = current + 1
    while True:
        s = tostr(n).rjust(8, "a")
        if isvalid(s):
            return n
        n = (n + 1) % MAXp1


n = tonum(INPUT)
part1 = find_next(n)
part2 = find_next(part1)
print("ANSWER PART 1:", tostr(part1).rjust(8, "a"))
print("ANSWER PART 2:", tostr(part2).rjust(8, "a"))
