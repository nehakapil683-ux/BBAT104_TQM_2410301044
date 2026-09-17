# CTQ Tree – Restaurant Billing System

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

# 1. What is a CTQ Tree?

CTQ stands for **Critical to Quality**.

A CTQ Tree converts customer requirements into measurable quality
requirements.

The structure used in this project is:

**Customer Need → Quality Driver → Measurable Requirement**

---

# 2. Main Customer Need

## Customer Need

**Fast and responsive Restaurant Billing System**

The system should allow restaurant staff to perform common billing tasks
quickly and efficiently.

---

# 3. CTQ Tree

```text
                         CUSTOMER NEED
                              │
                              ▼
                Fast & Responsive Billing System
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
      Fast Search       Easy Navigation      Fast Dashboard
          │                   │                   │
          ▼                   ▼                   ▼
    Search response      Fewer steps to       Avoid repeated
    should be quick      access modules       database queries
          │                   │                   │
          ▼                   ▼                   ▼
      Prefix search       Sidebar menu        Dashboard cache
      + DB index
          
          ┌───────────────────┴───────────────────┐
          │                                       │
          ▼                                       ▼
    Fast Database                         Fast Reports
       Queries                                  │
          │                                       ▼
          ▼                              Limited records
    Proper indexes                         per page
          │                                       │
          ▼                                       ▼
   Efficient query                         Pagination
       execution