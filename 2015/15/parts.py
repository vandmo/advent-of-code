from dataclasses import dataclass
from itertools import combinations_with_replacement


@dataclass
class Ingredient:
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def parse(line):
    _, rest = line.split(": ")
    properties = rest.split(", ")
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for property in properties:
        name, value = property.split()
        value = int(value)
        match name:
            case "capacity":
                capacity = value
            case "durability":
                durability = value
            case "flavor":
                flavor = value
            case "texture":
                texture = value
            case "calories":
                calories = value
            case _:
                assert False
    return Ingredient(
        capacity=capacity,
        durability=durability,
        flavor=flavor,
        texture=texture,
        calories=calories,
    )


ingredients = tuple(parse(line.strip()) for line in open("input.txt"))


def calc(recipe):
    return (
        max(sum(i.capacity for i in recipe), 0)
        * max(sum(i.durability for i in recipe), 0)
        * max(sum(i.flavor for i in recipe), 0)
        * max(sum(i.texture for i in recipe), 0)
    )


print(
    "ANSWER PART 1:",
    max(calc(recipe) for recipe in combinations_with_replacement(ingredients, 100)),
)
print(
    "ANSWER PART 2:",
    max(
        calc(recipe)
        for recipe in combinations_with_replacement(ingredients, 100)
        if sum(i.calories for i in recipe) == 500
    ),
)
