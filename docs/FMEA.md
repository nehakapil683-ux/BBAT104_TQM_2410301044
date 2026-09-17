# FMEA – Restaurant Billing System

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

# 1. Purpose of FMEA

Failure Mode and Effects Analysis (FMEA) is used to identify possible failures
in the Restaurant Billing System, understand their effects, identify possible
causes, and prioritize risks for improvement.

The main focus of this FMEA is the assigned quality goal:

**Q05 – Reduce Response Time**

The analysis covers the following five quality features:

1. Fast Search
2. Quick Navigation
3. Cached Dashboard
4. DB Indexing
5. Paginated Reports

---

# 2. FMEA Scoring Method

Each failure mode is evaluated using three factors:

- **Severity (S):** How serious the effect of the failure is.
- **Occurrence (O):** How frequently the failure may occur.
- **Detection (D):** How difficult it is to detect the failure.

The Risk Priority Number is calculated as:

**RPN = Severity × Occurrence × Detection**

### Rating Scale

| Rating | Severity | Occurrence | Detection |
|---|---|---|---|
| 1 | Very Low | Very Rare | Very Easy |
| 2 | Low | Rare | Easy |
| 3 | Low | Occasional | Relatively Easy |
| 4 | Moderate | Sometimes | Moderate |
| 5 | Moderate | Possible | Moderate |
| 6 | High | Frequent | Difficult |
| 7 | High | Very Frequent | More Difficult |
| 8 | Very High | Very Frequent | Very Difficult |
| 9 | Critical | Almost Certain | Very Difficult |
| 10 | Critical | Certain | Almost Impossible |

---

# 3. FMEA Table

| ID | Process / Feature | Potential Failure Mode | Potential Effect | Potential Cause | S | O | D | RPN | Recommended Action |
|---|---|---|---|---|---:|---:|---:|---:|---|
| F01 | Fast Search | Search returns results slowly | User waits longer to find menu items | Inefficient search query or large dataset | 6 | 5 | 5 | 150 | Use optimized prefix search and database indexing |
| F02 | Fast Search | Search returns incorrect results | User may select the wrong menu item | Incorrect search/filter logic | 7 | 3 | 5 | 105 | Test search with multiple valid and invalid inputs |
| F03 | Quick Navigation | Navigation takes too many steps | Reduced usability and increased task time | Poor page organization | 5 | 4 | 4 | 80 | Provide direct sidebar navigation |
| F04 | Quick Navigation | Navigation button does not open correct page | User cannot access required function quickly | Incorrect command binding | 7 | 3 | 4 | 84 | Test every navigation button |
| F05 | Cached Dashboard | Dashboard shows outdated values | User may see incorrect sales/order information | Cached data is not refreshed after changes | 8 | 4 | 6 | 192 | Invalidate cache after menu, customer and order changes |
| F06 | Cached Dashboard | Dashboard refresh is slow | Delay in viewing business information | Repeated database queries | 6 | 4 | 5 | 120 | Use dashboard caching and refresh only when required |
| F07 | DB Indexing | Required database index is missing | Search/report queries may become slower | Index not created during database setup | 7 | 4 | 6 | 168 | Create and verify indexes for frequently searched columns |
| F08 | DB Indexing | Query does not use expected index | Response time may not improve as expected | Query structure or database planner behavior | 7 | 3 | 7 | 147 | Check query plan using EXPLAIN QUERY PLAN |
| F09 | Paginated Reports | Report loads too many records at once | Report page becomes slower | No effective pagination | 7 | 5 | 5 | 175 | Display a limited number of records per page |
| F10 | Paginated Reports | Next/Previous page works incorrectly | User may not be able to view all report data | Pagination offset/count logic error | 6 | 3 | 5 | 90 | Test first, middle and last report pages |
| F11 | Order Processing | Order creation takes too long | Billing process is delayed | Multiple unnecessary database operations | 8 | 3 | 5 | 120 | Keep order transaction operations efficient |
| F12 | Order Processing | Order total is calculated incorrectly | Incorrect bill amount | Incorrect quantity/price/subtotal calculation | 9 | 2 | 4 | 72 | Validate calculations before saving the order |
| F13 | Menu Management | Menu search does not find existing item | User spends more time searching | Search input or filtering issue | 6 | 3 | 4 | 72 | Test exact and prefix search cases |
| F14 | Dashboard | Dashboard count is incorrect | Management receives incorrect summary information | Data not refreshed after database changes | 8 | 3 | 6 | 144 | Refresh/invalidate dashboard cache after data changes |
| F15 | Reports | Report displays incorrect total | Incorrect business analysis | Incorrect aggregation/query logic | 9 | 2 | 5 | 90 | Compare report totals with database totals |

