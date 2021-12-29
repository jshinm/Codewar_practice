# Find the rate of processed tickets for each type

Find the rate of processed tickets for each type.

```
DataFrame: facebook_complaints
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
facebook_complaints.head()

# rate of ticket for each type
# processed - bool
# rate of processed ticket = processed / total

# 1. group by type and count processed
# 2. count that are true
# 3. return rate

df = facebook_complaints.groupby('type').agg({'processed': ['count', lambda x:x[x == True].count()]}).reset_index()
df.columns = ['type', 'total', 'count']
df['rate'] = df['count'] / df['total']
df[['type','rate']]
```