#!/usr/bin/python3

from collections.abc import Callable
from typing import Any, Optional


def mage_counter() -> Callable:
    i = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item_name: (
        f"{enchantment_type.capitalize()} {item_name.capitalize()}"
    )


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: Any, value: Any) -> None:
        vault[key] = value

    def recall(key: Any) -> Optional[Any]:
        return vault.get(key) or "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i} = {counter_a()}")
    print(f"counter_b call 1 = {counter_b()}")

    print("\nTesting spell accumulator...")
    base_power = 100
    accumator = spell_accumulator(base_power)
    print(f"Base {base_power}, add 20 : {accumator(20)}")
    print(f"Base {base_power}, add 30 : {accumator(30)}")

    print("\nTesting enchantment factory...")
    flame_enchanter = enchantment_factory("Flame")
    frozen_enchanter = enchantment_factory("frozen")
    print(flame_enchanter("sword"))
    print(frozen_enchanter("Shield"))

    print("\nTesting memory vault..")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]('secret', 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
