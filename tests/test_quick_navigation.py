import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_FILE = os.path.join(PROJECT_ROOT, "app", "main.py")


def test_navigation_labels():
    with open(MAIN_FILE, "r", encoding="utf-8") as file:
        source = file.read()

    required_buttons = [
        "Dashboard",
        "Menu",
        "Customers",
        "New Order",
        "Order History",
        "Reports",
        "Q05 Performance",
    ]

    for button in required_buttons:
        assert button in source, f"Navigation button missing: {button}"

    print("All required navigation buttons are present.")


if __name__ == "__main__":
    print("Quick Navigation Verification")
    print("=" * 35)

    test_navigation_labels()

    print("\nRESULT: PASS")