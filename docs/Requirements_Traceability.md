# Requirements Traceability Matrix

## Restaurant Billing System – Q05: Reduce Response Time

## 1. Purpose

The Requirements Traceability Matrix (RTM) connects project requirements with their implementation and verification activities.

It helps ensure that important requirements are not missed during development and testing.

---

## 2. Traceability Matrix

| ID | Requirement | Implementation | Verification |
|---|---|---|---|
| R01 | Manage menu items | `database/db.py` + Menu UI | Menu functionality |
| R02 | Search menu items | Menu search + database query | Fast Search test |
| R03 | Manage customers | `database/db.py` + Customer UI | Customer functionality |
| R04 | Search customers | Customer search + database query | Fast Search test |
| R05 | Create restaurant orders | New Order interface + database | Order workflow |
| R06 | Calculate bill total | Order/cart calculation logic | Billing Calculation test |
| R07 | View order history | Order History interface | Order History verification |
| R08 | Generate sales reports | Reports interface + database query | Paginated Reports test |
| R09 | Provide quick navigation | Application navigation controls | Quick Navigation test |
| R10 | Improve dashboard response | Dashboard cache | Cached Dashboard test |
| R11 | Support database indexing | SQLite indexes | Database Integrity test |
| R12 | Validate user input | Quantity and price validation | Input Validation test |
| R13 | Analyze software risks | FMEA documentation | FMEA review |
| R14 | Analyze process flow | SIPOC documentation | SIPOC review |
| R15 | Identify quality requirements | CTQ Tree | CTQ review |
| R16 | Record defects | Defect Log | Defect review |
| R17 | Analyze defect categories | Pareto Analysis | Pareto review |
| R18 | Identify root causes | Fishbone Analysis | Fishbone review |
| R19 | Support continuous improvement | PDCA documentation | PDCA review |
| R20 | Reduce response time | Five Q05 features | Q05 verification |

---

## 3. Q05 Traceability

The assigned quality goal is:

**Q05 – Reduce Response Time**

### Q05-01 — Fast Search

**Requirement:** Search frequently used records efficiently.

**Implementation:**
- Menu search
- Customer search
- Database search functions
- Relevant database indexes

**Verification:**
- Fast Search test

---

### Q05-02 — Quick Navigation

**Requirement:** Allow users to move quickly between major application sections.

**Implementation:**
- Dashboard
- Menu
- Customers
- New Order
- Order History
- Reports
- Q05 Performance navigation

**Verification:**
- Quick Navigation test

---

### Q05-03 — Cached Dashboard

**Requirement:** Avoid unnecessary repeated dashboard data processing.

**Implementation:**
- Dashboard data retrieval
- Application-level dashboard cache
- Dashboard refresh mechanism

**Verification:**
- Cached Dashboard test

---

### Q05-04 — Database Indexing

**Requirement:** Support efficient retrieval for frequently accessed database fields.

**Implementation:**
- Menu indexes
- Customer indexes
- Order indexes
- Order-item indexes

**Verification:**
- Database Integrity test
- Database Index Verification documentation

---

### Q05-05 — Paginated Reports

**Requirement:** Display report information in manageable pages.

**Implementation:**
- Sales report retrieval
- Report navigation
- Pagination-related application logic

**Verification:**
- Paginated Reports test

---

## 4. TQM Traceability

| TQM Activity | Project Evidence |
|---|---|
| Customer Focus | CTQ Tree |
| Continuous Improvement | PDCA |
| Process-Centric Approach | SIPOC |
| Fact-Based Decision Making | Testing, Defect Log, Pareto |
| Poka-Yoke | Input Validation |
| Risk Analysis | FMEA |
| Statistical Quality Control | Pareto, Fishbone, Checksheet |

---

## 5. Review Traceability

| Review | Main Evidence |
|---|---|
| Review 1 | SRS, Architecture, Scope, CTQ |
| Review 2 | Base Billing System and Q05 Features |
| Review 3 | FMEA, SIPOC, CTQ, Defect Log |
| Review 4 | Pareto, Fishbone, Checksheet, PDCA |
| Final Demo | Working Application, Testing, Documentation |
| GitHub Health | README, commits, issues, documentation |

---

## 6. Traceability Flow

```text
Requirement
     |
     v
Design
     |
     v
Implementation
     |
     v
Testing
     |
     v
Quality Analysis
     |
     v
Continuous Improvement