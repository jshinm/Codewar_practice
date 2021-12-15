# Risky Projects

Identify projects that are at risk for going overbudget. A project is considered to be overbudget if the cost of all employees assigned to the project is greater than the budget of the project. 

You'll need to prorate the cost of the employees to the duration of the project. For example, if the budget for a project that takes half a year to complete is $10K, then the total half-year salary of all employees assigned to the project should not exceed $10K. Salary is defined on a yearly basis, so be careful how to calculate salaries for the projects that last less or more than one year.

Output a list of projects that are overbudget with their project name, project budget, and prorated total employee expense (rounded to the next dollar amount).

```
DataFrames: linkedin_projects, linkedin_emp_projects, linkedin_employees
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
linkedin_projects.head()
linkedin_emp_projects.head()
linkedin_employees.head()

# identify risk projects for overbudget
# overbudget is when cost of all employee for the project > the budget for the project
# prorate salary (ie match the salary according to the duration of the project)
# output - project_name, project_budget, prorated_total_expenses of all employee

# 1. join emp and employee tables
# 2. filter columns
# 3. group by project_id then sum(salary)
# 4. join result with linkedin projects
# 5. filter columns
# 6. new bool column (total prorate > budget)
# 7. filter for bool == true

# merge two tables
df = pd.merge(linkedin_emp_projects, linkedin_employees, left_on='emp_id', right_on='id')

# filter columns
df = df[['project_id', 'salary']]

# get total salary
df = df.groupby('project_id').sum().reset_index()

# merge result with project table
df_all = pd.merge(df, linkedin_projects, left_on='project_id', right_on='id')

# get the time diff
df_all['dt'] = df_all['end_date'] - df_all['start_date'] #/ (3600*24)
df_all['dt'] = df_all['dt'].apply(lambda x:x.days / 365)

# get prorated salary
df_all['psal'] = df_all['salary'] * df_all['dt']

# conditional filter
df_all = df_all.query('psal > budget')[['title', 'budget', 'psal']]

# round to the next dollar amount
df_all['psal'] = round(df_all.psal)

df_all
```