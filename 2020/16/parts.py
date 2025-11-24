from math import prod

fields: dict[str, tuple[tuple[int, int], ...]] = dict()
my_ticket: tuple[int, ...] | None = None
nearby_tickets: list[tuple[int, ...]] = list()


def parse_ticket(line):
    return tuple(int(n) for n in line.split(","))


state = "fields"
for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    if line == "your ticket:":
        state = "my-ticket"
    elif line == "nearby tickets:":
        state = "nearby-tickets"
    else:
        match state:
            case "fields":
                name, ranges_str = line.split(": ")
                ranges = list()
                for _range in ranges_str.split(" or "):
                    lower, upper = [int(v) for v in _range.split("-")]
                    assert upper > lower
                    ranges.append((lower, upper))
                assert name not in fields
                fields[name] = tuple(ranges)
            case "my-ticket":
                my_ticket = parse_ticket(line)
            case "nearby-tickets":
                nearby_tickets.append(parse_ticket(line))

assert my_ticket is not None


def is_valid(v):
    for ranges in fields.values():
        for lower, upper in ranges:
            if v >= lower and v <= upper:
                return True
    return False


valid_tickets = list()
part1 = 0
for ticket in nearby_tickets:
    for v in ticket:
        if not is_valid(v):
            part1 += v
            break
    else:
        valid_tickets.append(ticket)


def can_fit(i, ranges):
    for ticket in valid_tickets:
        v = ticket[i]
        for lower, upper in ranges:
            if v >= lower and v <= upper:
                break
        else:
            return False
    return True


possibilities: dict[str, set[int]] = dict()
for name, ranges in fields.items():
    for i in range(len(my_ticket)):
        if can_fit(i, ranges):
            possibilities.setdefault(name, set()).add(i)


def find_order(
    remaining_names: list[str], remaining_positions: set[int]
) -> list[tuple[str, int]] | None:
    if not remaining_names:
        return list()
    for name in remaining_names:
        next_remaining = remaining_names.copy()
        next_remaining.remove(name)
        for pos in possibilities[name]:
            if pos in remaining_positions:
                next_remaining_positions = remaining_positions.difference([pos])
                next_order = find_order(next_remaining, next_remaining_positions)
                if next_order is not None:
                    return [(name, pos)] + next_order
    return None


names = sorted(possibilities.keys(), key=lambda name: len(possibilities[name]))
order = find_order(names, set().union(*possibilities.values()))
assert order is not None
wanted = [my_ticket[i] for name, i in order if name.startswith("departure")]

print("ANSWER PART 1:", part1)
print("ANSWER PART 2:", prod(wanted))
