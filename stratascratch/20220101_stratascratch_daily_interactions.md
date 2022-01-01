# Daily Interactions By Users Count

Find the number of interactions along with the number of people involved with them on a given day. Output the date along with the number of interactions and people. Order results based on the date in ascending order and the number of people in descending order.

```
DataFrame: facebook_user_interactions
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
facebook_user_interactions.head()

# number of interactions and people involved on a given day
# output - date, interaction, people
# order - date (ascending), people (descending)

# 1. group by day and count each row
# 2. group by day and count unique id
# 3. order by day

df = facebook_user_interactions.copy()

# interaction counts by given date
out = df.groupby('day').count()['user1'].reset_index()

# people counts by given date
tmp = df.groupby('day').agg(['unique'])
out['people'] = tmp.apply(lambda x: len(set(x.user1['unique'].tolist()+x.user2['unique'].tolist())), axis=1)

# renaming columns
out.columns = ['day', 'interaction', 'people']
out
```