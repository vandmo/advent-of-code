from dataclasses import dataclass
from typing import Self


@dataclass
class Range:
    lower: int
    upper: int

    def __init__(self, a: int, b: int):
        self.lower = min(a, b)
        self.upper = max(a, b)

    def length(self):
        return self.upper - self.lower + 1

    def sub(self, other: Self):
        if other.lower <= self.lower and other.upper >= self.upper:
            return []
        if other.upper < self.lower or other.lower > self.upper:
            return [self]
        result = []
        if other.lower > self.lower:
            result.append(Range(self.lower, other.lower - 1))
        if other.upper < self.upper:
            result.append(Range(other.upper + 1, self.upper))
        assert len(result) > 0
        return result


assert Range(5, 10).sub(Range(11, 14)) == [Range(5, 10)]
assert Range(5, 10).sub(Range(1, 4)) == [Range(5, 10)]
assert Range(5, 10).sub(Range(4, 11)) == []
assert Range(5, 10).sub(Range(5, 10)) == []
assert Range(5, 10).sub(Range(6, 8)) == [Range(5, 5), Range(9, 10)]

MAX = 4294967295
allowed = [Range(0, MAX)]


for line in open("input.txt"):
    exclude = Range(*[int(n) for n in line.strip().split("-")])
    new_allowed = []
    for a in allowed:
        new_allowed.extend(a.sub(exclude))
    allowed = new_allowed

print("ANSWER PART 1:", min(r.lower for r in allowed))
print("ANSWER PART 2:", sum(r.length() for r in allowed))
