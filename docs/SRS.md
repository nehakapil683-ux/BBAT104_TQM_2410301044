# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)

## Restaurant Billing System
### Quality Goal: Q05 – Reduce Response Time

---

## 1. Project Information

| Field | Details |
|---|---|
| Course | BBAT104 – Fundamentals of TQM |
| Academic Session | 2026–27 |
| Student Name | Neha Kapil |
| Roll Number | 2410301044 |
| Branch | CSE |
| Section | A |
| Baseline System | Restaurant Billing System |
| Quality Goal | Q05 – Reduce Response Time |

---

# 2. Introduction

## 2.1 Purpose

The purpose of the Restaurant Billing System is to provide a simple,
efficient and reliable software solution for managing restaurant orders,
menu items and customer bills.

The system will reduce manual billing work, improve order processing and
provide faster access to restaurant information.

The project specifically focuses on the TQM Quality Goal:

**Q05 – Reduce Response Time**

The system will implement five quality features:

1. Fast Search
2. Quick Navigation
3. Cached Dashboard
4. Database Indexing
5. Paginated Reports

---

## 2.2 Scope

The Restaurant Billing System will provide the following major functions:

- Add restaurant menu items
- View menu items
- Update menu items
- Delete menu items
- Search menu items quickly
- Create customer orders
- Calculate bills automatically
- View dashboard information
- Generate billing/report information
- Navigate quickly between system modules
- Display reports using pagination
- Optimize database queries using indexes

The system is designed for a small or medium-sized restaurant.

---

# 3. Problem Statement

Traditional manual restaurant billing can result in:

- Slow order processing
- Calculation errors
- Difficulty searching menu items
- Repeated database queries
- Slow report loading
- Unnecessary navigation steps
- Delays in viewing dashboard information

The proposed system aims to reduce these response-time problems by using
optimized search, database indexing, caching, quick navigation and
paginated reports.

---

# 4. Objectives

The main objectives of the project are:

1. Develop a functional Restaurant Billing System.
2. Implement complete CRUD operations.
3. Reduce response time during common operations.
4. Provide fast menu-item searching.
5. Provide quick navigation between modules.
6. Reduce repeated dashboard calculations through caching.
7. Improve database query performance through indexing.
8. Prevent reports from loading excessive records at once.
9. Apply TQM principles to software development.
10. Measure and improve software quality using SQC and TQM tools.

---

# 5. Users of the System

## 5.1 Restaurant Staff

Restaurant staff can:

- View menu items
- Search menu items
- Create orders
- Generate bills
- View reports

## 5.2 Administrator

The administrator can:

- Add menu items
- Update menu items
- Delete menu items
- View dashboard information
- Monitor system data
- View reports

---

# 6. Functional Requirements

## FR-01: Add Menu Item

The system shall allow authorized users to add a new menu item.

Required information:

- Item name
- Category
- Price
- Availability

---

## FR-02: View Menu Items

The system shall display available menu items in a structured format.

---

## FR-03: Update Menu Item

The system shall allow users to modify existing menu item information.

---

## FR-04: Delete Menu Item

The system shall allow authorized users to delete menu items.

---

## FR-05: Fast Search

The system shall provide a search feature that allows users to quickly
find menu items by name or category.

The search operation shall use optimized database queries.

---

## FR-06: Quick Navigation

The system shall provide a navigation menu allowing users to quickly
access:

- Dashboard
- Menu
- Orders
- Billing
- Reports

---

## FR-07: Cached Dashboard

The dashboard shall display frequently requested summary information.

Dashboard data may be cached temporarily to avoid performing the same
database calculations repeatedly.

---

## FR-08: Database Indexing

Database indexes shall be created on frequently searched or filtered
fields.

Example:

- Menu item name
- Category
- Order date

The purpose is to improve query response time.

---

## FR-09: Paginated Reports

The reporting module shall display a limited number of records per page
instead of loading all records simultaneously.

Users shall be able to move between report pages.

---

## FR-10: Billing

The system shall calculate:

- Item quantity
- Item price
- Subtotal
- Total bill amount

The system shall generate the final bill automatically.

---

# 7. Non-Functional Requirements

## 7.1 Performance

The system should respond quickly to common operations such as:

- Search
- Navigation
- Dashboard loading
- Report loading

---

## 7.2 Usability

The interface should be simple and easy to understand for restaurant
staff.

---

## 7.3 Reliability

The system should maintain correct data during normal operations.

---

## 7.4 Maintainability

The source code should be organized into separate modules so that future
changes can be made easily.

---

## 7.5 Data Integrity

The system should store restaurant data consistently in the SQLite
database.

---

## 7.6 Scalability

The system structure should allow additional restaurant features to be
added in the future.

---

# 8. Quality Goal – Q05

## Reduce Response Time

The project focuses on reducing the time required to perform frequently
used restaurant operations.

### Selected Quality Features

| Feature | Purpose |
|---|---|
| Fast Search | Quickly locate menu items |
| Quick Navigation | Reduce unnecessary screen transitions |
| Cached Dashboard | Avoid repeated calculations |
| Database Indexing | Improve database query speed |
| Paginated Reports | Reduce report loading time |

---

# 9. TQM Quality Parameters

The following Critical to Quality (CTQ) parameters will be monitored:

| CTQ | Measurement |
|---|---|
| Search Response Time | Time required to return search results |
| Dashboard Load Time | Time required to display dashboard |
| Navigation Time | Time required to open a module |
| Report Load Time | Time required to display report page |
| Database Query Time | Time required to execute important queries |

---

# 10. System Constraints

- The application will be developed using Python.
- SQLite will be used for local data storage.
- The application will run on a computer with Python installed.
- The system will initially target a single restaurant environment.
- Internet connectivity will not be required for basic application
  operations.

---

# 11. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Application development |
| Tkinter / CustomTkinter | GUI |
| SQLite3 | Database |
| Pandas | Data processing |
| Matplotlib | SQC charts |
| Git | Version control |
| GitHub | Repository hosting |
| VS Code | Development environment |

---

# 12. Expected Benefits

The system is expected to:

- Reduce manual billing effort
- Reduce search time
- Improve order processing
- Improve navigation
- Improve dashboard response
- Improve report loading performance
- Reduce unnecessary database operations
- Provide a structured restaurant billing workflow

---

# 13. Future Enhancements

Future versions may include:

- Online payment integration
- QR-code based ordering
- Customer management
- Inventory management
- Cloud database
- Multi-restaurant support
- Mobile application
- Advanced analytics

---

# 14. Conclusion

The Restaurant Billing System will provide a structured software solution
for restaurant order and billing operations.

The primary TQM focus of this project is **Q05 – Reduce Response Time**.
Fast Search, Quick Navigation, Cached Dashboard, Database Indexing and
Paginated Reports will be integrated to improve the responsiveness of the
system.

The project will also use TQM and Statistical Quality Control techniques
such as FMEA, SIPOC, CTQ analysis, Pareto analysis, Fishbone analysis,
Checksheets and PDCA for continuous quality improvement.