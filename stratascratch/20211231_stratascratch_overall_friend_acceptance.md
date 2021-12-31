# Find the overall friend acceptance count for a given date

Find the overall friend acceptance count for a given date.
Assume the date is 2nd of January 2019.

```
DataFrame: facebook_friendship_requests
Expected Output Type: int
```

```python
# Import your libraries
import pandas as pd

# Start writing code
facebook_friendship_requests.head()

# Import your libraries
import pandas as pd

# Start writing code
facebook_friendship_requests.head()

# get the overall friend acceptance for 1/2/2019

# 1. get date_approved != NaN
# 2. filter date
# 3. count rows

df = facebook_friendship_requests

df = df[~df.date_approved.isna()]
df = df[df.date_approved == '2019-01-02']
len(df)
```