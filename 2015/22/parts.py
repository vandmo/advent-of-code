from functools import cache
from math import inf

BOSS_HP, BOSS_DAMAGE = [int(line.split(": ")[1]) for line in open("input.txt")]


@cache
def least_cost_to_win(
    *,
    player_hp,
    player_mana,
    boss_hp,
    boss_damage,
    turn="player",
    shield_remain=0,
    poison_remain=0,
    recharge_remain=0,
    difficulty="easy"
):
    if difficulty == "hard" and turn == "player":
        player_hp -= 1
    if boss_hp <= 0:
        return 0, tuple()
    if player_hp <= 0:
        return inf, tuple()

    player_armor = 0

    # apply effect
    if shield_remain > 0:
        shield_remain -= 1
        player_armor += 7
    if poison_remain > 0:
        poison_remain -= 1
        boss_hp -= 3
        if boss_hp <= 0:
            return 0, tuple()
    if recharge_remain > 0:
        recharge_remain -= 1
        player_mana += 101

    if turn == "boss":
        player_hp -= max(1, boss_damage - player_armor)
        return least_cost_to_win(
            player_hp=player_hp,
            player_mana=player_mana,
            boss_hp=boss_hp,
            boss_damage=boss_damage,
            turn="player",
            shield_remain=shield_remain,
            poison_remain=poison_remain,
            recharge_remain=recharge_remain,
            difficulty=difficulty,
        )
    best = inf, tuple()

    # perform spell
    if player_mana >= 229 and recharge_remain == 0:
        # Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
        rest_cost, rest_casted = least_cost_to_win(
            player_hp=player_hp,
            player_mana=player_mana - 229,
            boss_hp=boss_hp,
            boss_damage=boss_damage,
            turn="boss",
            shield_remain=shield_remain,
            poison_remain=poison_remain,
            recharge_remain=5,
            difficulty=difficulty,
        )
        best = min(best, (229 + rest_cost, tuple(["recharge"]) + rest_casted))
    if player_mana >= 173 and poison_remain == 0:
        # Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
        rest_cost, rest_casted = least_cost_to_win(
            player_hp=player_hp,
            player_mana=player_mana - 173,
            boss_hp=boss_hp,
            boss_damage=boss_damage,
            turn="boss",
            shield_remain=shield_remain,
            poison_remain=6,
            recharge_remain=recharge_remain,
            difficulty=difficulty,
        )
        best = min(best, (173 + rest_cost, tuple(["poison"]) + rest_casted))
    if player_mana >= 113 and shield_remain == 0:
        # Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
        rest_cost, rest_casted = least_cost_to_win(
            player_hp=player_hp,
            player_mana=player_mana - 113,
            boss_hp=boss_hp,
            boss_damage=boss_damage,
            turn="boss",
            shield_remain=6,
            poison_remain=poison_remain,
            recharge_remain=recharge_remain,
            difficulty=difficulty,
        )
        best = min(best, (113 + rest_cost, tuple(["shield"]) + rest_casted))
    if player_mana >= 73:
        # Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
        rest_cost, rest_casted = least_cost_to_win(
            player_hp=player_hp + 2,
            player_mana=player_mana - 73,
            boss_hp=boss_hp - 2,
            boss_damage=boss_damage,
            turn="boss",
            shield_remain=shield_remain,
            poison_remain=poison_remain,
            recharge_remain=recharge_remain,
            difficulty=difficulty,
        )
        best = min(best, (73 + rest_cost, tuple(["drain"]) + rest_casted))
    if player_mana >= 53:
        # Magic Missile costs 53 mana. It instantly does 4 damage.
        rest_cost, rest_casted = least_cost_to_win(
            player_hp=player_hp,
            player_mana=player_mana - 53,
            boss_hp=boss_hp - 4,
            boss_damage=boss_damage,
            turn="boss",
            shield_remain=shield_remain,
            poison_remain=poison_remain,
            recharge_remain=recharge_remain,
            difficulty=difficulty,
        )
        best = min(best, (53 + rest_cost, tuple(["magic-missile"]) + rest_casted))
    return best


print(
    "ANSWER PART 1:",
    least_cost_to_win(
        player_hp=50, player_mana=500, boss_hp=BOSS_HP, boss_damage=BOSS_DAMAGE
    ),
)
print(
    "ANSWER PART 2:",
    least_cost_to_win(
        player_hp=50,
        player_mana=500,
        boss_hp=BOSS_HP,
        boss_damage=BOSS_DAMAGE,
        difficulty="hard",
    ),
)
