bots = dict()
bot_instrs = dict()
outputs = dict()

for line in open("input.txt"):
    line = line.strip()
    if line.startswith("value "):
        line = line[len("value ") :]
        v, b = [int(n) for n in line.split(" goes to bot ")]
        bots.setdefault(b, []).append(v)
    elif line.startswith("bot "):
        line = line[len("bot ") :]
        l, r = line.split(" gives low to ")
        bot = int(l)
        low, high = r.split(" and high to ")
        bot_instrs[bot] = low, high
    else:
        assert 0


def give(source, target, value):
    if target.startswith("bot "):
        targetbot = int(target[len("bot ") :])
        targetchips = bots.setdefault(targetbot, [])
        assert len(targetchips) < 2
        targetchips.append(value)
    else:
        output = int(target[len("output ") :])
        outputs.setdefault(output, []).append(value)
    source.remove(value)


def solve():
    acted = True
    part1 = None
    while acted:
        acted = False
        for bot in list(bots.keys()):
            chips = bots[bot]
            if 61 in chips and 17 in chips:
                assert part1 is None
                part1 = bot
            if len(chips) == 2:
                acted = True
                low, high = bot_instrs[bot]
                give(chips, low, min(chips))
                give(chips, high, max(chips))
    return part1


print("ANSWER PART 1:", solve())
print("ANSWER PART 2:", outputs[0][0] * outputs[1][0] * outputs[2][0])
