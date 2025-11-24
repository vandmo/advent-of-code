reindeers = list()
for line in open("input.txt"):
    name, rest = line.split(" can fly ")
    left, right = rest.split(" seconds, but then must rest for ")
    speed, fly_time = left.split(" km/s for ")
    speed = int(speed)
    fly_time = int(fly_time)
    rest_time, _ = right.split(" seconds.")
    rest_time = int(rest_time)
    reindeers.append((name, speed, fly_time, rest_time))


def distance_after(reindeer, s):
    _, speed, fly_time, rest_time = reindeer
    interval_time = fly_time + rest_time
    q, r = divmod(s, interval_time)
    whole = speed * fly_time * q
    part = speed * min(fly_time, r)
    return whole + part


print("ANSWER PART 1:", max(distance_after(reindeer, 2503) for reindeer in reindeers))


points_per_reindeer = dict()
for s in range(1, 2503 + 1):
    distances = dict()
    for reindeer in reindeers:
        distances[reindeer[0]] = distance_after(reindeer, s)
    lead_distance = max(distances.values())
    for name, distance in distances.items():
        if distance == lead_distance:
            points_per_reindeer[name] = points_per_reindeer.get(name, 0) + 1

print("\nSCOREBOARD PART 2:")
for name, points in sorted(points_per_reindeer.items(), key=lambda item: -item[1]):
    print(f"  {name:<10}{points:>12}")

winner, points = max(points_per_reindeer.items(), key=lambda item: item[1])
print(f"Winner is {winner} with \033[1;37m{points}\033[0m points!")
