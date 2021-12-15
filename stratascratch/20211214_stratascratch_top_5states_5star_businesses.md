# Top 5 States With 5 Star Businesses

Find the top 5 states with the most 5 star businesses. Output the state name along with the number of 5-star businesses and order records by the number of 5-star businesses in descending order. In case there are ties in the number of businesses, return all the unique states. If two states have the same result, sort them in alphabetical order.

```
DataFrame: yelp_business
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

# find top 5 states with the most number of 5 star business
# output - state_name, number of 5-star business
# order by descending order of the number of 5-star
# if multiple winners, sort by alphabetical order

# 1. filter out columns and for stars == 5
# 2. group by state and count(star)
# 3. sort by sum desc then sort by state alpha

df = yelp_business[['state', 'stars']]
df = df[df['stars'] == 5]

df = df.groupby('state').count()

df = df.sort_values(by=['stars', 'state'], ascending=[False, True]).reset_index()

slst = list(df.stars.unique()[:5])

df = df[df['stars'].isin(slst)]
out = df.copy()

for i in slst[::-1]:
    if len(out[out.stars != i]) > 5:
        out = out[out.stars != i]
    else:
        break
```