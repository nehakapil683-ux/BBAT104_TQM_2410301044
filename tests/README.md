# Testing Guide

## Restaurant Billing System – Q05: Reduce Response Time

This folder contains verification scripts for the Restaurant Billing System.

The tests focus on functional correctness, database integrity, billing calculations, input validation, and the five Q05 quality features.

---

## Test Files

| Test File | Purpose |
|---|---|
| `test_q05_performance.py` | Verifies Q05 performance-related operations |
| `test_fast_search.py` | Verifies menu and customer search |
| `test_quick_navigation.py` | Verifies application navigation |
| `test_cached_dashboard.py` | Verifies dashboard data and caching |
| `test_paginated_reports.py` | Verifies sales report and pagination support |
| `test_database_integrity.py` | Verifies database tables and indexes |
| `test_billing_calculation.py` | Verifies billing calculations |
| `test_input_validation.py` | Verifies quantity and price validation |

---

## Running a Test

Run commands from the project root:

```bash
python3 tests/test_fast_search.py