def validate_quantity(quantity):
    try:
        value = int(quantity)
        return value > 0
    except (ValueError, TypeError):
        return False


def validate_price(price):
    try:
        value = float(price)
        return value >= 0
    except (ValueError, TypeError):
        return False


def test_valid_quantity():
    assert validate_quantity("2") is True
    print("Valid quantity verification passed.")


def test_invalid_quantity():
    assert validate_quantity("0") is False
    assert validate_quantity("-1") is False
    assert validate_quantity("abc") is False
    print("Invalid quantity verification passed.")


def test_valid_price():
    assert validate_price("100") is True
    assert validate_price("99.50") is True
    print("Valid price verification passed.")


def test_invalid_price():
    assert validate_price("-10") is False
    assert validate_price("abc") is False
    print("Invalid price verification passed.")


if __name__ == "__main__":
    print("Input Validation Verification")
    print("=" * 40)

    test_valid_quantity()
    test_invalid_quantity()
    test_valid_price()
    test_invalid_price()

    print("\nRESULT: PASS")