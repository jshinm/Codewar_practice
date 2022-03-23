# Distances Traveled

Find the top 10 users that have traveled the greatest distance. Output their id, name and a total distance traveled.

```
DataFrames: lyft_rides_log, lyft_users
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# top 10 users that travled the greatest distance
# output: id, name, total dist

# 1. join two tables
# 2. group by name, sum distance
# 3. order by distance
# 4. get first 10

# Start writing code

dfa = lyft_rides_log.copy()[['user_id','distance']]
dfb = lyft_users.copy()

dft = dfa.groupby('user_id').sum().reset_index()
dft = pd.merge(dft, dfb, left_on='user_id', right_on='id')[['user_id', 'distance','name']]

dft['rank'] = dft['distance'].rank(method='dense', ascending=False)
dft.sort_values('rank').query('rank < 11')
```