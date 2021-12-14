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
```