# SIPOC – Restaurant Billing System

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

# 1. What is SIPOC?

SIPOC stands for:

**S – Suppliers**  
**I – Inputs**  
**P – Process**  
**O – Outputs**  
**C – Customers**

SIPOC provides a high-level view of the Restaurant Billing System process.

It helps identify where the required data comes from, how it is processed,
what outputs are produced, and who uses those outputs.

---

# 2. SIPOC Diagram

```text
┌─────────────────┐
│   SUPPLIERS     │
├─────────────────┤
│ Restaurant Staff│
│ Manager         │
│ Menu Data       │
│ Customer        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     INPUTS      │
├─────────────────┤
│ Menu Items      │
│ Customer Details│
│ Order Details   │
│ Quantity        │
│ Price            │
└────────┬────────┘
         │
         ▼
┌──────────────────────────┐
│         PROCESS          │
├──────────────────────────┤
│ 1. Manage Menu           │
│ 2. Search Menu           │
│ 3. Manage Customers      │
│ 4. Create Order          │
│ 5. Calculate Bill        │
│ 6. Store Order           │
│ 7. Generate Reports      │
│ 8. Display Dashboard     │
└────────────┬─────────────┘
             │
             ▼
┌─────────────────┐
│     OUTPUTS     │
├─────────────────┤
│ Generated Bill  │
│ Order Record    │
│ Sales Reports   │
│ Dashboard Data  │
│ Menu Information│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    CUSTOMERS    │
├─────────────────┤
│ Restaurant Staff│
│ Cashier         │
│ Manager         │
│ Restaurant Owner│
└─────────────────┘