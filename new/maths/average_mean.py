"""Find mean of a list of numbers."""


def average(nums: List[int]) -> float:
    """Find mean of a list of numbers."""
    sum = 0
    for x in nums:
        sum += x
    avg = sum / len(nums)
    print(avg)
    return avg


def main() -> None:
    """Call average module to find mean of a specific list of numbers."""
    average([2, 4, 6, 8, 20, 50, 70])


if __name__ == '__main__':
    main()
