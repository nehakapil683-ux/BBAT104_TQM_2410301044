# Pareto Analysis – Restaurant Billing System

## Project Information

| Field | Details |
|---|---|
| Project Title | Restaurant Billing System – Q05: Reduce Response Time |
| Student | Neha Kapil |
| Roll No. | 2410301044 |
| Branch | CSE |
| Section | A |
| Quality Goal | Q05 – Reduce Response Time |
| Review | Review 4 – SQC & Continuous Improvement |

---

# 1. Purpose

Pareto Analysis is a quality control technique used to identify the most
frequent categories of defects.

The principle is based on the idea that a relatively small number of causes
can account for a large proportion of observed problems.

For this project, the recorded defects from the Defect Log are grouped into
categories so that improvement efforts can focus on the areas contributing
most to the observed defects.

---

# 2. Defect Data

The following 10 defects were recorded during functional testing:

| Defect ID | Module | Defect Category |
|---|---|---|
| D01 | Menu | Search / Performance |
| D02 | Menu | Database / Data Integrity |
| D03 | Customers | Data Refresh |
| D04 | New Order | Input Validation |
| D05 | New Order | Input Validation |
| D06 | Dashboard | Data Refresh |
| D07 | Reports | Performance |
| D08 | Database | Database / Performance |
| D09 | Navigation | Navigation |
| D10 | Billing | Calculation |

---

# 3. Defect Category Frequency

The defects are grouped into the following categories:

| Rank | Defect Category | Frequency | Percentage | Cumulative Percentage |
|---:|---|---:|---:|---:|
| 1 | Input Validation | 2 | 20% | 20% |
| 2 | Performance | 2 | 20% | 40% |
| 3 | Database | 1 | 10% | 50% |
| 4 | Data Refresh | 2 | 20% | 70% |
| 5 | Search | 1 | 10% | 80% |
| 6 | Navigation | 1 | 10% | 90% |
| 7 | Calculation | 1 | 10% | 100% |

---

# 4. Pareto Calculation

Total number of recorded defects:

**10**

Percentage is calculated as:

```text
Percentage = (Category Frequency / Total Defects) × 100