#!/usr/bin/python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: -artifact["power"])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages,
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells,
        )
    )


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum([
                (lambda mage: mage["power"])(el)
                for el in mages
            ]) / len(mages),
            2
        ),
    }


def main() -> None:
    # Lambda Sanctum Test Data

    artifacts = [
        {"name": "Ice Wand", "power": 107, "type": "weapon"},
        {"name": "Fire Staff", "power": 69, "type": "weapon"},
        {"name": "Water Chalice", "power": 77, "type": "weapon"},
        {"name": "Storm Crown", "power": 110, "type": "armor"},
    ]

    mages = [
        {"name": "Zara", "power": 90, "element": "light"},
        {"name": "Luna", "power": 61, "element": "lightning"},
        {"name": "Kai", "power": 64, "element": "earth"},
        {"name": "Alex", "power": 60, "element": "wind"},
        {"name": "Casey", "power": 67, "element": "ice"},
    ]

    spells = ["blizzard", "freeze", "shield", "flash"]

    print(
        "===== BASE DATA =====",
        "-----------",
        "Artifacts:",
        artifacts,
        "-----------",
        "Mages:",
        mages,
        "-----------",
        "Spells:",
        spells,
        "-----------",
        sep="\n",
    )

    min_power = 67
    print(f"\n===== FILTERD MAGES (power >= {min_power}) =====")
    print(power_filter(mages, min_power))

    print("\n===== SORTED ARTIFACTS (by power, desc.) =====")
    print(artifact_sorter(artifacts))

    print("\n===== TRANSFORMED SPELLS (surrounded by * *) =====")
    print(spell_transformer(spells))
    print("\n===== MAGE STATS =====")
    print(mage_stats(mages))


if __name__ == "__main__":

    main()
