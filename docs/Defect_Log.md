# Defect Log & Checksheet – Restaurant Billing System

## Project Information

| Field | Details |
|---|---|
| Project Title | Restaurant Billing System – Q05: Reduce Response Time |
| Student | Neha Kapil |
| Roll No. | 2410301044 |
| Branch | CSE |
| Section | A |
| Quality Goal | Q05 – Reduce Response Time |
| Review | Review 3 – FMEA & Risk Audit |

---

# 1. Purpose

The Defect Log is used to record defects identified during testing of the
Restaurant Billing System.

It provides a structured record of:

- Defect identification
- Defect description
- Severity
- Status
- Corrective action
- Verification

The log supports fact-based decision making and continuous improvement.

---

# 2. Defect Status

| Status | Meaning |
|---|---|
| Open | Defect has been identified and requires action |
| In Progress | Corrective action is being implemented |
| Fixed | Corrective action has been completed |
| Verified | Fix has been tested successfully |
| Closed | Defect is resolved and no further action is required |

---

# 3. Defect Severity

| Severity | Description |
|---|---|
| Low | Minor issue with limited effect |
| Medium | Issue affects a function but has a workaround |
| High | Issue significantly affects system operation |
| Critical | Issue prevents an important system operation |

---

# 4. Defect Log

| Defect ID | Module | Defect Description | Severity | Status | Corrective Action |
|---|---|---|---|---|---|
| D01 | Menu | Search result did not initially update as expected | Medium | Fixed | Added search event handling and database search |
| D02 | Menu | Menu item could not be removed when related order records existed | Medium | Fixed | Added error handling for database relationship restriction |
| D03 | Customers | Customer list required refresh after adding a customer | Low | Fixed | Refresh customer data after successful insertion |
| D04 | New Order | Invalid quantity could affect cart entry | High | Fixed | Added quantity validation |
| D05 | New Order | Unavailable menu items should not be selectable | High | Fixed | Load only available menu items |
| D06 | Dashboard | Dashboard values could become outdated after database changes | High | Fixed | Invalidate dashboard cache after relevant changes |
| D07 | Reports | Large report datasets could increase loading time | High | Fixed | Implemented report pagination |
| D08 | Database | Missing indexes could affect frequently searched operations | High | Fixed | Added indexes to frequently queried columns |
| D09 | Navigation | Incorrect navigation command could open the wrong module | Medium | Fixed | Verified navigation commands |
| D10 | Billing | Incorrect total calculation could produce an incorrect bill | Critical | Fixed | Validate quantity, price and subtotal calculations |

---

# 5. Q05 Defect Checksheet

The following checks are performed for the assigned quality goal.

| Check | Test Condition | Result |
|---|---|---|
| C01 | Search menu item by prefix | Pass |
| C02 | Search for non-existing menu item | Pass |
| C03 | Navigate between all major modules | Pass |
| C04 | Dashboard displays summary information | Pass |
| C05 | Dashboard refreshes after relevant data changes | Pass |
| C06 | Required database indexes exist | Pass |
| C07 | Database query plan can be inspected | Pass |
| C08 | Reports display limited records per page | Pass |
| C09 | Previous page control works | Pass |
| C10 | Next page control works | Pass |
| C11 | Order can be created successfully | Pass |
| C12 | Bill total is calculated correctly | Pass |

---

# 6. Q05 Quality Feature Verification

## Fast Search

**Test:** Enter a menu item prefix in the search field.

**Expected Result:** Matching menu items should be displayed.

**Observed Result:** Pass.

---

## Quick Navigation

**Test:** Open each module using the navigation menu.

**Expected Result:** The selected module should open directly.

**Observed Result:** Pass.

---

## Cached Dashboard

**Test:** Open dashboard and perform relevant data changes.

**Expected Result:** Dashboard should be refreshed when relevant data changes,
while unnecessary repeated database queries are reduced through caching.

**Observed Result:** Pass.

---

## DB Indexing

**Test:** Inspect database indexes and query plan.

**Expected Result:** Required indexes should be available for frequently
queried columns.

**Observed Result:** Pass.

---

## Paginated Reports

**Test:** Open reports and navigate between pages.

**Expected Result:** Only a limited number of records should be displayed at
one time and navigation should work correctly.

**Observed Result:** Pass.

---

# 7. Defect Recording Process

The following process is used whenever a defect is identified:

```text
Identify Defect
      ↓
Record Defect
      ↓
Assign Severity
      ↓
Analyze Possible Cause
      ↓
Implement Corrective Action
      ↓
Retest
      ↓
Verify Fix
      ↓
Close Defect