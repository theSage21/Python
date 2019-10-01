"""Newton's Method."""

# Newton's Method - https://en.wikipedia.org/wiki/Newton%27s_method


# function is the f(x) and function1 is the f'(x)
def newton(function: Callable, function1: Callable, startingInt: int) -> float:
    x_n = startingInt
    while True:
        x_n1 = x_n - function(x_n) / function1(x_n)
        if abs(x_n - x_n1) < 10**-5:
            return x_n1
        x_n = x_n1


def f(x: float) -> float:
    return (x**3) - (2 * x) - 5


def f1(x: float) -> float:
    return 3 * (x**2) - 2


if __name__ == "__main__":
    print(newton(f, f1, 3))
