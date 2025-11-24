from itertools import combinations
from math import inf

WEAPONS = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
]

ARMOR = [
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
]

RINGS = [
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
]


def player_wins(player, boss):
    player_hit_poits, player_damage, player_armor = player
    boss_hit_points, boss_damage, boss_armor = boss
    player_damage_per_round = max(1, boss_damage - player_armor)
    boss_damage_per_round = max(1, player_damage - boss_armor)
    player_max_rounds = ((player_hit_poits - 1) // player_damage_per_round) + 1
    boss_max_rounds = ((boss_hit_points - 1) // boss_damage_per_round) + 1
    return player_max_rounds >= boss_max_rounds


BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR = [
    int(line.split(": ")[1]) for line in open("input.txt")
]

assert player_wins((8, 5, 5), (12, 7, 2))


def add(*args):
    total_cost, total_damage, total_armor = 0, 0, 0
    for _, cost, damage, armor in args:
        total_cost += cost
        total_damage += damage
        total_armor += armor
    return total_cost, total_damage, total_armor


part1 = inf
part2 = -inf
for weapon in WEAPONS:
    for narmor in range(2):
        for armor in combinations(ARMOR, narmor):
            for nrings in range(3):
                for rings in combinations(RINGS, nrings):
                    total_cost, total_damage, total_armor = add(weapon, *armor, *rings)
                    if player_wins(
                        (100, total_damage, total_armor),
                        (BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR),
                    ):
                        part1 = min(part1, total_cost)
                    else:
                        part2 = max(part2, total_cost)

print("ANSWER PART 1:", part1)
print("ANSWER PART 2:", part2)
