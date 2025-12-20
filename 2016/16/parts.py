from itertools import batched

INPUT = "10000"


def transform(data: str):
    return data + "0" + data[::-1].replace("1", "x").replace("0", "1").replace("x", "0")


def checksum(data: str):
    result = ""
    for a, b in batched(data, 2):
        if a == b:
            result += "1"
        else:
            result += "0"
    if len(result) % 2 == 1:
        return result
    return checksum(result)


def solve(n):
    data = INPUT
    while len(data) < n:
        data = transform(data)
    return checksum(data[:n])


print("ANSWER PART 1:", solve(272))
print("ANSWER PART 2:", solve(35651584))
