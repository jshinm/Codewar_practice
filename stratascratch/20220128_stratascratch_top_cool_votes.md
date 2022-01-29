# Top Cool Votes
Find the review_text that received the highest number of  'cool' votes.
Output the business name along with the review text with the highest numbef of 'cool' votes.

```
DataFrame: yelp_reviews
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()

# review_text that received highest # of cool votes 
# output - business_name, review_text with highest # of cool votes

# 1. select columns
# 2. order by 'cool'
# 3. get max cool
# 4. df.loc[find rows with max]

df = yelp_reviews
df = df[['business_name', 'review_text', 'cool']]
df = df.sort_values('cool', ascending=False)

cmax = df.cool.max()

out = df.loc[df.cool == cmax]
```