---

# 4. RPN Interpretation

RPN is calculated using:

**RPN = Severity × Occurrence × Detection**

For example:

### F05 – Cached Dashboard

Severity = 8  
Occurrence = 4  
Detection = 6

**RPN = 8 × 4 × 6 = 192**

This indicates that stale dashboard information should receive attention
because it can affect the accuracy of displayed business information.

### F09 – Paginated Reports

Severity = 7  
Occurrence = 5  
Detection = 5

**RPN = 7 × 5 × 5 = 175**

This represents the risk associated with loading a large number of report
records without effective pagination.

### F07 – DB Indexing

Severity = 7  
Occurrence = 4  
Detection = 6

**RPN = 7 × 4 × 6 = 168**

This represents the risk of slower database operations when required indexes
are not available.

---

# 5. Risk Priority Categories

For this project, the following categories are used for prioritization:

| RPN Range | Risk Category | Action |
|---|---|---|
| 1–50 | Low | Monitor |
| 51–100 | Moderate | Review and improve |
| 101–150 | High | Improvement required |
| 151–200 | Very High | Priority improvement |
| 201–1000 | Critical | Immediate attention |

---

# 6. High-Priority Risks

The following identified risks have RPN values above 150:

| Failure ID | Feature | RPN | Improvement Focus |
|---|---|---:|---|
| F05 | Cached Dashboard | 192 | Cache invalidation and refresh |
| F09 | Paginated Reports | 175 | Limit records loaded per page |
| F07 | DB Indexing | 168 | Create and verify required indexes |

These risks should be monitored during testing and continuous improvement.

---

# 7. Recommended Preventive Actions

## 7.1 Fast Search

- Use optimized search queries.
- Use prefix-based search.
- Add indexes on frequently searched fields.
- Test search with valid and invalid inputs.
- Avoid unnecessary database operations.

## 7.2 Quick Navigation

- Keep navigation controls clearly visible.
- Provide direct access to major modules.
- Test every navigation button.
- Use consistent navigation across pages.

## 7.3 Cached Dashboard

- Store dashboard results temporarily.
- Avoid repeated database queries when data has not changed.
- Clear or invalidate cache after relevant data changes.
- Provide a refresh option.

## 7.4 DB Indexing

- Create indexes for frequently searched columns.
- Verify indexes using database metadata.
- Check query execution plans.
- Compare query behavior before and after optimization.

## 7.5 Paginated Reports

- Load only a limited number of records at a time.
- Provide Previous and Next navigation.
- Display the current page and total pages.
- Test first, middle and final pages.

---

# 8. Poka-Yoke Considerations

Poka-Yoke means mistake-proofing the process.

The Restaurant Billing System uses the following preventive controls:

1. Quantity is entered before adding an item to the cart.
2. Only available menu items are shown for new orders.
3. Menu price is obtained from the database.
4. Order totals are calculated by the system.
5. Required customer/menu selections are validated.
6. Database foreign-key constraints help maintain relationships.
7. Pagination prevents unnecessary loading of large report datasets.

These controls reduce the possibility of common user and data-entry errors.

---

# 9. FMEA Monitoring Plan

FMEA should not be treated as a one-time activity.

The risk table should be reviewed when:

- A new defect is discovered.
- A major feature is changed.
- Database structure is changed.
- Search or report performance changes.
- A customer/user reports a problem.
- A preventive action is implemented.

After an improvement is implemented, the Severity, Occurrence and Detection
ratings can be reviewed again and a new RPN can be calculated.

---

# 10. Conclusion

The FMEA identifies possible failure modes in the Restaurant Billing System
and evaluates their potential risks using Severity, Occurrence and Detection.

The analysis focuses particularly on the Q05 quality goal:

**Reduce Response Time**

The identified preventive actions focus on:

- Fast Search
- Quick Navigation
- Cached Dashboard
- DB Indexing
- Paginated Reports

FMEA provides a fact-based approach for identifying risks and selecting areas
for continuous quality improvement.