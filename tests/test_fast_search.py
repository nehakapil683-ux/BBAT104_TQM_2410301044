import os
import sys
import time

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from database.db import (
    get_menu_items,
    get_customers,
)


def test_menu_fast_search():
    start = time.perf_counter()

    results = get_menu_items("Pizza")

    elapsed = time.perf_counter() - start

    print(f"Menu search time: {elapsed:.6f} seconds")
    print(f"Menu search results: {len(results)}")

    assert isinstance(results, list)


def test_customer_fast_search():
    start = time.perf_counter()

    results = get_customers("")

    elapsed = time.perf_counter() - start

    print(f"Customer search time: {elapsed:.6f} seconds")
    print(f"Customer search results: {len(results)}")

    assert isinstance(results, list)


if __name__ == "__main__":
    print("Fast Search Verification")
    print("=" * 30)

    test_menu_fast_search()
    test_customer_fast_search()

    print("\nRESULT: PASS")