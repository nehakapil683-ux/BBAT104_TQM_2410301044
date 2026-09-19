# Database Design

## Restaurant Billing System – Q05: Reduce Response Time

## 1. Database Technology

The project uses **SQLite3** as its database.

SQLite was selected because it is lightweight, serverless, easy to integrate with Python, and suitable for a desktop billing application.

---

## 2. Database Tables

The system contains four main tables:

1. `menu_items`
2. `customers`
3. `orders`
4. `order_items`

---

## 3. Menu Items Table

The `menu_items` table stores restaurant menu information.

| Column | Purpose |
|---|---|
| `id` | Unique menu item ID |
| `name` | Menu item name |
| `category` | Menu category |
| `price` | Item price |
| `available` | Availability status |

### Main Operations

- Add menu item
- View menu items
- Search menu items
- Update menu item
- Delete menu item

---

## 4. Customers Table

The `customers` table stores customer information.

| Column | Purpose |
|---|---|
| `id` | Unique customer ID |
| `name` | Customer name |
| `phone` | Customer phone number |
| `email` | Customer email |

### Main Operations

- Add customer
- Search customers
- View customers
- Count customers

---

## 5. Orders Table

The `orders` table stores order-level information.

| Column | Purpose |
|---|---|
| `id` | Unique order ID |
| `customer_id` | Related customer |
| `order_date` | Date and time of order |
| `total` | Total order amount |
| `status` | Order status |

The `customer_id` connects an order with a customer.

---

## 6. Order Items Table

The `order_items` table stores individual items belonging to an order.

| Column | Purpose |
|---|---|
| `id` | Unique order-item ID |
| `order_id` | Related order |
| `menu_item_id` | Related menu item |
| `quantity` | Quantity ordered |
| `price` | Price at the time of order |
| `subtotal` | Item subtotal |

The subtotal is based on the item's price and quantity.

---

## 7. Table Relationships

The main relationships are:

```text
Customers
    |
    | 1
    |
    | many
    v
Orders
    |
    | 1
    |
    | many
    v
Order Items
    ^
    |
    | many
    |
Menu Items