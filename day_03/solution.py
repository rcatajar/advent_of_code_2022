from collections import defaultdict
from string import ascii_letters


# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
PRIORITIES = {item: priority for priority, item in enumerate(ascii_letters, 1)}


def get_input_str() -> str:
    with open("input.txt", "r") as f:
        input_str = f.read()
    return input_str


def get_raw_sacks() -> list[str]:
    return get_input_str().split("\n")


# item: number
Compartiment = dict[str, int]
# 2 compartiment / sac
Sack = tuple[Compartiment, Compartiment]


def parse_compartiment(compartiment: str) -> Compartiment:
    content = defaultdict(int)
    for item in compartiment:
        content[item] += 1
    return content


def parse_sack(raw_sack: str) -> Sack:
    middle = int(len(raw_sack) / 2)
    raw_compartiment_1 = raw_sack[:middle]
    raw_compartiment_2 = raw_sack[middle:]
    return (
        parse_compartiment(raw_compartiment_1),
        parse_compartiment(raw_compartiment_2),
    )


def get_shared_item(sack: Sack) -> str:
    items_compartiment_1 = set(sack[0].keys())
    items_compartiment_2 = set(sack[1].keys())
    shared_items = items_compartiment_1 & items_compartiment_2
    if len(shared_items) != 1:
        raise ValueError("No unique shared item")
    return list(shared_items)[0]


def part_one():
    raw_sacks = get_raw_sacks()
    priorities_sum = 0
    for raw_sack in raw_sacks:
        sack = parse_sack(raw_sack)
        shared_item = get_shared_item(sack)
        priorities_sum += PRIORITIES[shared_item]
    return priorities_sum


# group of 3 elves input
ElvesGroup = tuple[str, str, str]


def get_groups() -> list[ElvesGroup]:
    raws_sacks = get_raw_sacks()
    return [
        (raws_sacks[i], raws_sacks[i + 1], raws_sacks[i + 2])
        for i in range(0, len(raws_sacks), 3)
    ]


def get_shared_group_item(ElvesGroup):
    items_1 = set(ElvesGroup[0])
    items_2 = set(ElvesGroup[1])
    items_3 = set(ElvesGroup[2])
    shared_items = items_1 & items_2 & items_3
    if len(shared_items) != 1:
        raise ValueError("No unique shared item")
    return list(shared_items)[0]


def part_two():
    groups = get_groups()
    priorities_sum = 0
    for group in groups:
        shared_item = get_shared_group_item(group)
        priorities_sum += PRIORITIES[shared_item]
    return priorities_sum


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
