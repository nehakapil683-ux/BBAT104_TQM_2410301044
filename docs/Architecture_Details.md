# Architecture Details

## Restaurant Billing System – Q05: Reduce Response Time

## 1. Architecture Overview

The Restaurant Billing System follows a simple layered architecture.

```text
+-----------------------------+
|       User Interface        |
|     CustomTkinter / Tkinter |
+-------------+---------------+
              |
              v
+-----------------------------+
|      Application Logic      |
|       app/main.py           |
+-------------+---------------+
              |
              v
+-----------------------------+
|       Database Layer        |
|       database/db.py        |
+-------------+---------------+
              |
              v
+-----------------------------+
|         SQLite3             |
|        Database             |
+-----------------------------+