from collections import Counter

ingredient_count = Counter()
per_allergen: dict[str, set[str]] = dict()

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    ingredients, allergens = line.split(" (contains ")
    allergens = allergens.removesuffix(")")
    ingredients = set(ingredients.split())
    allergens = set(allergens.split(", "))
    ingredient_count.update(ingredients)
    for allergen in allergens:
        if not allergen in per_allergen:
            per_allergen[allergen] = ingredients
        else:
            per_allergen[allergen] = per_allergen[allergen].intersection(ingredients)


def pair_ingredient_with_allergen(per_allergen, remaining: set[str]):
    if not per_allergen:
        assert not remaining
        return tuple()
    (first_allergen, first_ingredients), *rest = per_allergen
    for remaining_ingredient in first_ingredients:
        if remaining_ingredient not in remaining:
            continue
        remaining_pairs = pair_ingredient_with_allergen(
            rest, remaining - set([remaining_ingredient])
        )
        if remaining_pairs is not None:
            return ((first_allergen, remaining_ingredient),) + remaining_pairs
    return None


ingredients_that_might_contain_allergen = set()
for ingredients in per_allergen.values():
    ingredients_that_might_contain_allergen.update(ingredients)
ingredients_that_can_not_contain_an_allergen = (
    ingredient_count.keys() - ingredients_that_might_contain_allergen
)
paired = pair_ingredient_with_allergen(
    list(sorted(per_allergen.items(), key=lambda i: len(i[1]))),
    ingredients_that_might_contain_allergen,
)
assert paired is not None

print(
    "ANSWER PART 1:",
    sum(
        ingredient_count[ingredient]
        for ingredient in ingredients_that_can_not_contain_an_allergen
    ),
)
print("ANSWER PART 2:", ",".join(pair[1] for pair in sorted(paired)))
