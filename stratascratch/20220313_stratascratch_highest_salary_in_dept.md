# Highest Salary In Department

Find the employee with the highest salary per department.
Output the department name, employee's first name along with the corresponding salary.

```
DataFrame: employee
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# employee w/ highest salary per dept
# output - dept name, first name, corresponding salary

# 1. filter col
# 2. group by dept
# 3. filter highest salary per dept only

# groupby followed by max does not return right records
df = employee[['first_name', 'department', 'salary']]
df = df.groupby('department', as_index=False).salary.max() #as_index replaces reset_index()
df.merge(employee, how='left', on=['department', 'salary'])[['department', 'salary', 'first_name']]
```