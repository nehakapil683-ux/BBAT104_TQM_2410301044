# Fishbone Analysis – Restaurant Billing System

## Project Information

- **Project:** Restaurant Billing System
- **Quality Goal:** Q05 – Reduce Response Time
- **Student:** Neha Kapil
- **Roll No:** 2410301044
- **Branch:** CSE
- **Section:** A

---

## 1. Purpose

Fishbone Analysis, also called Ishikawa Analysis, is used to identify possible root causes of defects and performance problems.

For this project, the analysis focuses on factors that can increase the response time of the Restaurant Billing System.

---

## 2. Problem Statement

### Main Problem

**Slow Response Time in Restaurant Billing System**

Slow response can affect:

- Menu search
- Customer search
- Dashboard loading
- Order processing
- Report generation
- Navigation between modules

---

## 3. Fishbone Categories

The possible causes are analyzed under six major categories:

1. People
2. Process
3. Technology
4. Database
5. Interface
6. Data

---

## 4. Fishbone Cause Analysis

### 4.1 People

Possible causes:

- User enters incomplete or incorrect information.
- User performs repeated searches.
- User is unfamiliar with the billing workflow.
- Manual data entry increases processing time.

### 4.2 Process

Possible causes:

- Unnecessary steps during billing.
- Non-optimized search process.
- Loading complete reports instead of smaller pages.
- Repeated database operations.
- Lack of systematic performance monitoring.

### 4.3 Technology

Possible causes:

- Unoptimized application logic.
- Repeated calculations.
- Unnecessary UI refresh operations.
- Large amount of data loaded at once.
- Inefficient processing of reports.

### 4.4 Database

Possible causes:

- Missing database indexes.
- Inefficient database queries.
- Searching through unnecessary records.
- Loading complete datasets instead of required records.
- Repeated database access.

### 4.5 Interface

Possible causes:

- Too many navigation steps.
- Delayed screen refresh.
- Unclear placement of frequently used actions.
- Large tables displayed at once.
- Slow report navigation.

### 4.6 Data

Possible causes:

- Large number of menu items.
- Large customer records.
- Large order history.
- Large reports.
- Duplicate or unnecessary records.

---

## 5. Fishbone Diagram

```text
                         Slow Response Time
                                |
        -------------------------------------------------
        |             |             |          |        |
      People        Process      Technology  Database Interface
        |             |             |          |        |
   - Training    - Extra steps  - UI refresh - No     - Slow
   - Data entry  - Full reports - Repeated     index    navigation
   - Repeated    - Repeated       calculations - Slow  - Large tables
     searches      operations   - Large load    query - Delayed refresh
        |             |             |          |        |
        -------------------------------------------------
                                |
                              Data
                                |
                     - Large menu records
                     - Large customer data
                     - Large order history
                     - Large reports