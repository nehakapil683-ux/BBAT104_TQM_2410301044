# Test Cases – Restaurant Billing System

## Project Information

- **Project:** Restaurant Billing System
- **Quality Goal:** Q05 – Reduce Response Time
- **Student:** Neha Kapil
- **Roll No.:** 2410301044
- **Branch:** CSE
- **Section:** A

---

## 1. Testing Objective

Testing is performed to verify that the Restaurant Billing System works correctly and that the Q05 response-time features perform their intended functions.

---

## 2. Test Case Format

Each test case contains:

- Test Case ID
- Module
- Test Description
- Expected Result
- Actual Result
- Status

---

## 3. Functional Test Cases

| ID | Module | Test Description | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Database | Initialize database | Tables and indexes are created | PASS |
| TC02 | Menu | Add valid menu item | Menu item is added successfully | PASS |
| TC03 | Menu | Update menu item | Selected item is updated | PASS |
| TC04 | Menu | Delete menu item | Selected item is deleted | PASS |
| TC05 | Menu | Search menu item | Matching menu items are displayed | PASS |
| TC06 | Customer | Add valid customer | Customer is added successfully | PASS |
| TC07 | Customer | Search customer | Matching customer is displayed | PASS |
| TC08 | Order | Select customer | Customer is selected successfully | PASS |
| TC09 | Order | Add menu item to cart | Item appears in cart | PASS |
| TC10 | Order | Change quantity | Quantity is updated correctly | PASS |
| TC11 | Order | Remove cart item | Selected item is removed | PASS |
| TC12 | Billing | Generate bill | Correct bill is displayed | PASS |
| TC13 | History | Open order history | Previous orders are displayed | PASS |
| TC14 | Reports | Open reports | Sales records are displayed | PASS |

---

## 4. Q05 Performance Test Cases

| ID | Feature | Test Description | Expected Result | Status |
|---|---|---|---|---|
| Q05-T01 | Fast Search | Search menu using prefix | Matching records appear efficiently | PASS |
| Q05-T02 | Fast Search | Search customer using prefix | Matching records appear efficiently | PASS |
| Q05-T03 | Quick Navigation | Navigate to Menu | Menu opens directly | PASS |
| Q05-T04 | Quick Navigation | Navigate to Customers | Customer page opens directly | PASS |
| Q05-T05 | Quick Navigation | Navigate to New Order | Order page opens directly | PASS |
| Q05-T06 | Cached Dashboard | Refresh dashboard repeatedly | Repeated queries are reduced through caching | PASS |
| Q05-T07 | DB Indexing | Verify menu indexes | Required indexes exist | PASS |
| Q05-T08 | DB Indexing | Verify customer indexes | Required indexes exist | PASS |
| Q05-T09 | DB Indexing | Verify order indexes | Required indexes exist | PASS |
| Q05-T10 | Paginated Reports | Open report | Records are displayed page-wise | PASS |
| Q05-T11 | Paginated Reports | Next page | Next records are displayed | PASS |
| Q05-T12 | Paginated Reports | Previous page | Previous records are displayed | PASS |

---

## 5. Input Validation Test Cases

| ID | Test | Expected Result | Status |
|---|---|---|---|
| VAL01 | Empty menu name | Input should be rejected | PASS |
| VAL02 | Invalid menu price | Invalid value should be rejected | PASS |
| VAL03 | Empty customer name | Input should be rejected | PASS |
| VAL04 | Invalid quantity | Invalid quantity should be rejected | PASS |
| VAL05 | Empty order selection | Order should not be generated without required data | PASS |

---

## 6. Billing Calculation Tests

| ID | Test | Expected Result | Status |
|---|---|---|---|
| BILL01 | One item × quantity 1 | Correct subtotal | PASS |
| BILL02 | One item × quantity > 1 | Quantity-based subtotal | PASS |
| BILL03 | Multiple cart items | Correct combined total | PASS |
| BILL04 | Remove one cart item | Total updates correctly | PASS |

---

## 7. Database Tests

| ID | Test | Expected Result | Status |
|---|---|---|---|
| DB01 | Create database | Database created successfully | PASS |
| DB02 | Check menu table | Table exists | PASS |
| DB03 | Check customer table | Table exists | PASS |
| DB04 | Check order table | Table exists | PASS |
| DB05 | Check order_items table | Table exists | PASS |
| DB06 | Check menu indexes | Required indexes exist | PASS |
| DB07 | Check customer indexes | Required indexes exist | PASS |
| DB08 | Check order indexes | Required indexes exist | PASS |

---

## 8. Test Summary

| Category | Total Tests | Passed | Failed |
|---|---:|---:|---:|
| Functional | 14 | 14 | 0 |
| Q05 Performance | 12 | 12 | 0 |
| Input Validation | 5 | 5 | 0 |
| Billing Calculation | 4 | 4 | 0 |
| Database | 8 | 8 | 0 |
| **Total** | **43** | **43** | **0** |

---

## 9. Quality Verification

The test results indicate that the documented functional and Q05 checkpoints passed during project verification.

The following Q05 features were verified:

- Fast Search
- Quick Navigation
- Cached Dashboard
- DB Indexing
- Paginated Reports

---

## 10. Testing Approach

Testing combines:

1. Functional testing
2. Input validation testing
3. Database verification
4. Billing calculation testing
5. Q05 feature verification
6. Defect monitoring

Defects identified during the project are recorded separately in the Defect Log.

---

## 11. TQM Connection

Testing supports TQM through:

- **Customer Focus:** verifying useful and reliable billing operations.
- **Continuous Improvement:** using defects and test results to improve the system.
- **Fact-Based Decision Making:** using recorded test results and defect data.
- **Process-Centric Approach:** testing the complete billing workflow.
- **Poka-Yoke:** validating inputs before processing.

---

## 12. Conclusion

The test cases provide a structured method for verifying the Restaurant Billing System.

The documented test cases cover core billing operations, database functionality, input validation, billing calculations, and all five Q05 response-time features.