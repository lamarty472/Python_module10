from typing import Callable
from typing import Any
import operator
from functools import reduce, partial, lru_cache, singledispatch


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
    version_fire = partial(base_enchantment, power=50, element="fire")
    version_ice = partial(base_enchantment, power=50, element="ice")
    version_lightning = partial(
        base_enchantment, power=50, element="lightning"
        )

    return {
        "fire": version_fire,
        "ice": version_ice,
        "lightning": version_lightning,
    }


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} spell of power {power} cast on {target}"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(x: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(x: int) -> str:
        return f"{x} damage"

    @dispatcher.register
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @dispatcher.register(list)
    def _(x: list[Any]) -> str:
        return f"Multi-cast: {len(x)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    print(spell_reducer([10, 20, 30, 40], "add"))
    print(spell_reducer([10, 20, 30, 40], "multiply"))
    print(spell_reducer([10, 20, 30, 40], "max"))

    print("\nTesting partial_enchanter...")
    versions = partial_enchanter(base_enchantment)
    print(versions["fire"](target="dragon"))
    print(versions["ice"](target="troll"))
    print(versions["lightning"](target="gollem"))

    print("\nTesting memoized_fibonacci...")
    print(memoized_fibonacci(10))
    print(memoized_fibonacci(15))
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell([1, 2, 3]))
    print(spell(3.14))


if __name__ == "__main__":
    main()
