import json

input = json.load(open("input.txt"))


def solve(j, allow_red):
    if isinstance(j, list):
        return sum(solve(e, allow_red) for e in j)
    elif isinstance(j, dict):
        if not allow_red and "red" in j.values():
            return 0
        return sum(solve(e, allow_red) for _, e in j.items())
    elif isinstance(j, int):
        return j
    elif isinstance(j, str):
        return 0
    else:
        assert False


print("ANSWER PART 1:", solve(input, True))
print("ANSWER PART 2:", solve(input, False))
