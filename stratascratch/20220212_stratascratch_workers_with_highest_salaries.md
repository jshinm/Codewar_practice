# Workers With The Highest Salaries

Find the titles of workers that earn the highest salary. Output the highest-paid title or multiple titles that share the highest salary.

```
DataFrames: worker, title
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
worker.head()

# title of worker with highest salary
# output - highest-paid title

# 1. get col of interest
# 2. get highest from worker
# 3. join worker with title

dfw = worker[['worker_id', 'salary']]
dft = title[['worker_ref_id', 'worker_title']]

df = pd.merge(dfw[dfw.salary == dfw.salary.max()], dft, left_on='worker_id', right_on='worker_ref_id')
```