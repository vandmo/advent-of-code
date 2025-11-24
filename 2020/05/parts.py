def decode(seat):
    row = seat[:7]
    col = seat[7:]
    rl, rh = 0, 127
    for c in row:
        if c == "F":
            rh = (rl + rh) // 2
        else:
            assert c == "B"
            rl = (rl + rh + 1) // 2
    assert rl == rh
    cl, ch = 0, 7
    for c in col:
        if c == "L":
            ch = (cl + ch) // 2
        else:
            assert c == "R"
            cl = (cl + ch + 1) // 2
    assert cl == ch
    return rl, cl


assert decode("FBFBBFFRLR") == (44, 5)
assert decode("BFFFBBFRRR") == (70, 7)
assert decode("FFFBBBFRRR") == (14, 7)
assert decode("BBFFBBFRLL") == (102, 4)


def idfor(line):
    row, col = decode(line.strip())
    return row * 8 + col


ids = [idfor(line) for line in open("input.txt") if line.strip()]
MAX = max(ids)
MIN = min(ids)

print("ANSWER PART 1:", MAX)
for i in range(MIN, MAX):
    if i not in ids:
        print("ANSWER PART 2:", i)
        break
