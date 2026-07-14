from typing import Callable


# test functions


def water_ball(target: str, power: int) -> str:
    return f"Throw a waterball on {target} and has a power of {power}!"


def thunder(target: str, power: int) -> str:
    return f"Throw a thunder on {target} and has a power of {power}!"


def flying(target: str, power: int) -> str:
    return f"{target} start flying at a height of {power} meters"


def can_begin_flying(target: str, power: int) -> bool:
    if power >= 5 and target != "fairy":
        return (True)
    else:
        return (False)


# function requested


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def new_power(target: str, power: int) -> Callable:
        new_spell = base_spell(target, power * multiplier)
        return (new_spell)
    return new_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


def main() -> None:
    print("Testing spell_combiner:")
    combined_spell = spell_combiner(water_ball, thunder)
    result = combined_spell("Claude", 5)
    print(f"combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power_amplifier:")
    amplified_power = power_amplifier(thunder, 5)
    result = amplified_power("Francois", 5)
    print(f"power amplifier result: {result}")

    print("\nTesting conditional caster with wrong target:")
    cast = conditional_caster(can_begin_flying, flying)
    result = cast("fairy", 5)
    print(f"conditional caster result: {result}")
    print("\nTesting conditional caster with wrong power:")
    cast = conditional_caster(can_begin_flying, flying)
    result = cast("pig", 2)
    print(f"conditional caster result: {result}")
    print("\nTesting conditional caster with correct args:")
    cast = conditional_caster(can_begin_flying, flying)
    result = cast("litle dog", 12)
    print(f"conditional caster result: {result}")

    print("\nTesting spell sequence:")
    spell_list = [water_ball, thunder, flying]
    sequence = spell_sequence(spell_list)
    result = sequence("litle dog", 2)
    print(f"spell sequence result: {result}")


if __name__ == "__main__":
    main()
