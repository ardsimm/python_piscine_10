#!/usr/bin/python3

from collections.abc import Callable
from typing import List


PLAYER_NAME = "BURLAG COURTE QUEUE"


def healing_word(target: str, power: int) -> str:
    return f"Healing word restores {target} for {power} HP"


def eldritch_blast(target: str, power: int) -> str:
    return f"Eldritch blast damages {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combiner(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combiner


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditioned_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditioned_spell


def spell_sequence(
    spells: List[Callable[[str, int], str]],
) -> Callable[[str, int], List[str]]:
    def sequence_cast(target: str, power: int) -> List[str]:
        return [spell(target, power) for spell in spells]
    return sequence_cast


def main() -> None:

    print("Testing spell combiner...")

    print(spell_combiner(healing_word, eldritch_blast)(PLAYER_NAME, 42))

    print("\nTesting power amplifier...")

    print(power_amplifier(eldritch_blast, 5)(PLAYER_NAME, 5))

    print("\nTesting Conditional caster...")
    print("With condition -> False:")
    print(
        conditional_caster(
            condition=lambda target, power: target != "" and power > 0,
            spell=eldritch_blast
        )("", -1)
    )

    print("\nWith condition -> True:")
    print(
        conditional_caster(
            condition=lambda target, power: target != "" and power > 0,
            spell=healing_word
        )(PLAYER_NAME, 42)
    )

    print("\nTesting Spell sequence...")
    print(
        spell_sequence([
            healing_word,
            eldritch_blast,
            eldritch_blast,
            healing_word
        ])(PLAYER_NAME, 42)
    )


if __name__ == "__main__":
    main()
