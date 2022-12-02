from typing import List


def get_input_str() -> str:
    with open("input.txt", "r") as f:
        input_str = f.read()
    return input_str


def get_calories_per_elf() -> List[int]:
    input_str = get_input_str()
    calories_per_elf = []
    for elf_load_str in input_str.split("\n\n"):
        elf_foods = map(int, elf_load_str.split("\n"))
        elf_calories = sum(elf_foods)
        calories_per_elf.append(elf_calories)
    return calories_per_elf


def part_one():
    calories_per_elf = get_calories_per_elf()
    return sorted(calories_per_elf, reverse=True)[0]


def part_two():
    calories_per_elf = get_calories_per_elf()
    return sum(sorted(calories_per_elf, reverse=True)[:3])


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
