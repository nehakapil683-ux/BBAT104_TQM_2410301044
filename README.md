# Restaurant Billing System – Q05: Reduce Response Time

A Python-based Restaurant Billing System developed as part of the **BBAT104 – Fundamentals of TQM** project.

The project focuses on **Q05: Reduce Response Time** by applying software quality and Total Quality Management (TQM) principles.

---

## Project Information

| Field | Details |
|---|---|
| Student | Neha Kapil |
| Roll No. | 2410301044 |
| Branch | CSE |
| Section | A |
| Course | BBAT104 – Fundamentals of TQM |
| Academic Session | 2026–27 |
| Baseline System | Restaurant Billing System |
| Quality Goal | Q05 – Reduce Response Time |

---

## Quality Goal – Q05

### Reduce Response Time

The system focuses on improving the speed and efficiency of frequently used billing operations.

### Five Q05 Features

1. **Fast Search**
2. **Quick Navigation**
3. **Cached Dashboard**
4. **DB Indexing**
5. **Paginated Reports**

---

## Key Features

### Restaurant Billing

- Menu management
- Customer management
- Order creation
- Shopping cart
- Bill generation
- Order history
- Sales reports

### Performance Improvements

- Fast prefix-based search
- Quick navigation between modules
- Dashboard caching
- Database indexing
- Paginated reports

### Quality & TQM

- FMEA with RPN
- SIPOC analysis
- CTQ Tree
- Defect Log
- Pareto Analysis
- Fishbone Analysis
- Checksheet
- PDCA Continuous Improvement

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Application development |
| Tkinter / CustomTkinter | GUI |
| SQLite3 | Database |
| Pandas | Data processing |
| Matplotlib | Data visualization |
| Git | Version control |
| GitHub | Project repository |

---

## Project Structure

```text
BBAT104_TQM_2410301044/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── reports/
│   ├── pareto_chart.py
│   └── pareto_chart.png
│
├── tqm/
│   └── __init__.py
│
├── tests/
│
├── docs/
│   ├── SRS.md
│   ├── architecture.md
│   ├── CTQ.md
│   ├── FMEA.md
│   ├── SIPOC.md
│   ├── CTQ_Tree.md
│   ├── Defect_Log.md
│   ├── Pareto_Analysis.md
│   ├── Fishbone_Analysis.md
│   ├── Checksheet.md
│   └── PDCA_Continuous_Improvement.md
│
├── assets/
├── README.md
├── requirements.txt
└── .gitignore