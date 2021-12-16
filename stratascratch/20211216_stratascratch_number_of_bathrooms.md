# Number Of Bathrooms And Bedrooms

Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.

```
DataFrame: airbnb_search_details
Expected Output Type: pandas.DataFrame
```

```python
# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()

# avg num of bath and bedroom for each city's property types
# output - avg num, city name and prop type

# 1. get columns of interest (property_type, bathrooms, bedrooms, city)
# 2. groupby city then prop type - avg(bath, bed)

df = airbnb_search_details[['property_type', 'bathrooms', 'bedrooms', 'city']]

df = df.groupby(['city', 'property_type']).mean().reset_index()
```