# Average Salaries

Compare each employee's salary with the average salary of the corresponding department.

Output the department, first name, and salary of employees along with the average salary of that department.

```
DataFrame: employee
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
employee.head()

# compare ind. salary with the avg salary of the dep
# output - department, first name, salary, avg sal of the dep

# 1. filter out unwanted col (df1)
# 2. group by(dep) - agg(avg(sal))
# 3. save as new col (df2)
# 4. concat df1 + df2

df1 = employee[['department', 'first_name', 'salary']]
df2 = df1.groupby('department').mean().reset_index()
out = pd.merge(df1, df2, on='department')
```