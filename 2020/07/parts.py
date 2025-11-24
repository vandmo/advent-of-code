from functools import cache

m = {}


def parse(bag: str):
    if bag.startswith("no other bag"):
        return None
    n, rest = bag.split(" ", 1)
    return int(n), rest.split(" bag", 1)[0]


for line in open("input.txt"):
    l, r = line.strip().split(" bags contain ", 1)
    m[l] = list(filter(lambda b: b is not None, (parse(bag) for bag in r.split(", "))))


@cache
def can_have_shiny_gold(bag):
    for _, child in m[bag]:
        if child == "shiny gold" or can_have_shiny_gold(child):
            return True
    return False


@cache
def bags_in(bag):
    return sum(bags_in(child) * count + count for count, child in m[bag])


print("ANSWER PART 1:", sum(1 for v in m if can_have_shiny_gold(v)))
print("ANSWER PART 2:", bags_in("shiny gold"))
