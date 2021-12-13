# Acceptance Rate By Date

What is the overall friend acceptance rate by date? Your output should have the rate of acceptances by the date the request was sent. Order by the earliest date to latest.

Assume that each friend request starts by a user sending (i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver) that's logged in the table with action = 'sent'. If the request is accepted, the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.

```
DataFrame: fb_friend_requests
Expected Output Type: pandas.DataFrame
```

```
fb_friend_requests
    user_id_sender  object
    user_id_receiver    object
    date    datetime64[ns]
    action  object
```

```python
# Import your libraries
import pandas as pd

# Start writing code
fb_friend_requests.head()
```