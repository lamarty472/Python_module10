import time
from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball():
    time.sleep(0.1)
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None and len(args) > 0:
                power = args[-1]

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(min_power=10)
def cast_spell_standalone(spell_name: str, power: int) -> str:
    return f"Successfully cast {spell_name} with {power} power"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


attempt_counter = {"count": 0}


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    attempt_counter["count"] += 1
    if attempt_counter["count"] < 3:
        raise ValueError("Spell fizzled")
    return "Waaaaaaagh spelled!"


@retry_spell(max_attempts=3)
def doomed_spell() -> str:
    raise ValueError("Spell fizzled")


def main():
    print("Testing spell timer...")
    print("Result:", fireball())

    print("\nTesting power validator...")
    print(cast_spell_standalone("Lightning", power=15))
    print(cast_spell_standalone("Weak", power=5))

    print("\nTesting retrying spell...")
    print(unstable_spell())
    print(doomed_spell())


if __name__ == "__main__":
    main()
