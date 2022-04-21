# Rank Variance Per Country

Which countries have risen in the rankings based on the number of comments between Dec 2019 vs Jan 2020? Hint: Avoid gaps between ranks when ranking countries.

```
DataFrames: fb_comments_count, fb_active_users
Expected Output Type: pandas.DataFrame
```

```python
# risen in rankings from pre-12/2019 based on the number comments

# 1. filter cols
# 2. join tables
# 3. group by country + sum(num comments) pre-12/2019
# 4. do the same for 12/2019 - 1/2020
# 5. compare the rank + find countries rose in rank

# Import your libraries
import pandas as pd

# Start writing code
dfA = fb_comments_count
dfB = fb_active_users[['user_id', 'country']]

df_tmp = pd.merge(dfA, dfB, on='user_id')
df_tmp['year'] = df_tmp.created_at.apply(lambda x: x.year)
df_tmp['month'] = df_tmp.created_at.apply(lambda x: x.month)
df_tmp
df_out = df_tmp.groupby(['country', 'year', 'month']).sum().reset_index()

df_out_2019 = df_out.query('year == 2019 and month == 12')
df_out_2019['rank19'] = df_out_2019.number_of_comments.rank(method='dense')
df_out_2019 = df_out_2019[['country', 'rank19']]

df_out_2020 = df_out.query('year == 2020 and month == 1')
df_out_2020['rank20'] = df_out_2020.number_of_comments.rank(method='dense')
df_out_2020 = df_out_2020[['country', 'rank20']]

#returns no row - we can see that there aren't countries that rose in rank within the overlapping country
pd.merge(df_out_2019, df_out_2020, on='country', how='inner').query('rank19 > rank20')['country']

#we can see from this list that there are 1 country from 2019 list that showed up in the 2020 list which ranks first place, thus that country is determined to be the answer
pd.merge(df_out_2019, df_out_2020, on='country', how='outer')
```