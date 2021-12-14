# Users By Avg Session time

Calculate each user's average session time. A session is defined as the time difference between a page_load and page_exit. For simplicity, assume an user has only 1 session per day and if there are multiple of the same events in that day, consider only the latest page_load and earliest page_exit. Output the user_id and their average session time.

```
DataFrame: facebook_web_log
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
facebook_web_log.head()

# avg session time: avg(page_load - page_exit)
# there will only be 1 session per day per user (there are multiple dates per user)
# thus only consider the latest page_load and earliest page_exit
# output user_id and avg(session time)

# 1. make two dfs for ['page_load', 'page_exit'] on 'action' column
# 2. group by user_id and get the min or max of the timestamp for corresponding action
# 3. merge two dfs
# 5. subtract timestamp to get session time
# 6. take average of session time
# 7. output user_id and the avg

df_ld = facebook_web_log[facebook_web_log.action == 'page_load']
df_ex = facebook_web_log[facebook_web_log.action == 'page_exit']

df_ld['ts'] = df_ld.timestamp.apply(lambda x:x.date())
df_ex['ts'] = df_ex.timestamp.apply(lambda x:x.date())

df_ld = df_ld.groupby(['user_id', 'ts']).max().reset_index()
df_ex = df_ex.groupby(['user_id', 'ts']).min().reset_index()

df_merge = pd.merge(df_ld, df_ex, how='left', left_on=['user_id', 'ts'], right_on=['user_id','ts'])
df_merge = df_merge.dropna(how='any')

df_out = df_merge[['user_id']]
df_out.avg = df_merge['timestamp_y'] - df_merge['timestamp_x'] #output as datetime
df_out.avg = df_out['avg'].apply(lambda x:x.total_seconds()) #by default output as total_seconds
df_out.groupby(by='user_id').mean().reset_index()
```