# Finding User Purchases

Write a query that'll identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active users.

```
DataFrame: amazon_transactions
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
amazon_transactions.head()

# find a returning user (who purchased for the second time within 7 days)
# output the list of user ids

# 1. group by user_id
# 2. find the datediff of the purchase dates
# 3. find ids that has datediff <= 7 days

# it's important to sort values by date
df = amazon_transactions[['user_id', 'created_at']].sort_values('created_at')

# the diff method basically calculates diff of each row (thus the first row is nan)
# then the diff of datetime needs to be converted to days for numeric comparison
df['diff'] = df.groupby(by='user_id')['created_at'].diff().apply(lambda x: x.days)

# filter out and output user_id
df[df['diff'] <= 7]['user_id'].drop_duplicates()
```