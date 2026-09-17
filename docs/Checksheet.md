# Checksheet – Restaurant Billing System

## Project Information

- **Project:** Restaurant Billing System
- **Quality Goal:** Q05 – Reduce Response Time
- **Student:** Neha Kapil
- **Roll No:** 2410301044
- **Branch:** CSE
- **Section:** A

---

## 1. Purpose

A Checksheet is used to systematically record defects and verify whether the implemented quality features are working correctly.

For Q05, the checksheet focuses on response-time-related features.

---

## 2. Q05 Quality Features

The five quality features being monitored are:

1. Fast Search
2. Quick Navigation
3. Cached Dashboard
4. DB Indexing
5. Paginated Reports

---

## 3. Q05 Feature Checksheet

| S.No. | Feature | Checkpoint | Expected Result | Status |
|---|---|---|---|---|
| 1 | Fast Search | Search menu item by name | Matching records appear quickly | PASS |
| 2 | Fast Search | Search customer by name | Matching customers appear quickly | PASS |
| 3 | Quick Navigation | Open Dashboard | Dashboard opens directly | PASS |
| 4 | Quick Navigation | Open Menu | Menu page opens directly | PASS |
| 5 | Quick Navigation | Open Customers | Customer page opens directly | PASS |
| 6 | Quick Navigation | Open New Order | Order page opens directly | PASS |
| 7 | Cached Dashboard | Open dashboard repeatedly | Cached data reduces repeated loading | PASS |
| 8 | DB Indexing | Check menu indexes | Search-related indexes exist | PASS |
| 9 | DB Indexing | Check customer indexes | Customer search indexes exist | PASS |
| 10 | DB Indexing | Check order indexes | Order-related indexes exist | PASS |
| 11 | Paginated Reports | Open reports | Records are loaded page-wise | PASS |
| 12 | Paginated Reports | Move to next page | Next records load correctly | PASS |
| 13 | Paginated Reports | Move to previous page | Previous records load correctly | PASS |

---

## 4. Defect Recording Sheet

| Defect ID | Date | Module | Defect Category | Description | Severity | Status |
|---|---|---|---|---|---|---|
| D01 | 2026-09-13 | Menu | Input Validation | Invalid menu input | Medium | Closed |
| D02 | 2026-09-13 | Customer | Input Validation | Invalid customer input | Medium | Closed |
| D03 | 2026-09-13 | Dashboard | Data Refresh | Dashboard data not refreshed | Medium | Closed |
| D04 | 2026-09-13 | Reports | Performance | Report loading delay | High | Closed |
| D05 | 2026-09-13 | Menu | Search | Slow/unoptimized search | Medium | Closed |
| D06 | 2026-09-13 | Navigation | Navigation | Extra navigation step | Low | Closed |
| D07 | 2026-09-13 | Database | Database | Missing/required index | High | Closed |
| D08 | 2026-09-13 | Dashboard | Data Refresh | Repeated dashboard query | Medium | Closed |
| D09 | 2026-09-13 | Reports | Performance | Large report loading | High | Closed |
| D10 | 2026-09-13 | Billing | Calculation | Billing calculation issue | Medium | Closed |

---

## 5. Defect Category Frequency

| Category | Frequency |
|---|---:|
| Input Validation | 2 |
| Performance | 2 |
| Data Refresh | 2 |
| Database | 1 |
| Search | 1 |
| Navigation | 1 |
| Calculation | 1 |
| **Total** | **10** |

---

## 6. Monitoring Checklist

| Monitoring Area | Check |
|---|---|
| Menu Search | Search results appear without unnecessary delay |
| Customer Search | Customer records are retrieved efficiently |
| Navigation | Main modules are directly accessible |
| Dashboard | Cached data prevents unnecessary repeated loading |
| Database | Required indexes are available |
| Reports | Records are displayed page-wise |
| Billing | Total calculation is correct |
| Input | Invalid data is controlled |
| Defects | Defects are recorded systematically |

---

## 7. TQM Connection

### Fact-Based Decision Making

Defects are recorded using measurable categories and frequencies.

### Continuous Improvement

Recorded defects are analyzed and corrective actions are applied.

### Customer Focus

The checksheet verifies features that improve the speed and usability of the billing system.

### Process-Centric Approach

Different stages of the billing process are monitored systematically.

### Poka-Yoke

Input validation helps prevent incorrect data from entering the system.

---

## 8. Conclusion

The Checksheet provides a structured method for monitoring defects and Q05 quality features.

The recorded data can be used for:

- Pareto Analysis
- Fishbone Analysis
- Root Cause Analysis
- Continuous Improvement
- PDCA implementation

The Q05 features are monitored using defined checkpoints and expected results.