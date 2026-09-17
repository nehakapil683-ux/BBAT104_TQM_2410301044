# Q05 Quality Metrics – Reduce Response Time

## Project Information

- **Project:** Restaurant Billing System
- **Quality Goal:** Q05 – Reduce Response Time
- **Branch:** CSE
- **Section:** A

## Objective

The objective of Q05 is to improve the responsiveness of the Restaurant Billing System so that common user operations can be completed quickly and efficiently.

## Q05 Quality Features

### 1. Fast Search

Search operations use database-supported prefix searching to reduce unnecessary records being processed.

**Measurement:**
- Search response time
- Number of records returned
- Search usability

### 2. Quick Navigation

The application provides direct navigation buttons for major modules.

**Measurement:**
- Number of clicks required to reach a module
- Navigation response
- User workflow simplicity

### 3. Cached Dashboard

Dashboard information is temporarily cached to avoid unnecessary repeated database calculations.

**Measurement:**
- Dashboard loading time
- Cache refresh behavior
- Data freshness after refresh

### 4. DB Indexing

Indexes are created for frequently searched and filtered database columns.

**Measurement:**
- Query execution behavior
- Indexed columns
- Search and report response

### 5. Paginated Reports

Reports display a limited number of records per page instead of loading the complete dataset at once.

**Measurement:**
- Records displayed per page
- Page navigation response
- Report loading behavior

## Quality Metrics

| Metric | Purpose | Target |
|---|---|---|
| Search Response | Measure search performance | Fast response |
| Dashboard Load | Measure dashboard performance | Fast loading |
| Navigation Response | Measure navigation usability | Immediate response |
| Report Load | Measure report performance | Controlled loading |
| Database Query | Measure database efficiency | Indexed queries |
| Page Navigation | Measure pagination performance | Quick page changes |

## Measurement Approach

Performance improvements are evaluated by comparing the behavior of the system before and after applying Q05 techniques.

The main areas considered are:

1. Search operations
2. Dashboard loading
3. Navigation
4. Database queries
5. Report loading
6. Pagination

## TQM Connection

Q05 supports the following TQM principles:

- **Customer Focus:** Faster operations improve the user experience.
- **Continuous Improvement:** Performance is reviewed and improved continuously.
- **Process-Centric Approach:** Response time is considered across important workflows.
- **Fact-Based Decision Making:** Quality decisions are supported by measurable performance observations.
- **Poka-Yoke:** Efficient workflows reduce unnecessary user actions and waiting.

## Acceptance Criteria

The Q05 implementation is considered successful when:

- Search remains responsive for available menu and customer records.
- Main modules can be accessed directly through navigation controls.
- Dashboard data can be loaded efficiently using caching.
- Database indexes are available for frequently used queries.
- Reports are divided into manageable pages.
- The implemented features work without affecting billing functionality.

## Conclusion

The Q05 quality goal applies performance-focused techniques throughout the Restaurant Billing System. Fast Search, Quick Navigation, Cached Dashboard, DB Indexing, and Paginated Reports work together to improve system responsiveness and usability.
