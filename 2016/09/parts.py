INPUT = open("input.txt").read().strip()


def calc(data: str, *, recursive):
    at = 0
    cnt = 0
    while at < len(data):
        c = data[at]
        if c == "(":
            ep = data.index(")", at)
            expr = data[at + 1 : ep]
            f1, f2 = [int(f) for f in expr.split("x")]
            if recursive:
                cnt += calc(data[ep + 1 : ep + f1 + 1], recursive=recursive) * f2
            else:
                cnt += f1 * f2
            at += f1 + ep - at + 1
        else:
            at += 1
            cnt += 1
            if at >= len(data):
                return cnt
    return cnt


print("ANSWER PART 1:", calc(INPUT, recursive=False))
print("ANSWER PART 2:", calc(INPUT, recursive=True))
