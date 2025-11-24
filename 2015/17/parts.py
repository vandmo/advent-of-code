containers = sorted([int(n) for n in open("input.txt")])


def find_all(eggnog, containers):
    solutions = list()

    def search(remaining_eggnog, remaining_containers, used_containers):
        if remaining_eggnog < 0:
            return
        elif remaining_eggnog == 0:
            solutions.append(used_containers)
            return
        elif not remaining_containers:
            return
        for i in range(len(remaining_containers)):
            search(
                remaining_eggnog - remaining_containers[i],
                remaining_containers[i + 1 :],
                used_containers + (remaining_containers[i],),
            )

    search(eggnog, containers, tuple())
    return solutions


EGGNOG = 150
all_solutions = find_all(EGGNOG, containers)
print("ANSWER PART 1:", len(all_solutions))
min_length = min(len(solution) for solution in all_solutions)
minimal_solutions = list(
    filter(lambda solution: len(solution) == min_length, all_solutions)
)
print(
    "ANSWER PART 2:",
    sum(len(find_all(EGGNOG, solution)) for solution in minimal_solutions),
)
