from functools import cache

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

patterns = lines[0].split(", ")
lines = lines[1:]


@cache
def waystomake(design):
    if design == "":
        return 1
    return sum(
        waystomake(design[len(pattern) :])
        for pattern in patterns
        if design.startswith(pattern)
    )


print(sum(waystomake(design) for design in lines))
