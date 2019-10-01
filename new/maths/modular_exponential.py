

def modular_exponential(base: int, power: int, mod: int) -> int:
    """Calculate Modular Exponential."""
    if power < 0:
        return -1
    base %= mod
    result = 1

    while power > 0:
        if power & 1:
            result = (result * base) % mod
        power = power >> 1
        base = (base * base) % mod
    return result


def main() -> None:
    """Call Modular Exponential Function."""
    print(modular_exponential(3, 200, 13))


if __name__ == '__main__':
    main()
