# Database Index Verification

## Project

Restaurant Billing System – Q05: Reduce Response Time

## Objective

Database indexing is used to improve the performance of frequently searched, filtered, and related database operations.

## Implemented Indexes

| Index | Table | Column | Purpose |
|---|---|---|---|
| idx_menu_name | menu_items | name | Faster menu search |
| idx_menu_category | menu_items | category | Faster category filtering |
| idx_menu_available | menu_items | available | Faster available-item filtering |
| idx_customer_name | customers | name | Faster customer search |
| idx_customer_phone | customers | phone | Faster customer lookup |
| idx_orders_date | orders | order_date | Faster order/date filtering |
| idx_orders_customer | orders | customer_id | Faster customer-order lookup |
| idx_order_items_order | order_items | order_id | Faster order-item retrieval |
| idx_order_items_menu | order_items | menu_item_id | Faster menu-item relation lookup |

## Verification Method

The application provides a function to retrieve the configured database indexes.

```python
from database.db import get_database_indexes

indexes = get_database_indexes()

for index in indexes:
    print(index)