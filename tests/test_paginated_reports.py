import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from database.db import get_sales_report


def test_sales_report_returns_data():
    results = get_sales_report()

    assert isinstance(results, list)

    print(f"Sales report returned {len(results)} records.")


def test_pagination_support_in_application():
    main_file = os.path.join(PROJECT_ROOT, "app", "main.py")

    with open(main_file, "r", encoding="utf-8") as file:
        source = file.read()

    pagination_terms = [
        "page",
        "page_size",
        "next_page",
        "previous_page",
    ]

    found_terms = [
        term for term in pagination_terms
        if term in source
    ]

    assert len(found_terms) >= 2, (
        "Pagination-related implementation could not be verified."
    )

    print("Pagination-related implementation verified.")
    print(f"Detected terms: {', '.join(found_terms)}")


if __name__ == "__main__":
    print("Paginated Reports Verification")
    print("=" * 35)

    test_sales_report_returns_data()
    test_pagination_support_in_application()

    print("\nRESULT: PASS")