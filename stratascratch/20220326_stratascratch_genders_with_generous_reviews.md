# Gender With Generous Reviews

Write a query to find which gender gives a higher average review score when writing reviews as guests. Use the `from_type` column to identify guest reviews. Output the gender and their average review score.

```
DataFrames: airbnb_reviews, airbnb_guests
Expected Output Type: pandas.Series
```

```python
# Import your libraries
import pandas as pd

# find gender that gives a higher avg review score when written as guest (use from_type col)
# output - gender, avg review score

# 1. filter col to get only the guest
# 2. join two table
# 3. group by gender, get avg(review score)
# 4. order by avg review score and take the first row

# Start writing code
dfa = airbnb_reviews.copy()
dfb = airbnb_guests.copy()

dfa = dfa.query('from_type == "guest"')[['from_user', 'review_score']]
dfb = dfb[['guest_id', 'gender']]

dft = pd.merge(dfa, dfb, left_on='from_user', right_on='guest_id')

df_out = dft.groupby('gender').mean().reset_index()
df_out[['gender', 'review_score']].sort_values('review_score', ascending=False)[:1]
```