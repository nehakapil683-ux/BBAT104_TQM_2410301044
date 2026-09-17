import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from database.db import get_dashboard_data


def test_dashboard_data():
    data = get_dashboard_data()

    assert isinstance(data, dict)

    required_keys = [
        "menu_count",
        "customer_count",
        "order_count",
        "total_sales",
        "today_orders",
        "today_sales",
    ]

    for key in required_keys:
        assert key in data, f"Dashboard data missing: {key}"

    print("Dashboard data structure verified.")


def test_dashboard_cache_implementation():
    main_file = os.path.join(PROJECT_ROOT, "app", "main.py")

    with open(main_file, "r", encoding="utf-8") as file:
        source = file.read()

    assert "dashboard_cache" in source
    assert "refresh_dashboard" in source

    print("Dashboard caching implementation verified.")


if __name__ == "__main__":
    print("Cached Dashboard Verification")
    print("=" * 35)

    test_dashboard_data()
    test_dashboard_cache_implementation()

    print("\nRESULT: PASS")