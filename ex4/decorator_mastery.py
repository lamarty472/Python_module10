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


def main():
    print("Testing spell timer...")
    print("Result:", fireball())

    print("\nTesting power validator...")



if __name__ == "__main__":
    main()
