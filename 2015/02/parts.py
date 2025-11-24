def paper(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def ribbon(l, w, h):
    s1, s2, _ = sorted([l, w, h])
    return 2 * s1 + 2 * s2 + l * w * h


presents = [
    tuple(int(n) for n in present.strip().split("x")) for present in open("input.txt")
]
print("ANSWER PART 1:", sum(paper(*present) for present in presents))
print("ANSWER PART 2:", sum(ribbon(*present) for present in presents))
