# Successfully Sent Messages

Find the ratio of successfully received messages to sent messages.

```
DataFrames: facebook_messages_sent, facebook_messages_received
```

```python
# Import your libraries
import pandas as pd

# Start writing code
facebook_messages_sent.head()

# ratio of received to sent

df_se = facebook_messages_sent.copy()
df_re = facebook_messages_received.copy()

len(df_re) / len(df_se)
```