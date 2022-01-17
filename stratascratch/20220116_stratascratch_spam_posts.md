# Spam Posts

Calculate the percentage of spam posts in all viewed posts by day. A post is considered a spam if a string "spam" is inside keywords of the post. Note that the facebook_posts table stores all posts posted by users. The facebook_post_views table is an action table denoting if a user has viewed a post.

```
DataFrames: facebook_posts, facebook_post_views
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
facebook_posts.head()

# calculate the % of spam posts in all VIEWED posts by DAY
# spam is defined as `post_keywords` == '#spam#'

# 1. filter out unwanted cols
# 2. get the list of all viewed posts
# 3. get number of total posts per day
# 4. get number of spam per day
# 5. get the percentage

df1 = facebook_post_views
df2 = facebook_posts[['post_id', 'post_keywords', 'post_date']]

df_viewed = pd.merge(df1, df2, on='post_id')
total = df_viewed.groupby('post_date').count().reset_index()

spam = df_viewed[df_viewed.apply(lambda x: '#spam#' in x['post_keywords'], axis=1)]
spam = spam.groupby('post_date').count().reset_index()

df_out = pd.merge(spam[['post_date', 'post_id']], total[['post_date', 'post_id']], on='post_date')
df_out['perc'] = df_out.post_id_x / df_out.post_id_y * 100
df_out
```