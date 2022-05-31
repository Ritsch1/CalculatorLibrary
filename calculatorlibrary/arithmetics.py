from functools import reduce


def add(*args: [float]) -> float:
    """Add arbitrary numeric arguments together and return the sum.

    Params:
        args[float]: Numerical arguments to be added together.

    Returns:
        float: The sum of the arguments.
    """
    assert (
        len(args) >= 2
    ), "At least two numbers need to be provided in order to calculate a sum."
    assert all(
        isinstance(number, (int, float)) for number in args
    ), "Only numeric values can be provided to the add function."
    return reduce(lambda x, y: x + y, args)


def subtract(*args: [float]) -> float:
    """subtract arbitrary many numeric arguments from each other.

    Params:
        args[float]: Numerical arguments to be subtracted from each other.
    Returns:
        float: The difference of the numerical arguments.
    """
    assert (
        len(args) >= 2
    ), "At least two numbers need to be provided in order to calculate a sum."
    assert all(
        isinstance(number, (int, float)) for number in args
    ), "Only numeric values can be provided to the add function."
    return reduce(lambda x, y: x - y, args)
