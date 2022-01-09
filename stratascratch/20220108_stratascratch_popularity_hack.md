# Popularity of Hack

Facebook has developed a new programing language called Hack.To measure the popularity of Hack they ran a survey with their employees. The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored.

Based on the above, find the average popularity of the Hack per office location.
Output the location along with the average popularity.

```
DataFrames: facebook_employees, facebook_hack_survey
Expected Output Type: pandas.Series
```

```python
# Import your libraries
import pandas as pd

# Start writing code
facebook_employees.head()

# find the avg popularity of the hack per office loc
# output the loc along with the avg popularity

# 1. filter table for the col of interest
# 2. join table by `employee_id`
# 3. groupby location - agg(avg(popularity))

dfA = facebook_employees[['id', 'location']]
dfB = facebook_hack_survey[['employee_id', 'popularity']]

out = pd.merge(dfA, dfB, left_on='id', right_on='employee_id')
out = out.groupby('location').mean().reset_index()
out = out[['location', 'popularity']]
```