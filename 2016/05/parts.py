import hashlib
from itertools import count

INPUT = "ffykfhsq"


def part1():
    pwd = ""

    for i in count():
        m = hashlib.md5()
        m.update(f"{INPUT}{i}".encode())
        h = m.hexdigest()
        if h.startswith("00000"):
            pwd += h[5]
            if len(pwd) >= 8:
                return pwd
    assert False


def part2():
    pwd = ["_"] * 8

    for i in count():
        m = hashlib.md5()
        m.update(f"{INPUT}{i}".encode())
        h = m.hexdigest()
        if h.startswith("00000"):
            pos = int(h[5], 16)
            if pos > 7:
                continue
            if pwd[pos] == "_":
                pwd[pos] = h[6]
            pwds = "".join(pwd)
            print(f"\rDecrypting:    {pwds}", end="")
            if "_" not in pwds:
                print(f"\rANSWER PART 2: {pwds}")
                break


print("ANSWER PART 1:", part1())

part2()
