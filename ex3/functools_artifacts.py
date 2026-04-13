#!/usr/bin/python3

from collections.abc import Callable
from typing import Any
import functools
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(add, spells)
    elif operation == "multiply":
        return functools.reduce(mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    raise ValueError(f"Unknown operation {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "frost": functools.partial(base_enchantment, 50, "Frost"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning"),
    }


@functools.lru_cache(maxsize=4096)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(val: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return f"Damage spell: {damage} damage"

    @dispatcher.register(str)
    def _(ench: str) -> str:
        return f"Enchantment: {ench}"

    @dispatcher.register(list)
    def _(spells: list) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")

    try:
        print(
            "Sum:",
            spell_reducer([50, 30, 20], "add"),
            "\nProduct:",
            spell_reducer([50, 30, 20], "multiply"),
            "\nMax:",
            spell_reducer([50, 30, 20], "max"),
            "\nMin:",
            spell_reducer([50, 30, 20], "min"),
        )
        print("With invalid operation:")
        spell_reducer([], "eat")
    except Exception as e:
        print(e.__class__.__name__, ":", e)

    print("\nTesting partial enchanter...")

    enchanter = partial_enchanter(
        lambda power, element, target: (
            f"{target} is enchanted with {element} for {power}"
        )
    )

    print(f"Fire enchanter: {enchanter['fire']('Sword')}")
    print(f"Frost enchanter: {enchanter['frost']('Hammer')}")
    print(f"Lightning enchanter: {enchanter['lightning']('Spear')}")

    print("\nTesting fibonacci")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(
        dispatcher(42),
        dispatcher("fireball"),
        dispatcher([1, 2, 3]),
        dispatcher(None),
        sep="\n"
    )


if __name__ == "__main__":
    main()
