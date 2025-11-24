timestamp_str, busses = [line.strip() for line in open("input.txt")]
timestamp = int(timestamp_str)
busses = busses.split(",")


def part1():
    mybusses = [int(bus) for bus in busses if bus != "x"]

    def next_bus_at(bus):
        if timestamp % bus == 0:
            return timestamp
        return ((timestamp // bus) + 1) * bus

    departure, bus_id = min((next_bus_at(bus), bus) for bus in mybusses)

    return (departure - timestamp) * bus_id


def part2():
    mybusses = [
        (int(bus_id), offset) for offset, bus_id in enumerate(busses) if bus_id != "x"
    ]
    n = 1
    step = 1
    for bus_id, offset in sorted(mybusses):
        while True:
            if n % bus_id == offset % bus_id:
                step = step * bus_id
                break
            n += step

    return step - n


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
