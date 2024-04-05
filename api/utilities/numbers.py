from decimal import Decimal


def parse_cost_to_cents(cost_str):
    # Convert string to Decimal for precision
    cost_decimal = Decimal(cost_str)
    # Multiply by 100 to convert to cents and convert to integer
    cost_cents = int(cost_decimal * 100)
    return cost_cents
