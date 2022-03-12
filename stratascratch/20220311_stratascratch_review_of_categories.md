# Reviews of Categories

Find the top business categories based on the total number of reviews. Output the category along with the total number of reviews. Order by total reviews in descending order.

```
DataFrame: yelp_business
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# 1. filter columns
# 2. parse text in categories and put them in each row
# 3. group by and sum over review_count
# 4. order by review_count

yelp_business.categories = yelp_business.categories.str.split(';')
yelp_business[['categories', 'review_count']].explode('categories').groupby('categories').sum().reset_index().sort_values('review_count', ascending=False)
```