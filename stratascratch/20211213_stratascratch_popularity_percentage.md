# Popularity Percentage

Find the popularity percentage for each user on Facebook. The popularity percentage is defined as the total number of friends the user has divided by the total number of users on the platform, then converted into a percentage by multiplying by 100.
Output each user along with their popularity percentage. Order records in ascending order by user id.

The 'user1' and 'user2' column are pairs of friends.

```
DataFrame: facebook_friends
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# find popularity percentage (total friend / total user * 100)
# ascending order by user_id

# 1. get the total # of users (by getting a unique id of all people)
# 2. get the total number of friend each user has
# 3. calculate the percentage
# 4. order by user_id

tmp = facebook_friends.loc[:,['user2', 'user1']]
tmp.columns = ['user1', 'user2']

df_fr = pd.concat([facebook_friends, tmp])

df_out = df_fr.groupby('user1').count().reset_index()
df_out['pp'] = df_out['user2']/len(df_out) * 100

df_out = df_out[['user1', 'pp']]
```