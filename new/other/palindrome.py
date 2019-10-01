def is_palindrome(str: str) -> bool:
    start_i = 0
    end_i = len(str) - 1
    while start_i < end_i:
        if str[start_i] == str[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True


# Recursive method
def recursive_palindrome(str: str) -> bool:
    if len(str) <= 1:
        return True
    if str[0] == str[len(str) - 1]:
        return recursive_palindrome(str[1:-1])
    else:
        return False


def main() -> None:
    str = 'ama'
    print(recursive_palindrome(str.lower()))
    print(is_palindrome(str.lower()))


if __name__ == '__main__':
    main()
