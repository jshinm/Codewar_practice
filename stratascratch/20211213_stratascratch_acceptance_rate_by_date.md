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

#rate of acceptances by the date (acceptance / total)
#sort by ascending order

#it's looking for the rate from the sender's perspective
#thus, the date at which the request was accepted is not important

dfs = fb_friend_requests[fb_friend_requests.action.isin(['sent'])]
dfa = fb_friend_requests[fb_friend_requests.action.isin(['accepted'])]

ref_col = list(dfs.columns[:2]) #reference columns to join on

df_comb = pd.merge(dfs, dfa, how='left', left_on=ref_col, right_on=ref_col)

#at this stage, separate count for sent and accepted are grouped by sent date
#reset_index is to show date_x in the stratascratch platform
df_out = df_comb.groupby(by='date_x').count().reset_index()

#calculating rates
df_out['rate'] = df_out['action_y']/df_out['action_x']

#cleaning output
df_out = df_out[['date_x', 'rate']]
df_out.sort_values(by='date_x', ascending=True)
```