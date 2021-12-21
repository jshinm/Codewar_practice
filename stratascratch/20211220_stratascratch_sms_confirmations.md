# SMS Confirmations From Users

Facebook sends SMS texts when users attempt to 2FA (2-factor authenticate) into the platform to log in. In order to successfully 2FA they must confirm they received the SMS text message. Confirmation texts are only valid on the date they were sent. Unfortunately, there was an ETL problem with the database where friend requests and invalid confirmation records were inserted into the logs, which are stored in the 'fb_sms_sends' table. These message types should not be in the table. Fortunately, the 'fb_confirmers' table contains valid confirmation records so you can use this table to identify SMS text messages that were confirmed by the user.

Calculate the percentage of confirmed SMS texts for August 4, 2020.

```
DataFrames: fb_sms_sends, fb_confirmers
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
fb_sms_sends.head()
# fb_confirmers.head()

# fb_sms_sends contains invalid confirmation records
# fb_confirmers contains valid confirmation records
# calculate the % of confirmed sms text

# 1. filter out `fb_confirmers` and `fb_sms_sends` for date == 8/4/20
# 2. merge with `fb_sms_sends`
# 3. count all counts of unique phone #
# 4. count all confirmed counts
# 5. compute percentage

dfc = fb_confirmers.query('date == "2020-08-04"')
dfs = fb_sms_sends.query('ds == "2020-08-04"')

dfs = dfs[~dfs.isin(['confirmation','friend_request'])].dropna() #all counts of message

df_merge = pd.merge(dfc, dfs, how='right', on=['phone_number']) #there are matched and unmatched phone #

numer = (~df_merge['date'].isna()).sum() # number of valid count
denom = len(df_merge['date']) # number of all 

ans = (numer / denom) * 100

#output: there are 1 out of 5 phone number that were messaged that were also confirmed on 8-4-2020
```