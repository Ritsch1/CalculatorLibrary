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
    return sum(args)
