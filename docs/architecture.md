# SYSTEM ARCHITECTURE

## Restaurant Billing System – Q05

```text
+----------------------+
|      USER / STAFF    |
+----------+-----------+
           |
           v
+----------------------+
|     GUI INTERFACE    |
|      (Tkinter)       |
+----------+-----------+
           |
           v
+----------------------+
|   APPLICATION LOGIC  |
+----------+-----------+
           |
     +-----+-----+
     |           |
     v           v
+---------+   +----------------+
| Billing |   | Q05 Performance|
| Module  |   | Features       |
+---------+   +-------+--------+
                     |
       +-------------+-------------+
       |             |             |
       v             v             v
  Fast Search   Cached          Quick
                Dashboard      Navigation
       |
       v
+----------------------+
|    SQLite Database   |
|  + Database Indexes  |
+----------+-----------+
           |
           v
+----------------------+
|   Reports Module     |
|  Paginated Reports  |
+----------------------+

          TQM / SQC Layer
                 |
     +-----------+-----------+
     |           |           |
     v           v           v
    FMEA       Defect      PDCA
               Log