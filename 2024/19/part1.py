with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

patterns = lines[0].split(", ")
lines = lines[1:]


def canmake(design):
    if design == "":
        return True
    for pattern in patterns:
        if design.startswith(pattern) and canmake(design[len(pattern) :]):
            return True
    return False


print(sum(1 for design in lines if canmake(design)))
