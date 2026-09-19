def calculate_expected_total(items):
    return sum(
        item["quantity"] * item["price"]
        for item in items
    )


def test_single_item_calculation():
    items = [
        {"quantity": 2, "price": 100.0}
    ]

    total = calculate_expected_total(items)

    assert total == 200.0

    print("Single-item calculation verified.")


def test_multiple_item_calculation():
    items = [
        {"quantity": 2, "price": 100.0},
        {"quantity": 1, "price": 150.0},
        {"quantity": 3, "price": 50.0},
    ]

    total = calculate_expected_total(items)

    assert total == 500.0

    print("Multiple-item calculation verified.")


def test_zero_quantity():
    items = [
        {"quantity": 0, "price": 100.0}
    ]

    total = calculate_expected_total(items)

    assert total == 0.0

    print("Zero-quantity calculation verified.")


if __name__ == "__main__":
    print("Billing Calculation Verification")
    print("=" * 40)

    test_single_item_calculation()
    test_multiple_item_calculation()
    test_zero_quantity()

    print("\nRESULT: PASS")