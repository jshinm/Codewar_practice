# Classify Business Type

Classify each business as either a restaurant, cafe, school, or other. A restaurant should have the word 'restaurant' in the business name. For cafes, either 'cafe', 'café', or 'coffee' can be in the business name. 'School' should be in the business name for schools. All other businesses should be classified as 'other'. Output the business name and the calculated classification.

```
DataFrame: sf_restaurant_health_violations
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations.head()

# classify business type: res, cafe, school, other
# res: 'restaurant'
# cafe: 'cafe', 'café', 'coffee'
# school: 'school'
# other: everything else
# output - business name, classification

# 1. get col of interest
# 2. make all lowercases
# 3. categorize by conditionals

def categorize(x):
    tmp = x[['business_name']].str.lower()
    tmp = tmp['business_name']
    
    if 'school' in tmp:
        return 'School'
    elif 'cafe' in tmp or 'café' in tmp or 'coffee' in tmp:
        return 'Cafe'
    elif 'restaurant' in tmp:
        return 'Restaurant'
    else:
        return 'other'

df = sf_restaurant_health_violations[['business_name']]

tmp = df.apply(lambda x: categorize(x), axis=1)#.reset_index()
df = pd.concat([df, tmp],axis=1)
df.columns = [['business_name', 'classification']]

df.drop_duplicates()
```