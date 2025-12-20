INPUT = "......^^^^^^......"


def next_row(row):
    result = ""
    pr = f".{row}."
    for i in range(1, len(pr) - 1):
        s = pr[i - 1 : i + 2]
        if s in ["^^.", ".^^", "^..", "..^"]:
            result += "^"
        else:
            result += "."
    return result


def solve(n):
    row = INPUT
    cnt = 0
    for _ in range(n):
        cnt += row.count(".")
        row = next_row(row)
    return cnt


print("ANSWER PART 1:", solve(40))
print("ANSWER PART 2:", solve(400_000))
