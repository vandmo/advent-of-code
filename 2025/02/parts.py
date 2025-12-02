ranges = [
    tuple(int(n) for n in pairs.strip().split("-"))
    for pairs in open("input.txt").read().split(",")
]


def ids():
    for lower, upper in ranges:
        for id in range(lower, upper + 1):
            yield id


def is_invalid_part1(id: int):
    id_str = str(id)
    length = len(id_str)
    if length % 2 == 1:
        return False
    return id_str[: length // 2] == id_str[length // 2 :]


def is_invalid_part2(id: int):
    id_str = str(id)
    length = len(id_str)
    for sequence_length in range(1, length // 2 + 1):
        if length % sequence_length == 0:
            seen = set()
            for offset in range(length // sequence_length):
                sequence = id_str[
                    offset * sequence_length : offset * sequence_length
                    + sequence_length
                ]
                seen.add(sequence)
            if len(seen) == 1:
                return True
    return False


print("ANSWER PART 1:", sum(id for id in ids() if is_invalid_part1(id)))
print("ANSWER PART 2:", sum(id for id in ids() if is_invalid_part2(id)))
