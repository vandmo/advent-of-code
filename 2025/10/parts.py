def parse(line: str):
    lights, rest = line.split("] ")
    lights = lights.removeprefix("[")
    buttons, joltages = rest.split(" {")
    buttons = [
        tuple(int(n) for n in button.removeprefix("(").removesuffix(")").split(","))
        for button in buttons.split()
    ]
    joltages = tuple(int(n) for n in joltages.removesuffix("}").split(","))
    return lights, buttons, joltages


machines = [parse(line.strip()) for line in open("input.txt")]


def part1():
    from collections import deque

    def solve(lights, buttons, start):
        q = deque([(0, start)])
        visited = set()
        while q:
            dist, state = q.popleft()
            if lights == state:
                return dist
            if state in visited:
                continue
            visited.add(state)
            for button in buttons:
                new_state = list(state)
                for light in button:
                    new_state[light] = "." if new_state[light] == "#" else "#"
                new_state = "".join(new_state)
                q.append((dist + 1, new_state))

        assert False

    return sum(
        solve(lights, buttons, "." * len(lights)) for lights, buttons, _ in machines
    )


def part2():
    import mip

    def solve(joltages, buttons):
        m = mip.Model()
        m.verbose = 0
        vars_per_button = [m.add_var(var_type=mip.INTEGER) for _ in range(len(buttons))]
        for joltage_idx in range(len(joltages)):
            joltage = joltages[joltage_idx]
            contributing_buttons = []
            for button_idx, button in enumerate(buttons):
                if joltage_idx in button:
                    contributing_buttons.append(vars_per_button[button_idx])
            equation = contributing_buttons[0]
            for button in contributing_buttons[1:]:
                equation = equation + button
            m += equation == joltage
        m.objective = mip.minimize(mip.xsum(vars_per_button))
        assert m.optimize() == mip.OptimizationStatus.OPTIMAL
        return sum(int(v.x) for v in m.vars)

    return sum(solve(joltages, buttons) for _, buttons, joltages in machines)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
