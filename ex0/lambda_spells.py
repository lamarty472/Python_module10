def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(x['power'] for x in mages) / len(mages), 2)

    return {
        'max_power': max_power, 'min_power': min_power, 'avg_power': avg_power
        }


def main() -> None:
    print("Testing artifact sorter...")
    test_artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'accessory'}
    ]
    sorted_artifacts = artifact_sorter(test_artifacts)
    print(
        f"{sorted_artifacts[0]['name']}"
        f" ({sorted_artifacts[0]['power']}"
        f" power) comes before {sorted_artifacts[1]['name']}"
        f" ({sorted_artifacts[1]['power']} power)"
        )

    print("\nTesting spell transformer...")
    test_spells = ["Fireball", "heal", "shield"]
    test_spells = spell_transformer(test_spells)
    print(*test_spells)


if __name__ == "__main__":
    main()
