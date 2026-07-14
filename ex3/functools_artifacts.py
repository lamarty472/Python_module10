from typing import Callable
import operator
from functools import reduce


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    


def main():
    print("Testing spell reducer...")
    print(spell_reducer([10, 20, 30, 40], "add"))
    print(spell_reducer([10, 20, 30, 40], "multiply"))
    print(spell_reducer([10, 20, 30, 40], "max"))


if __name__ == "__main__":
    main()
