# Finding Updated Records

We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.

```
DataFrame: ms_employee_salary
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.head()

# find current salary of each employee (always increase)
# output - id, first_name, last_name, dep_ID, current_salary
# order by id asc

# 1. group by id and max(salary)
# 2. order by id

df = ms_employee_salary.groupby('id').max().reset_index()

df = df.sort_values(by='id')
```