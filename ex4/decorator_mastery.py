#!/usr/bin/python3

from collections.abc import Callable
import time
import functools
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        print(f"Casting {func.__name__}...")
        t1 = time.time()
        result = func(*args, **kwds)
        t2 = time.time()
        print(f"Spell completed in {round(t2 - t1, 3)} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def power_validator_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwds: Any) -> Any:
            if args[1] >= min_power:
                return func(*args, **kwds)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return power_validator_decorator


def retry_spell(max_attempts: int) -> Callable:
    def retry_spell_decorator(func: Callable) -> Callable:
        tries_counter = 1

        @functools.wraps(func)
        def wrapper(*args: Any, **kwds: Any) -> Any:
            nonlocal tries_counter
            if tries_counter > max_attempts:
                return "Spell casting failed after max_attempts attempts"
            try:
                return func(*args, **kwds)
            except Exception:
                print(
                    "Spell failed, retrying...",
                    f"({tries_counter}/{max_attempts})"
                )
                tries_counter += 1
                return wrapper(*args, **kwds)

        return wrapper

    return retry_spell_decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        len_name = len(name)
        return len_name > 2 and len([
            char for char in name
            if str.isalpha(char) or str.isspace(char)
        ]) == len_name

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def spell_timer_test() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print("Result:", spell_timer_test())

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def failing_spell() -> str:
        if True is True and False is False:
            raise Exception("nope hihihi :p")
        else:
            return "How did we get here ?"

    @retry_spell(max_attempts=3)
    def successful_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(failing_spell())
    print(successful_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Xxx_DopeMage6942_xxX"))
    print(MageGuild.validate_mage_name("Boring Mage"))

    mage_guild = MageGuild()
    print(mage_guild.cast_spell(42, "Eldritch Blast"))
    print(mage_guild.cast_spell(2, "Healing Word"))


if __name__ == "__main__":
    main()
