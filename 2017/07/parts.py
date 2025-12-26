from functools import cache
from dataclasses import dataclass


@dataclass
class Program:
    id: str
    weight: int
    children: list[str]


def parse(line):
    splitted = line.split(" -> ")
    if len(splitted) == 1:
        (me,) = splitted
        children = []
    else:
        assert len(splitted) == 2
        me, children = splitted
        children = children.split(", ")
    me, weight = me.split()
    return Program(me, int(weight[1:-1]), children)


parsed = [parse(line.strip()) for line in open("input.txt")]
by_id = {p.id: p for p in parsed}


def find_parent():
    all = set(p.id for p in parsed)
    for program in parsed:
        if len(program.children) > 0:
            for child in program.children:
                all.discard(child)
    return all.pop()


parent = find_parent()


def part2():
    @cache
    def get_size(program_id: str):
        program = by_id[program_id]
        return program.weight + sum(get_size(child) for child in program.children)

    def find_unbalanced(children: list[str]):
        size_to_child = {}
        for child in children:
            size = get_size(child)
            size_to_child.setdefault(size, []).append(child)
        if len(size_to_child) == 1:
            return None
        else:
            assert len(size_to_child) == 2
            a, b = size_to_child.keys()
            if len(size_to_child[b]) == 1:
                p = b
                b = a
                a = p
            wrong_id = size_to_child[a][0]
            wrong = by_id[wrong_id]
            if not wrong.children:
                return wrong.weight + b - a
            nl = find_unbalanced(wrong.children)
            if nl is None:
                return wrong.weight + b - a
            else:
                return nl

    return find_unbalanced(by_id[parent].children)


print("ANSWER PART 1:", parent)
print("ANSWER PART 2:", part2())
