from typing import Callable


def mage_counter() -> Callable:
    counter = 0

    def mage():
        nonlocal counter
        counter += 1
        return counter
    return mage


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(add_power: int):
        nonlocal total_power
        total_power += add_power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    enchantment = enchantment_type

    def factory(item: str):
        return enchantment + " " + item
    return factory


def memory_vault() -> dict[str, Callable]:
    memory = []
    i = 0

    def store(key: str, value: Callable):
        nonlocal i
        memory.append([key, value])
        i += 1

    def recall(key: str):
        for case in memory:
            if case[0] == key:
                return case[1]
        return "Memory Not Found"
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 3: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    spell = spell_accumulator(100)
    print(f"Base 100, and 20: {spell(20)}")
    print(f"Base 100, add 30: {spell(30)}")

    print("\nTesting enchantment factory...")
    enchantment = enchantment_factory("Firing")
    enchantment2 = enchantment_factory("Freeze")
    print(f"{enchantment('Sword')}")
    print(f"{enchantment('Stick')}")
    print(f"{enchantment2('Arrow')}")

    print("\nTesting memory vault...")
    ssd1 = memory_vault()
    print("store: Coucou in ssd1 with the key: text")
    ssd1["store"]("text", "Coucou")
    print(f"ssd1 = {ssd1['recall']('text')}")
    print("store: 7 in ssd1 with the key: integer")
    ssd1["store"]("integer", "7")
    print(f"ssd1 = {ssd1['recall']('integer')}")
    print("Sherch Happyness case in ssd1")
    print(f"ssd1 = {ssd1['recall']('Happyness')}")


if __name__ == "__main__":
    main()
