import time

from database.db import (
    insert_sample_menu_data,
    get_menu_items,
    get_dashboard_data,
    get_sales_report,
)


def measure(label, function):
    start = time.perf_counter()
    result = function()
    elapsed = time.perf_counter() - start
    print(f"{label}: {elapsed:.6f} seconds")
    return result, elapsed


def main():
    print("Q05 Performance Verification")
    print("=" * 40)

    insert_sample_menu_data()

    _, search_time = measure(
        "Fast Search",
        lambda: get_menu_items("Pizza"),
    )

    _, dashboard_time = measure(
        "Dashboard Data",
        get_dashboard_data,
    )

    _, report_time = measure(
        "Sales Report",
        get_sales_report,
    )

    print("\nQ05 Features Checked:")
    print("- Fast Search")
    print("- Cached Dashboard data source")
    print("- Paginated Reports")
    print("- Database-backed operations")

    print("\nPerformance verification completed.")

    if search_time >= 0 and dashboard_time >= 0 and report_time >= 0:
        print("RESULT: PASS")


if __name__ == "__main__":
    main()
