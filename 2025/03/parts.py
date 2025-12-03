banks = [line.strip() for line in open("input.txt")]


def best_joltage(bank, batteries_to_take):
    result = ["0"] * batteries_to_take
    best_battery_at = -1
    for battery_at in range(batteries_to_take):
        for battery_index in range(
            best_battery_at + 1, len(bank) - batteries_to_take + battery_at + 1
        ):
            if bank[battery_index] > result[battery_at]:
                result[battery_at] = bank[battery_index]
                best_battery_at = battery_index
    return int("".join(result))


print("ANSWER PART 1:", sum(best_joltage(bank, 2) for bank in banks))
print("ANSWER PART 2:", sum(best_joltage(bank, 12) for bank in banks))
