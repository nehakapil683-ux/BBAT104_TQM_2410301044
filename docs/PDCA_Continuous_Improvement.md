# PDCA Continuous Improvement – Restaurant Billing System

## Project Information

- **Project:** Restaurant Billing System
- **Quality Goal:** Q05 – Reduce Response Time
- **Student:** Neha Kapil
- **Roll No:** 2410301044
- **Branch:** CSE
- **Section:** A

---

## 1. Introduction

PDCA stands for:

- **P – Plan**
- **D – Do**
- **C – Check**
- **A – Act**

PDCA is a continuous improvement cycle used to identify problems, implement improvements, check results, and standardize successful solutions.

For this project, PDCA is applied to the Q05 quality goal:

**Reduce Response Time**

---

# 2. PLAN

## Problem

The Restaurant Billing System may experience delays during:

- Menu search
- Customer search
- Dashboard loading
- Database retrieval
- Report generation
- Navigation

## Objective

Reduce unnecessary processing and improve the response time of the billing system.

## Planned Improvements

| Problem | Planned Solution |
|---|---|
| Slow menu search | Fast Search |
| Slow customer search | Fast Search |
| Repeated dashboard queries | Cached Dashboard |
| Slow database retrieval | DB Indexing |
| Multiple navigation steps | Quick Navigation |
| Large report loading | Paginated Reports |

## Quality Target

The system should provide quick access to frequently used functions and avoid unnecessary processing.

---

# 3. DO

The planned improvements are implemented in the system.

## 3.1 Fast Search

Prefix-based search is used for menu and customer records.

Example:

```text
Search: "Chi"
Result: "Chicken Biryani"