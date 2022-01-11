# Most Active Users On Messenger

Meta/Facebook Messenger stores the number of messages between users in a table named 'fb_messages'. In this table 'user1' is the sender, 'user2' is the receiver, and 'msg_count' is the number of messages exchanged between them.
Find the top 10 most active users on Meta/Facebook Messenger by counting their total number of messages sent and received. Your solution should output usernames and the count of the total messages they sent or received

```
DataFrame: fb_messages
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
fb_messages.head()

# user1 - sender; user2 - receiver; msg_count - # messages exchanged
# find top 10 most active users by total number of messages sent and received
# output - username, count of total messages sent or received

# 1. split count by each user (1 and 2)
# 2. concat table
# 3. groupby concatenated user and agg-sum(msg_cout)
# 4. output top 10 most active users

dfA = fb_messages[['user1', 'msg_count']]
dfB = fb_messages[['user2', 'msg_count']]

dfA.columns = ['user', 'count']
dfB.columns = ['user', 'count']

output = pd.concat([dfA, dfB]).groupby('user').sum().reset_index()
output = output.sort_values('count', ascending=False)
output.head(10)
```