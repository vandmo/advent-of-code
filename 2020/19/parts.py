import re


type Rule = tuple[tuple[str | int, ...], ...]


def parse_input(filename: str):
    reading_messages = False

    def parse(rule: str) -> Rule:
        parts: list[tuple[str | int, ...]] = list()
        for pps in rule.split("|"):
            ppstr = list()
            for pp in pps.split():
                pp = pp.strip()
                if pp.startswith('"'):
                    assert pp.endswith('"')
                    inside = pp[1:-1]
                    assert inside
                    ppstr.append(inside)
                else:
                    ppstr.append(int(pp))
            parts.append(tuple(ppstr))
        return tuple(parts)

    messages = list()
    rules: dict[int, Rule] = dict()

    for line in open(filename):
        line = line.strip()
        if not line:
            reading_messages = True
        if reading_messages:
            messages.append(line)
        else:
            lhs, rhs = line.split(": ", 1)
            rules[int(lhs)] = parse(rhs)
    return messages, rules


messages, rules = parse_input("input.txt")

longest = max(len(message) for message in messages)


def join_eithers(eithers):
    assert eithers
    if len(eithers) > 1:
        return "(" + "|".join(eithers) + ")"
    return eithers[0]


def make_regexp(rule_id: int, make_regexp):
    rule = rules[rule_id]
    parts = list()
    for either in rule:
        ppstr = ""
        for term in either:
            match term:
                case int(rule_id):
                    ppstr += make_regexp(rule_id)
                case str(literal):
                    ppstr += literal
                case _:
                    assert False
        parts.append(ppstr)
    assert parts
    return join_eithers(parts)


def shortest_match(rule: Rule | str | int):
    match rule:
        case int(rule_id):
            return shortest_match(rules[rule_id])
        case str(literal):
            return len(literal)
        case eithers:
            return min(
                sum(shortest_match(term) for term in either) for either in eithers
            )


def make_regexp_part1(rule_id: int):
    return make_regexp(rule_id, make_regexp_part1)


def make_regexp_part2(rule_id: int):
    if rule_id == 8:  # FROM 8: 42 TO 8: 42 | 42 8
        _42 = make_regexp(42, make_regexp_part2)
        return f"({_42})+"
    elif rule_id == 11:  # FROM 42 31 TO 42 31 | 42 11 31
        # If rule 42 needs to match at least 5 characters and rule 31 needs to match at least 4 characters.
        # Then each repetition of rule 11 is at least 5 + 4 = 9 characters long.
        # If the longest message is 100 characters long that means that rule 11 can only match 100 // 9 = 11 times.
        _31 = make_regexp(31, make_regexp_part2)
        _42 = make_regexp(42, make_regexp_part2)
        max_repetitions = (longest // (shortest_match(31) + shortest_match(42))) + 1
        eithers = [_42 * i + _31 * i for i in range(1, max_repetitions)]
        return join_eithers(eithers)
    else:
        return make_regexp(rule_id, make_regexp_part2)


part1_regexp = re.compile(f"^{make_regexp_part1(0)}$")
part2_regexp = re.compile(f"^{make_regexp_part2(0)}$")

print("ANSWER PART 1:", sum(1 for message in messages if part1_regexp.match(message)))
print("ANSWER PART 2:", sum(1 for message in messages if part2_regexp.match(message)))
