from decimal import Decimal


def parse_cost_to_cents(cost_str):
    """
    Parses a cost string and convert it to cents as an integer.
    I'm converting money to be based in cents because it's what
    Stripe do and they know what's what when dealing with money! :D

    Args:
        cost_str (str): The cost string to be parsed.

    Returns:
        int: The cost in cents.
    """
    return int(Decimal(cost_str) * 100)
